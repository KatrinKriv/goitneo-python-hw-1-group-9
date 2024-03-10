from collections import defaultdict
from datetime import datetime, timedelta


def get_birthdays_per_week(users):
    weekdays = [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday",
    ]

    birthdays_by_weekday = defaultdict(list)

    today = datetime.today().date()

    today += timedelta(days=(7 - today.weekday()))

    for user in users:
        name = user["name"]
        birthday = user["birthday"].date()
        birthday_this_year = birthday.replace(year=today.year)

        delta_days = (birthday_this_year - today).days

        if delta_days < 0:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)
            delta_days = (birthday_this_year - today).days

        weekday = birthday_this_year.strftime("%A")

        birthdays_by_weekday[weekday].append(name)

    for weekday in weekdays:
        if weekday == "Monday":
            if birthdays_by_weekday["Saturday"] or birthdays_by_weekday["Sunday"]:
                print(
                    f"{weekday}: {', '.join(birthdays_by_weekday['Saturday'])}, {', '.join(birthdays_by_weekday['Sunday'])}"
                )
            else:
                print(f"{weekday}: {', '.join(birthdays_by_weekday[weekday])}")
        else:
            print(f"{weekday}: {', '.join(birthdays_by_weekday[weekday])}")
