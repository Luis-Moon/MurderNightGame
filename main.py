import os
import json
import numpy as np
from src.funcs.utils import join_path, load_json, clear, print_logo, dump_json

def get_player_data(id: int | str):
    player_data = load_json(join_path("src", "tables", "player_data.json"))
    for data in player_data.values():
        clear()
        print_logo()
        input(f"DADOS DO JOGADOR {data['Nome']}")
        for key, value in data.items():
            print(f"{key} : {value}\n")
        input("Quando acabar, aperte enter")

def randomize_player(players: list):
    player_data_path = join_path(join_path("src", "tables"), "player_data.json")
    player_data = load_json(player_data_path)
    already_used = [player for player, description in player_data.items() if "Nome" in description.keys()]
    if isinstance(players, str):
        players = [players]
    for player_name in players:
        while True:
            random_role = np.random.choice(list(player_data.keys()))
            if "Nome" not in player_data[random_role].keys():
                player_data[random_role]["Nome"] = player_name
                break
    dump_json(player_data_path, player_data)
    
def choose_killer_victim():
    players = load_json(join_path(join_path("src", "tables"), "player_data.json"))
    all_players = list(players.keys())
    while True:
        assassino = np.random.choice(all_players)
        all_players.pop(all_players.index(assassino))
        if "Nome" in players[assassino].keys():
            break
    while True:
        vitima = np.random.choice(all_players)
        all_players.pop(all_players.index(vitima))
        if "Nome" in players[vitima].keys():
            break
    return assassino, vitima

def reset_json():
    path = join_path(join_path("src", "tables"), "player_data.json")
    player_data = load_json(path)
    for player in player_data.values():
        if "Nome" not in player.keys():
            continue
        if player["Nome"] not in ["Luis", "Jess"]:
            player.__delitem__("Nome")
    dump_json(path,player_data)

if __name__ == "__main__":
    Jogadores = ["Rafael", "Jackie", "Matheus", "Debbie"]
    randomize_player(Jogadores)
    assas , vict = choose_killer_victim()

