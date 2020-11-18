import argparse
import csv
import os
from datetime import datetime


def write_csv(start_year, end_year, path_to_source_files, destination_filename):
    csv_files = list(filter(lambda x: str(start_year) <= x <= str(int(end_year) + 1),
                            os.listdir(path_to_source_files)))

    with open(f"{destination_filename}.csv", 'a') as f:
        for csv_file in csv_files:
            with open(os.path.join(path_to_source_files, csv_file), 'r') as file:
                reader = csv.reader(file)
                next(reader)
                csv.writer(f).writerows(reader)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-psf", "--path_to_source_files",
                        dest="path_to_source_files",
                        required=True,
                        help='Path to source'
                        )

    parser.add_argument("-sy", "--start_year",
                        dest="start_year",
                        required=False,
                        default=min(os.listdir('beer_review/')),
                        help='The parameter corresponds to the year from which we start the search'
                        )
    parser.add_argument("-ey", "--end_year",
                        dest="end_year",
                        required=False,
                        default=str(sorted(os.listdir('beer_review/'), reverse=True))[2:6],
                        help='The parameter corresponds to the year in which we complete the search'
                        )

    parser.add_argument("-dp", "--destination_path",
                        required=False,
                        default=".",
                        dest="destination_path",
                        help='The path to the new file'
                        )
    arguments_for_name = parser.parse_args()
    parser.add_argument("-dfn", "--destination_filename",
                        required=False,
                        dest="destination_filename",
                        default=f"{arguments_for_name.start_year}-"
                                f"{arguments_for_name.end_year}-"
                                f"{datetime.now().ctime()}",
                        help='The name of file'
                        )
    arguments = parser.parse_args()

    if arguments.path_to_source_files:
        write_csv(start_year=arguments.start_year,
                  end_year=arguments.end_year,
                  path_to_source_files=arguments.path_to_source_files,
                  destination_filename=arguments.destination_filename
                  )


if __name__ == '__main__':
    main()
