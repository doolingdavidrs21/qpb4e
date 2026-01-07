def hello_world():
    print("Hello, World!")


def main():
    hello_world()

    # Read temperature data from file
    temperatures = []
    try:
        with open('code/Chapter 05/lab_05.txt') as infile:
            for row in infile:
                temperatures.append(float(row.strip()))
    except FileNotFoundError:
        print("Temperature file not found")
        return

    if not temperatures:
        print("No temperature data found")
        return

    # Find highest and lowest temperatures
    highest = max(temperatures)
    lowest = min(temperatures)

    # Calculate the mean (average)
    mean = sum(temperatures) / len(temperatures)

    # Calculate the median
    sorted_temps = sorted(temperatures)
    n = len(sorted_temps)
    if n % 2 == 0:
        median = (sorted_temps[n // 2 - 1] + sorted_temps[n // 2]) / 2
    else:
        median = sorted_temps[n // 2]

    # Print results
    print(f"Number of temperatures: {len(temperatures)}")
    print(f"Highest temperature: {highest}")
    print(f"Lowest temperature: {lowest}")
    print(f"Mean temperature: {mean:.2f}")
    print(f"Median temperature: {median}")


if __name__ == "__main__":
    main()
