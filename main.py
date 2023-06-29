import requests
def isBulba(content):
    return "bulbasaur".encode() is content
def isPikachu(content):
    return "pikachu".encode() is content
def isCharmander(content):
    return "charmander".encode() is content
def isGrassType(content):
    return "grass".encode() is content
def isPoisonType(content):
    return "poison".encode() is content

url = "https://pokeapi.co/api/v2/pokemon/"
pokemon = input("Enter a pokemon's name (lowercase only): ")
url += pokemon
url2 = "https://pokemon.fandom.com/wiki/"
url2 += pokemon
r = requests.get(url)
if r.status_code == 200:
    print(f"Wiki page for the pokemon is: {url2}")
else:
    print("this pokemon does not exist")

