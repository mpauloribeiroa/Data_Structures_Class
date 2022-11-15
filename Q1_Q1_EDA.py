#Quiz 1, Question 1, Data Structures, UnB 2022.2
#Program to calculate the difference between two dates
#Input: initial date and time (day hours:minutes:seconds)
#Output: the difference between them

import os
import sys

os.system('cls')

#get beginning date
initial_date = input()
initial_date = str(initial_date)

#get final date
final_date = input()
final_date = str(final_date)

#division in two different lists, one for day and one for the time
initial_date_l1 = initial_date.split() 
initial_date_l2 = initial_date_l1[1].split(":", ) 

#storing the initial moment to convert them to seconds later
initial_day = int(initial_date_l1[0])
if initial_day > 31 or initial_day < 1:
    print("Invalid date!")
    sys.exit()

initial_hour = int(initial_date_l2[0])
if initial_hour > 23 or initial_hour < 0:
    print("Invalid date!")
    sys.exit()

initial_minute = int(initial_date_l2[1])
if initial_minute > 59 or initial_minute < 0:
    print("Invalid date!")
    sys.exit()

initial_second = int(initial_date_l2[2])
if initial_second > 59 or initial_second < 0:
    print("Invalid date!")
    sys.exit()

#division in two different lists, one for day and one for the time
final_date_l1 = final_date.split() #list number 1, dividing day and time
final_date_l2 = final_date_l1[1].split(":", ) #list number 2, dividing time into hours, minutes and seconds

#storing the final moment to convert them to seconds later
final_day = int(final_date_l1[0])
if final_day > 31 or final_day <= 0:
    print("Invalid date!")
    sys.exit()

final_time = int(final_date_l2[0])
if final_time > 23 or final_time < 0:
    print("Invalid date!")
    sys.exit()

final_minute = int(final_date_l2[1])
if final_minute > 59 or final_minute < 0:
    print("Invalid date!")
    sys.exit()

final_second = int(final_date_l2[2])
if final_second > 59 or final_second < 0:
    print("Invalid date!")
    sys.exit()

#convert everything into seconds
beginning_time = (initial_day * 86400) + (initial_hour * 3600) + (initial_minute * 60) + initial_second
final_time = (final_day * 86400) + (final_time * 3600) + (final_minute * 60) + final_second

#fazer a subtração
seconds_duration = final_time - beginning_time

if final_time == beginning_time:
    print("Invalid date!")
    sys.exit()

#convert back into days, hours, minutes and seconds
days_duration = seconds_duration // 86400
seconds_duration = seconds_duration - days_duration * 86400

hours_duration = seconds_duration // 3600
seconds_duration = seconds_duration - hours_duration * 3600

minutes_duration = seconds_duration // 60
seconds_duration = seconds_duration - minutes_duration * 60


#show result
if days_duration < 0 or hours_duration < 0 or minutes_duration < 0 or seconds_duration < 0:
    print ("Invalid date!")
    sys.exit()
   
days_duration = str(days_duration)
print(days_duration + " day(s)")

hours_duration = str(hours_duration)
print(hours_duration + " hour(s)")

minutes_duration = str(minutes_duration)
print(minutes_duration + " minute(s)")

seconds_duration = str(seconds_duration)
print(seconds_duration + " second(s)")