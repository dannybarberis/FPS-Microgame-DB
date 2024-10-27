# Daniel Barberis
# Assignment 6: Tournament
# COP2500C-0004
# 10/19/24

# Initial Divisions Question
divisions_total = int(input("How many divisions are in the tournament?\n\n"))
divisions_start = 1

# Variable Declaration
players_start = 1
time_average = 0
time_winner = 0

#While Loop to handle all divisions, as well as printing
while(divisions_total > 0):
    players_total = int(input("\nHow many players are in division #"+ str(divisions_start)+"?\n\n"))
    players_total_initial = players_total
    time_temp = 1000
    # Nested While loop to handle all players , times, and averages
    while(players_total > 0):
        time_count = int(input("\nWhat was the time of player #"+ str(players_start)+"?\n\n"))
        time_average = time_average + time_count
        # Nested if statement to track lowest time
        if(time_count < time_temp):
            time_winner = time_count
            time_temp = time_count
        players_start += 1
        players_total -= 1
        average = time_average / players_total_initial
    # Prints for each division, kept in division while loop
    print("\nDivision #"+ str(divisions_start)+" results:\n")
    print("Best Time:", time_winner,"seconds\n")
    print("Average Time: %.1f"% average,"seconds")
    divisions_start += 1
    divisions_total -= 1
    players_start = 1
    time_average = 0
