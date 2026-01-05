import datetime
import pathlib

FILE_PATTERN = "*.txt"
ARCHIVE = "archive"

def main():

    date_string = datetime.datetime.now().strftime('%Y-%m-%d')

    cur_path = pathlib.Path(".")
    archive_path = cur_path.joinpath(ARCHIVE)
    archive_path.mkdir(exist_ok=True)

    date_archive_path = archive_path.joinpath(date_string)
    date_archive_path.mkdir(exist_ok=True)

    paths = cur_path.glob(FILE_PATTERN)

    for path in paths:
        new_filename = f"{path.stem}_{date_string}{path.suffix}"
        #new_path = archive_path.joinpath(new_filename)
        new_path = date_archive_path.joinpath(new_filename)
        path.rename(new_path)

if __name__ == "__main__":
    main()
