import argparse
import csv
import os
from time import gmtime


def make_data(source_file_path):
    data = []
    with open(os.path.join(source_file_path)) as csv_data:
        reader = csv.DictReader(csv_data)
        for row in reader:
            data.append(row)
    return data


def get_weekday(time_in_sec):
    data = ['Monday', "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    return data[gmtime(time_in_sec).tm_wday]


def max_grade(d):
    grade = []
    for row in d:
        grade.append(float(row.get('review_overall')) +
                     float(row.get('review_aroma')) +
                     float(row.get('review_taste')))
    return max(grade)


def check_grade(a):
    grade = (float(a.get('review_overall')) +
             float(a.get('review_aroma')) +
             float(a.get('review_taste')))
    return grade


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

    data = make_data(arguments.source_file_path)
    a = max_grade(data)

    if arguments.beer_type:
        print("_________________________________The most popular beer types")

        data_beer_type = filter(lambda x: a == check_grade(a=x),
                                data)
        for i in data_beer_type:
            print(i.get('beer_style'))

    if arguments.beer_name:
        print("_________________________________The most popular beer names")

        data_beer_names = filter(lambda x: a == check_grade(a=x),
                                 data)
        for i in data_beer_names:
            print(i.get('beer_name'))

    if arguments.day_of_review:
        print("_________________________________Day with they most number of review")
        data_of_days = {'Monday': 0, "Tuesday": 0, "Wednesday": 0,
                        "Thursday": 0, "Friday": 0, "Saturday": 0, "Sunday": 0}

        for row in data:
            data_of_days[get_weekday(float(row.get('review_time')))] += 1
        print(max(data_of_days, key=data_of_days.get))

    if arguments.reviewer_stats:
        print("_________________________________Reviewer stats")
        data_stats_of_review = {}

        with open(os.path.join(arguments.source_file_path)) as csv_data:
            reader = csv.DictReader(csv_data)
            for row in reader:
                data_stats_of_review.setdefault(row.get('review_profilename'), 0)
                data_stats_of_review[row.get('review_profilename')] = data_stats_of_review[
                                                                          row.get('review_profilename')] + 1
        for i in data_stats_of_review:
            print(f"{i:20} : {data_stats_of_review[i]} review")


if __name__ == '__main__':
    main()
