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
            if letter in "0123456789":
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

if __name__ == "__main__":

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
            counter = 0
            while counter < len(constants.TEAMS):
                print(f"{counter + 1}) {constants.TEAMS[counter]}")
                counter += 1
            try:
                option = int(input("\nEnter an option > "))
                if option < 1 or option > counter:
                    raise ValueError
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