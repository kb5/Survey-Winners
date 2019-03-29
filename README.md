# Survey-Winners
A random selection program used to randomly select winners from a list of names. 

# How does it work?
When MyVoice Winner.py is ran, it will ask you how many nanmes for it to select. It will then look though the file named "employee_roster.txt" and randomly select n names. It will display the names, as well as append them to another file named "past_winners.txt" along with a timestamp. The next time the program is ran, it will also search the "past_winners.txt" file to make sure the same name does not get selected twice. 

# Why?
At my work, we had a monthly drawing for VIP parking spots in our parking lot. This program is what I came up with to select the winners. It would pick new winners every time and keep a log of who won for any given month.
