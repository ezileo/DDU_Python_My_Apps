#user_name = input('Please input your Name: ')
#print('Welcome to the Birthday App {}'.format(user_name))

import datetime

def print_header():
    print('--------------------------------------')
    print('             THE BIRTHDAY APP         ')
    print('--------------------------------------')
    print()


def get_birthday_from_user():
    print('Tell us when you were born: ')
    year = int(input('Year of Birth [YYYY]: '))
    month = int(input('Month of Birth [MM]: '))
    day = int(input('Day of Birth [DD]: '))
    birthday = datetime.datetime(year, month, day)
    return birthday


def compute_days_between_dates(orignal_date, now):
    date1 = now
    date2 = datetime.datetime(now.year, orignal_date.month, orignal_date.day)
    dt = date1 - date2
    days = int(dt.total_seconds() / 60 / 60 / 24)
    return days


def print_birthday_information(days):
    if days < 0:
        print('Your Birthday is in {} days!'.format(-days))
    elif days >0:
        print ('You already had your birthday this year {} days ago!!!'.format(days))
    else:
        print('Happy Birthday Mate!!!')


def main():
    print_header()
    bday = get_birthday_from_user()
    print(bday)
    now = datetime.datetime.now()
    number_of_days = compute_days_between_dates(bday, now)
    print(number_of_days)
    print_birthday_information(number_of_days)

main()
