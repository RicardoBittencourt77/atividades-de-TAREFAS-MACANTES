import pyperclip
import re
from datetime import datetime
from time import sleep

text = pyperclip.paste()

formats = [  # first, day
    '%d/%m/%Y', '%d-%m-%Y', '%d.%m.%Y', '%d/%m/%y', '%d-%m-%y', '%d.%m.%y',
    '%e/%f/%Y', '%e-%f-%Y', '%e.%f.%Y', '%e/%f/%y', '%e-%f-%y', '%e.%f.%y',
    # first, year
    '%Y/%m/%d', '%Y-%m-%d', '%Y.%m.%d', '%Y/%f/%e', '%Y-%f-%e', '%Y.%f.%e',
    # first, month
    '%m/%d/%Y', '%m-%d-%Y', '%m.%d.%Y', '%f/%e/%Y', '%f-%e-%Y', '%f.%e.%Y',
    '%m/%d/%y', '%m-%d-%y', '%m.%d.%y', '%f/%e/%Y', '%f-%e-%Y', '%f.%e.%Y',
    # format: Month d, yyyy   output: January 19, 2007
    '%b %e, %Y', '%B %e, %Y', '%b %d, %Y', '%B %d, %Y',
    # format: dd/mm/yyyy hh:mm:ss or dd-mm-yyyy hh:mm:ss   output: 19/01/2007 10:00:00 or 19-01-2007 10:00:00
    '%d/%m/%Y %H:%M:%S', '%d-%m-%Y %H:%M:%S',
    # format: yyyy/mm/dd hh:mm:ss or yyyy-mm-dd hh:mm:ss   output: 2007/01/19 10:00:00 or 2007-01-19 10:00:00
    '%Y/%m/%d %H:%M:%S', '%Y-%m-%d %H:%M:%S',
    # output: 19 January 2007 - '19 de janeiro de 2007' (are not case sensitive - 'não diferenciam letras maiúsculas de minúsculas',
    # january, January, JANuary or JANUARY - 'janeiro, Janeiro, JANeiro ou JANEIRO')
    '%d %B %Y']

standard_format = '%d/%m/%Y'
format_found = None
findDates = re.compile(r''' # finds formats starting with 'day'
                        ((\d{1,2}[/-]\d{1,2}[/-]\d{2,4})
                        |(\d{1,2}\.\d{1,2}\.\d{2,4})
                        # finds formats starting with 'day'
                        |(\d{4}[/-]\d{1,2}[/-]\d{1,2})
                        |(\d{4}\.\d{1,2}\.\d{1,2})
                        )''', re.X)

# converting the formats below did not return the expected result
'''                        # finds the formats that contain the name of the month
                        |([a-zA-Z]{1,9}\s\d{1,2},\s\d{2,4})
                        |(\d{1,2}\s[de]{1,2}\s[a-zA-ZçÇ]{1,9}\s[de]{1,2}\s\d{4})
'''

matches = []

print('\nLooking for Dates...')
sleep(3)

for groups in findDates.findall(text):
    print(groups[0])
    for each_format in formats:
        try:
            groups_to_string = ''.join(groups[0])
            date_format = datetime.strptime(groups_to_string, each_format)
            format_found = each_format
            break
        except ValueError:
            pass  # format not found
    if format_found is not None:  # if found a format, convert the date to the other format
        date = datetime.strftime(date_format, standard_format)
        matches.append(date)

if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('\nCopied to clipboard:')
    print('\n'.join(matches))
else:
    print('No date found.')
