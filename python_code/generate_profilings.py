import pandas as pd
import os
import dotenv
from ydata_profiling import ProfileReport


def get_filenames() -> list:
    """Returns a list with all the filenames in the data folder that end with .csv"""
    data_folder = dotenv.get_key(dotenv.find_dotenv(), "DATA_FOLDER")
    filenames = os.listdir(data_folder)
    filenames = [filename for filename in filenames if filename.endswith(".csv")]
    return filenames


def generate_report(filename: str) -> None:
    data_folder = dotenv.get_key(dotenv.find_dotenv(), "DATA_FOLDER")
    reports_path = os.path.join(data_folder, "profilings")

    # create profilings folder inside data folder
    if not os.path.exists(reports_path):
        os.mkdir(reports_path)

    df = pd.read_csv(os.path.join(data_folder, filename))
    profile = ProfileReport(df, title=filename)
    profile.to_file(os.path.join(reports_path, f"{filename.replace('.csv', '')}_report.html"))


def main():
    filenames = get_filenames()
    if len(filenames) != 12:
        raise FileNotFoundError(f"{dotenv.get_key(dotenv.find_dotenv(), 'DATA_FOLDER')} does not contain 12 csv files")
    for filename in filenames:
        generate_report(filename)


def print_schema(filename):
    data_folder = dotenv.get_key(dotenv.find_dotenv(), "DATA_FOLDER")
    df = pd.read_csv(os.path.join(data_folder, filename))
    print(f"filename: {filename}")
    print(f"columns: {list(df.columns)}")


def print_schemas():
    filenames = get_filenames()
    for filename in filenames:
        print_schema(filename)


if __name__ == "__main__":
    print_schemas()
