from datetime import datetime, date
import calendar


def get_user_birthday():
    print("Введите дату вашего рождения:")

    while True:
        try:
            day = int(input("День (1-31): "))
            month = int(input("Месяц (1-12): "))
            year = int(input("Год (например, 1990): "))

            birthday = date(year, month, day)
            return birthday
        except ValueError:
            print("Ошибка! Пожалуйста, введите корректную дату.")


def get_weekday(birthday):
    weekdays = ["Понедельник", "Вторник", "Среда", "Четверг",
                "Пятница", "Суббота", "Воскресенье"]
    return weekdays[birthday.weekday()]


def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


def calculate_age(birthday):
    today = date.today()
    age = today.year - birthday.year

    if today.month < birthday.month or (today.month == birthday.month and today.day < birthday.day):
        age -= 1

    return age


def get_digit_patterns():
    patterns = {
        '0': [
            " *** ",
            "*   *",
            "*   *",
            "*   *",
            " *** "
        ],
        '1': [
            "  *  ",
            " **  ",
            "  *  ",
            "  *  ",
            " *** "
        ],
        '2': [
            " *** ",
            "*   *",
            "   * ",
            "  *  ",
            "*****"
        ],
        '3': [
            " *** ",
            "*   *",
            "  ** ",
            "*   *",
            " *** "
        ],
        '4': [
            "*   *",
            "*   *",
            "*****",
            "    *",
            "    *"
        ],
        '5': [
            "*****",
            "*    ",
            "**** ",
            "    *",
            "**** "
        ],
        '6': [
            " *** ",
            "*    ",
            "**** ",
            "*   *",
            " *** "
        ],
        '7': [
            "*****",
            "    *",
            "   * ",
            "  *  ",
            " *   "
        ],
        '8': [
            " *** ",
            "*   *",
            " *** ",
            "*   *",
            " *** "
        ],
        '9': [
            " *** ",
            "*   *",
            " ****",
            "    *",
            " *** "
        ],
        ' ': [
            "     ",
            "     ",
            "     ",
            "     ",
            "     "
        ]
    }
    return patterns


def print_big_digits(number_str):

    patterns = get_digit_patterns()
    lines = [""] * 5

    for digit in number_str:
        if digit in patterns:
            for i in range(5):
                lines[i] += patterns[digit][i] + "  "
        else:
            for i in range(5):
                lines[i] += patterns[' '][i] + "  "

    for line in lines:
        print(line)


def main():
    birthday = get_user_birthday()

    print("\n" + "=" * 50)
    print("ИНФОРМАЦИЯ О ВАШЕМ ДНЕ РОЖДЕНИЯ")
    print("=" * 50)

    weekday = get_weekday(birthday)
    print(f"Вы родились в: {weekday}")

    leap = is_leap_year(birthday.year)
    leap_str = "был високосным" if leap else "не был високосным"
    print(f"Год {birthday.year} {leap_str}")

    age = calculate_age(birthday)
    print(f"Сейчас вам: {age} лет")

    print("\n" + "=" * 50)
    print("ВАША ДАТА РОЖДЕНИЯ НА ТАБЛО:")
    print("=" * 50)

    date_str = birthday.strftime("%d %m %Y")
    print_big_digits(date_str)


if __name__ == "__main__":
    main()
