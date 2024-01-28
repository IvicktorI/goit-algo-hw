import datetime as dt
from datetime import datetime as dtdt
import os
os.system('cls')

users=[{'name': 'Ekaterina', 'birthday': '1985.1.28'},
       {'name': 'Vladislav', 'birthday': '1983.02.04'},
       {'name': 'Dariya', 'birthday': '1989.02.28'},
       {'name': 'Viktor', 'birthday': '1992.03.19'},
       {'name': 'Aleksandra', 'birthday': '1988.07.19'},
       {'name': 'Ivan', 'birthday': '1984.02.13'},
       {'name': 'Vasiliy', 'birthday': '1984.09.04'},
       {'name': 'Vladimir', 'birthday': '1981.08.06'},
       {'name': 'Bogdana', 'birthday': '1999.12.09'},
       {'name': 'Dobrinya', 'birthday': '1990.04.28'},
       {'name': 'Vladislava', 'birthday': '1981.12.04'}
       ]

def get_upcoming_birthdays(users):
    # congratulation list
    clist=[]
    # congratulation week
    # today = begin
    # today + 7 days = end
    begin= dtdt.today().date()
    end=dtdt.fromordinal(7+dtdt.toordinal(begin)).date()
    for i in users:
        # temp - birthday in current year
        temp=dtdt.strptime(i['birthday'], "%Y.%m.%d").date().replace(year=begin.year)
        if temp>=begin and temp<=end:
            if temp.weekday()==5:
                c=temp.replace(day=temp.day+2)
                temp=c
            if temp.weekday()==6:
                c=temp.replace(day=temp.day+1)
                temp=c
            clist.append({'name':i['name'], 'congratulation_date':dtdt.strftime(temp, "%Y.%m.%d")})

    return clist

print(get_upcoming_birthdays(users))