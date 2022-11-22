'''
Report Business Hours

We are a mobile app that displays a list of local businesses and want to display the hours each business
is open for throughout the week. For the sake of saving space in the UI, we would like to transform the CSV data
provided below into a format where days with similar hours are condensed into a single line.

Input:

Monday,11:00AM,11:00PM
Tuesday,11:00AM,11:00PM
Wednesday,11:00AM,11:00PM
Thursday,11:00AM,2:00AM
Friday,11:00AM,2:00AM
Saturday,11:00AM,2:00AM
Sunday,,

Output:

Mon-Wed: 11:00AM - 11:00PM
Thu-Sat: 11:00AM - 2:00AM
Sun: Closed

Write a function hours_of_operation(schedule) that accepts a single string argument representing the hours of operation
for a business. The input argument should contain 7 lines of text for each day of the week, with corresponding hours,
separated by commas.  The days of the week should only be combined if there is a continuous streak where consecutive
days have the same hours.
'''

def report_hours(schedule):

    return ''


schedule = '''
Monday,11:00AM,11:00PM
Tuesday,11:00AM,11:00PM
Wednesday,11:00AM,11:00PM
Thursday,11:00AM,2:00AM
Friday,11:00AM,2:00AM
Saturday,11:00AM,2:00AM
Sunday,,
'''

print(report_hours(schedule))
