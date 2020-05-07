import constants

players = []
teams = []

def clean_data():

    for player in constants.PLAYERS:
        stats = {'name': player['name'], 'guardians': player['guardians']}
        if player['experience'] == "YES":
            stats['experience'] = True
        if player['experience'] == "NO":
            stats['experience'] = False
        height = ""
        for letter in player['height']:
            if letter == "0" or letter == "1" or letter == "2" or letter == "3" or letter == "4" or letter == "5" or letter == "6" or letter == "7" or letter == "8" or letter == "9":
                height = height + letter
        stats['height'] = int(height)
        players.append(stats)

def balance_teams(team):

    player_number = 0
    for x in range(len(constants.TEAMS)):
        for z in range(int(len(constants.PLAYERS) / len(constants.TEAMS))):
            if team == x:
                print(constants.PLAYERS[player_number]['name'])
            player_number += 1

clean_data()

print("BASKETBALL TEAM STATS TOOL\n")
print("---- MENU ----\n")
print("Here are your choices")
print("1) Display Team Stats")
print("2) Quit\n")
while True:
    try:
        option = int(input("Enter an option > "))
        if option != 1 and option != 2:
            raise ValueError
    except:
        print("That is not a valid entry")
    else:
        break
if option == 1:
    print("")
    while True:
        for x in range(len(constants.TEAMS)):
            print(f"{x + 1}) {constants.TEAMS[x]}")
        try:
            option = int(input("\nEnter an option > "))
        except:
            print("That is not a valid entry")
        else:
            break
    option -= 1
    print(f"\nTeam: {constants.TEAMS[option]} Stats")
    print("--------------------")
    print("Total Players: ", int(len(constants.PLAYERS) / len(constants.TEAMS)), "\n")
    print("Players on Team:\n")
    balance_teams(option)
elif option == 2:
    print("Goodbye!")