# MyVoice Winner.py
# Written by Kevin Blank
# 2018-02-19

# This program reads in a txt file of current employees and randomly chooses a number you select. Those winners are
#   then displayed to the screen, as well as written to a text file "past_winners.txt". The winners
#   are verified by first making sure they are not selected multiple times and that they are were
#   not selected previously (as in a winner from past months).

import random
import datetime

# Variables for number of names to draw, input file, and output file.
num_to_draw = input("How many names would you like to select? ")
input_file = "employee_roster.txt"
past_winners_file = "past_winners.txt"

# Variables for date, a winners list, and a past winners list.
today = datetime.date.today()
winners = []
past_winners = []

past_file = open(past_winners_file, 'r+')
past_file.write(str(today) + " -------------------------------------------------------\n")

# Make a list of the past winners.
for x in past_file:
    past_winners.append(past_file.readlines())

print(str(past_winners))

# Loop to draw the names of the winners for garage access.
for x in range(int(num_to_draw)):
    line = random.choice(open(input_file).readlines())

    while line not in winners:
        if line not in past_winners:
            winners.append(line)
            past_file.write(line)
        else:
            print("Error: Person already a past winner. Finding another...")

past_file.write("\n")
past_file.close()

# Output results to the screen.
print("\nThe MyVoice Garage Winners are: \n")

for x in range(int(num_to_draw)):
    print(winners[x])

print("\nThis selection was generated on " + str(today))