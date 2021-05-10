import requests
import json

api = "https://pokeapi.co/api/v2/pokemon/"

# pokemon_request = input(str("What pokemon are you looking for? "))
pokemon_request = "ditto"


url = requests.get(api + pokemon_request)
pokemon = json.loads(url.text)


# Pokemon name
def get_pokemon_name():
    pokemon_name = pokemon["name"]
    print("Pokemon Name:")
    print(pokemon_name.title())

# Pokemon abilities
def get_abilities():
    abilities = []
    abilities_list = pokemon["abilities"][:]
    print("\nAbilities:")
    for ability in abilities_list:
        ability_name = ability['ability']['name']
        print(ability_name.title())
        abilities.append(ability)

# Pokemon moves
def get_moves():
    moves = pokemon["moves"][:]
    print(f"Total number of available moves: {len(moves)}")
    print("Moves:")
    for move in moves:
        move_name = move['move']["name"]
    #    move_learn_method = move['version_group_details'][:]['move_learn_method']['name']
        print(f"Move Name: {move_name.title()}")
    #    print(f"Move learnt by: {move_learn_method.title()}")


# get_pokemon_name()
# get_abilities()
# get_moves()
# save_file = open("ditto.json", "w")
# dump = json.dump(pokemon, save_file, indent= 6)
# save_file.close()#

version = pokemon["moves"][:]
