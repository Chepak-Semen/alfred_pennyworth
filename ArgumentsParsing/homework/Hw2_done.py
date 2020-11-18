import argparse
import csv
import os
from time import gmtime


def get_weekday(time_in_sec):
    data = ['Monday', "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    return data[gmtime(time_in_sec).tm_wday]


def max_grade(source_file_path):
    grade = []
    with open(os.path.join(source_file_path)) as csv_data:
        reader = csv.DictReader(csv_data)
        for row in reader:
            grade.append(float(row.get('review_overall')) +
                         float(row.get('review_aroma')) +
                         float(row.get('review_taste')))

    return max(grade)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-sfp', '--source_file_path',
                        required=True,
                        dest="source_file_path",
                        help="Path to files",
                        )
    parser.add_argument("-bt", "--beer_type",
                        required=False,
                        dest="beer_type",
                        help="Choose type of beer",
                        action="store_true"
                        )
    parser.add_argument("-bn", "--beer_name",
                        required=False,
                        dest="beer_name",
                        help="Choose beer name",
                        action="store_true"
                        )
    parser.add_argument('-dor', '--day_of_review',
                        required=False,
                        dest="day_of_review",
                        help="Day of review",
                        action="store_true"
                        )
    parser.add_argument('-rs', '--reviewer_stats',
                        required=False,
                        dest="reviewer_stats",
                        help="Name of reviewer",
                        action="store_true"
                        )
    arguments = parser.parse_args()

    if arguments.beer_type:
        print("_________________________________The most popular beer types_________________________________")
        data = []

        with open(os.path.join(arguments.source_file_path)) as csv_data:
            reader = csv.DictReader(csv_data)
            for row in reader:
                grade = (float(row.get('review_overall')) +
                         float(row.get('review_aroma')) +
                         float(row.get('review_taste')))
                if grade == max_grade(os.path.join(arguments.source_file_path)):
                    data.append(row.get('beer_style'))
            print(data)

    if arguments.beer_name:
        print("_________________________________The most popular beer names_________________________________")
        data = []

        with open(os.path.join(arguments.source_file_path)) as csv_data:
            reader = csv.DictReader(csv_data)
            for row in reader:
                grade = (float(row.get('review_overall')) +
                         float(row.get('review_aroma')) +
                         float(row.get('review_taste')))
                if grade == max_grade(os.path.join(arguments.source_file_path)):
                    data.append(row.get('beer_name'))
        print(data)

    if arguments.day_of_review:
        print("_____________________________Day with they most number of review_____________________________")
        data = {'Monday': 0, "Tuesday": 0, "Wednesday": 0,
                "Thursday": 0, "Friday": 0, "Saturday": 0, "Sunday": 0}

        with open(os.path.join(arguments.source_file_path)) as csv_data:
            reader = csv.DictReader(csv_data)
            for row in reader:
                data[get_weekday(float(row.get('review_time')))] += 1
        print(sorted(data.items(), key=lambda v: v[-1], reverse=True)[0])

    if arguments.reviewer_stats:
        data = {}

        with open(os.path.join(arguments.source_file_path)) as csv_data:
            reader = csv.DictReader(csv_data)
            for row in reader:
                data.setdefault(row.get('review_profilename'), 0)
                data[row.get('review_profilename')] = data[row.get('review_profilename')] + 1
        print("_______________________________________reviewer_stats________________________________________")
        for i in data:
            print(f"{i} : {data[i]}")


if __name__ == '__main__':
    main()
