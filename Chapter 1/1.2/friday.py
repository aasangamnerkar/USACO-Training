"""
ID: aasangamnerkar
LANG: PYTHON3
PROG: friday
"""

INPUTFILE = "friday.in"
OUTFILE = "friday.out"


fin = open (INPUTFILE, 'r')
fout = open (OUTFILE, 'w')

input_array = []
for line in fin:
    count_array = []
    input_array.append(str(line).split("\n")[0])

EXTRA_YEARS = int(input_array[0])
STARTING_YEAR = 1900
END_YEAR = 1900 + EXTRA_YEARS
MONTH_ARRAY = ["Jan", "Feb", "March", "Apr", "May", "June", "July", "Aug", "Sept", "Oct", "Nov", "Dec"]
WEEK_ARRAY = ["Mon", "Tues", "Wed", "Thurs", "Fri", "Sat", "Sun"]

count_array = []
for day in WEEK_ARRAY:
    count_array.append([day, 0])

def isLeap(year):
    if year % 4 == 0 and year % 100 != 0:
        return True
    elif year % 100 == 0 and year % 400 == 0:
        return True
    return False

def getDays(month, year):
    if (month == "Sept" or month == "Apr" or month == "June" or month == "Nov"):
        return 30
    elif (month == "Jan" or month == "March" or month == "May" or month == "July" or month == "Aug" or month == "Oct" or month == "Dec"):
        return 31
    elif (month == "Feb"):
        if (isLeap(year)):
            return 29
        else:
            return 28

def getDayOfWeek(counter):
    if (counter % 7 != 0):
        return counter % 7 - 1
    else:
        return 6

day_index = 0
current_day = WEEK_ARRAY[day_index]
for year in range(STARTING_YEAR, END_YEAR):
    for month in MONTH_ARRAY:
        days_in_month = getDays(month, year)
        for day in range(1, days_in_month+1):
            day_index += 1
            current_day = WEEK_ARRAY[getDayOfWeek(day_index)]
            if day == 13:
                count_array[getDayOfWeek(day_index)][1] += 1

output = ""
output += str(count_array[5][1]) + " "
output += str(count_array[6][1]) + " "
output += str(count_array[0][1]) + " "
output += str(count_array[1][1]) + " "
output += str(count_array[2][1]) + " "
output += str(count_array[3][1]) + " "
output += str(count_array[4][1]) + "\n"

fout.write(output)