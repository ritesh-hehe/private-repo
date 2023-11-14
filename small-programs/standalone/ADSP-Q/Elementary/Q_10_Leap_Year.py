# Write a program that prints the next 20 leap years.
# NOTE: Next 20 is rather subjective. I reckon 20 from when the program is run...

import datetime


def leap_years_20(curr_year: int) -> None:
    leap_counter = 0
    print(f"The 20 leap years from {curr_year} are: ")
    while True:
        # Source: wikipedia
        if ((curr_year % 4 == 0) and (curr_year % 100 != 0) or (curr_year % 400 == 0)):
            leap_counter += 1
            print(curr_year)
        if (leap_counter == 20):
            break
        curr_year += 1


if __name__ == '__main__':
    leap_years_20(int(datetime.datetime.strftime(
        datetime.datetime.now(), '%Y')))
