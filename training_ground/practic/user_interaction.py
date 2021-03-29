from Player import Player
import json


def main():
    editing = True
    players = []
    with open("players.json", "r") as f:
        for i in json.load(f):
            player = Player(i["name"], i["last name"])
            player.set_score(i["score"])
            players.append(player)
    while editing:
        key = input(
            'For add new player enter N\nchange age or score press C\nenter EXIT for exit ')
        if key == "exit":
            editing = False
        elif key == "n":
            player_name = input("Enter player name ")
            player_last_name = input("Enter player last name ")
            new_player = Player(player_name, player_last_name)
            value = input("Enter player result ")
            if value.isdigit():
                new_player.set_score(int(value))
            players.append(new_player)
            age = -1
            while not new_player.set_age(age):
                age = int(input("enter age"))
        elif key == "c":
            print("Players:")
            for n, i in enumerate(players):
                print(n + 1,i.name)
            num = int(input("Who will change? Enter numb "))
            value = input("Enter player result ")
            if value.isdigit():
                players[num - 1].set_score(int(value))

        else:
            print("you made mistake")

    with open("players.json", "w") as f:
        json.dump([p.get_dict_repr() for p in players], f, indent=4)


if __name__ == '__main__':
    main()
