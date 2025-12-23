#!/usr/bin/env python3.12
"""
GPU Benchmark: pandas vs cuDF Performance Comparison

Tests various DataFrame operations to see if GPU acceleration
provides meaningful speedups ("is the juice worth the squeeze?").

Run with: python3.12 gpu_benchmark.py
"""

import time
import traceback
import numpy as np

# We'll import cudf conditionally to allow testing pandas-only too
HAS_CUDF = False
cudf = None
cp = None

try:
    # Import cupy first and set device
    import cupy as cp_module
    cp_module.cuda.Device(0).use()

    # Import cudf after CUDA is initialized
    import cudf as cudf_module

    # Test that it works
    test_arr = cp_module.array([1, 2, 3])
    test_df = cudf_module.DataFrame({'test': test_arr})
    del test_arr, test_df

    # Set globals
    cp = cp_module
    cudf = cudf_module
    HAS_CUDF = True
    print(f"GPU detected: {cp.cuda.runtime.getDeviceProperties(0)['name'].decode()}")
except ImportError as e:
    print(f"Warning: cuDF not available ({e}), running pandas-only benchmark")
except Exception as e:
    print(f"Warning: CUDA initialization failed: {e}")
    traceback.print_exc()

import pandas as pd


def benchmark(func, name, runs=3):
    """Run a function multiple times and return average time."""
    times = []
    result = None
    for i in range(runs):
        start = time.perf_counter()
        result = func()
        elapsed = time.perf_counter() - start
        times.append(elapsed)
    avg_time = sum(times) / len(times)
    return avg_time, result


def format_speedup(pandas_time, cudf_time):
    """Format speedup ratio."""
    if cudf_time > 0:
        speedup = pandas_time / cudf_time
        if speedup >= 1:
            return f"{speedup:.1f}x faster"
        else:
            return f"{1/speedup:.1f}x slower"
    return "N/A"


def print_result(operation, pandas_time, cudf_time):
    """Print benchmark result in a formatted way."""
    speedup = format_speedup(pandas_time, cudf_time)
    print(f"  {operation:40} | {pandas_time*1000:10.2f} ms | {cudf_time*1000:10.2f} ms | {speedup}")


def main():
    print("=" * 80)
    print("GPU Benchmark: pandas vs cuDF (RAPIDS)")
    print("=" * 80)

    # Test sizes - start small and scale up
    test_sizes = [
        100_000,      # 100K rows
        1_000_000,    # 1M rows
        10_000_000,   # 10M rows
        50_000_000,   # 50M rows (if memory allows)
    ]

    for n in test_sizes:
        print(f"\n{'='*80}")
        print(f"Testing with {n:,} rows")
        print(f"{'='*80}")

        # Check if we have enough memory (rough estimate: 100 bytes per row)
        estimated_mb = n * 100 / (1024 * 1024)
        print(f"Estimated memory usage: ~{estimated_mb:.0f} MB per DataFrame")

        try:
            run_benchmarks(n)
        except MemoryError:
            print(f"  Skipping - not enough memory for {n:,} rows")
            break
        except Exception as e:
            print(f"  Error: {e}")
            traceback.print_exc()
            break


def run_benchmarks(n):
    """Run all benchmarks for a given data size."""

    print(f"\n  {'Operation':40} | {'pandas':>10} | {'cuDF':>10} | Speedup")
    print("  " + "-" * 75)

    # =========================================================================
    # 1. DataFrame Creation from arrays
    # =========================================================================

    # Create random data using NumPy (for pandas)
    np.random.seed(42)
    categories = np.random.randint(0, 100, n)
    nums = np.random.randint(10, 1000, n)
    floats = np.random.random(n) * 100

    def create_pandas_df():
        df = pd.DataFrame({
            'category': categories,
            'num': nums,
            'float': floats
        })
        df['category'] = df['category'].astype('category')
        return df

    pandas_time, pandas_df = benchmark(create_pandas_df, "Create DataFrame")

    if HAS_CUDF:
        # Create data on GPU using CuPy
        cp.random.seed(42)
        categories_gpu = cp.random.randint(0, 100, n)
        nums_gpu = cp.random.randint(10, 1000, n)
        floats_gpu = cp.random.random(n) * 100

        def create_cudf_df():
            df = cudf.DataFrame({
                'category': categories_gpu,
                'num': nums_gpu,
                'float': floats_gpu
            })
            df['category'] = df['category'].astype('category')
            return df

        cudf_time, cudf_df = benchmark(create_cudf_df, "Create DataFrame")
    else:
        cudf_time = float('inf')
        cudf_df = None

    print_result("1. Create DataFrame", pandas_time, cudf_time)

    # =========================================================================
    # 2. GroupBy Aggregation
    # =========================================================================

    def pandas_groupby():
        return (
            pandas_df
            .groupby(by='category')
            .agg({'num': 'sum', 'float': 'mean'})
            .reset_index()
        )

    pandas_time, _ = benchmark(pandas_groupby, "GroupBy Aggregation")

    if HAS_CUDF:
        def cudf_groupby():
            return (
                cudf_df
                .groupby(by='category')
                .agg({'num': 'sum', 'float': 'mean'})
                .reset_index()
            )
        cudf_time, _ = benchmark(cudf_groupby, "GroupBy Aggregation")
    else:
        cudf_time = float('inf')

    print_result("2. GroupBy Aggregation", pandas_time, cudf_time)

    # =========================================================================
    # 3. Filtering
    # =========================================================================

    def pandas_filter():
        return pandas_df[(pandas_df['num'] > 500) & (pandas_df['float'] < 50)]

    pandas_time, _ = benchmark(pandas_filter, "Filter rows")

    if HAS_CUDF:
        def cudf_filter():
            return cudf_df[(cudf_df['num'] > 500) & (cudf_df['float'] < 50)]
        cudf_time, _ = benchmark(cudf_filter, "Filter rows")
    else:
        cudf_time = float('inf')

    print_result("3. Filter rows", pandas_time, cudf_time)

    # =========================================================================
    # 4. Sorting
    # =========================================================================

    def pandas_sort():
        return pandas_df.sort_values(by=['category', 'num'], ascending=[True, False])

    pandas_time, _ = benchmark(pandas_sort, "Sort")

    if HAS_CUDF:
        def cudf_sort():
            return cudf_df.sort_values(by=['category', 'num'], ascending=[True, False])
        cudf_time, _ = benchmark(cudf_sort, "Sort")
    else:
        cudf_time = float('inf')

    print_result("4. Sort by multiple columns", pandas_time, cudf_time)

    # =========================================================================
    # 5. Arithmetic Operations (Vectorized)
    # =========================================================================

    def pandas_arithmetic():
        return pandas_df['num'] * 2 + pandas_df['float'] / 10

    pandas_time, _ = benchmark(pandas_arithmetic, "Vectorized arithmetic")

    if HAS_CUDF:
        def cudf_arithmetic():
            return cudf_df['num'] * 2 + cudf_df['float'] / 10
        cudf_time, _ = benchmark(cudf_arithmetic, "Vectorized arithmetic")
    else:
        cudf_time = float('inf')

    print_result("5. Vectorized arithmetic", pandas_time, cudf_time)

    # =========================================================================
    # 6. Value Counts
    # =========================================================================

    def pandas_value_counts():
        return pandas_df['category'].value_counts()

    pandas_time, _ = benchmark(pandas_value_counts, "Value counts")

    if HAS_CUDF:
        def cudf_value_counts():
            return cudf_df['category'].value_counts()
        cudf_time, _ = benchmark(cudf_value_counts, "Value counts")
    else:
        cudf_time = float('inf')

    print_result("6. Value counts", pandas_time, cudf_time)

    # =========================================================================
    # 7. Join/Merge Operations
    # =========================================================================

    # Create a smaller lookup table
    lookup_size = min(100, n // 1000)
    lookup_pd = pd.DataFrame({
        'category': range(lookup_size),
        'category_name': [f'Cat_{i}' for i in range(lookup_size)]
    })

    def pandas_merge():
        return pandas_df.merge(lookup_pd, on='category', how='left')

    pandas_time, _ = benchmark(pandas_merge, "Merge/Join")

    if HAS_CUDF:
        lookup_cudf = cudf.DataFrame(lookup_pd)

        def cudf_merge():
            return cudf_df.merge(lookup_cudf, on='category', how='left')
        cudf_time, _ = benchmark(cudf_merge, "Merge/Join")
    else:
        cudf_time = float('inf')

    print_result("7. Merge/Join", pandas_time, cudf_time)

    # =========================================================================
    # 8. Describe (Statistics)
    # =========================================================================

    def pandas_describe():
        return pandas_df.describe()

    pandas_time, _ = benchmark(pandas_describe, "Describe statistics")

    if HAS_CUDF:
        def cudf_describe():
            return cudf_df.describe()
        cudf_time, _ = benchmark(cudf_describe, "Describe statistics")
    else:
        cudf_time = float('inf')

    print_result("8. Describe (statistics)", pandas_time, cudf_time)

    # =========================================================================
    # 9. CSV Write (I/O bound test)
    # =========================================================================

    # Only test with smaller sizes to avoid disk slowdowns
    if n <= 1_000_000:
        def pandas_to_csv():
            pandas_df.to_csv('/tmp/pandas_test.csv', index=False)

        pandas_time, _ = benchmark(pandas_to_csv, "Write CSV", runs=1)

        if HAS_CUDF:
            def cudf_to_csv():
                cudf_df.to_csv('/tmp/cudf_test.csv', index=False)
            cudf_time, _ = benchmark(cudf_to_csv, "Write CSV", runs=1)
        else:
            cudf_time = float('inf')

        print_result("9. Write CSV", pandas_time, cudf_time)

        # CSV Read
        def pandas_read_csv():
            return pd.read_csv('/tmp/pandas_test.csv')

        pandas_time, _ = benchmark(pandas_read_csv, "Read CSV", runs=1)

        if HAS_CUDF:
            def cudf_read_csv():
                return cudf.read_csv('/tmp/pandas_test.csv')
            cudf_time, _ = benchmark(cudf_read_csv, "Read CSV", runs=1)
        else:
            cudf_time = float('inf')

        print_result("10. Read CSV", pandas_time, cudf_time)


if __name__ == "__main__":
    main()
    print("\n" + "=" * 80)
    print("Benchmark complete!")
    print("=" * 80)
