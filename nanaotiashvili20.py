import requests
import json

base_url = "https://rickandmortyapi.com/api/character/"

characters = []
response = requests.get("https://rickandmortyapi.com/api/character")
data = response.json()
characters.extend(data['results'])

character_episodes = {}

for character in characters:
    name = character['name']
    episode_urls = character['episode']
    
    episode_names = []
    for url in episode_urls:
        episode_data = requests.get(url).json()
        episode_names.append(episode_data['name'])
    
    character_episodes[name] = episode_names

with open("characters_episodes.json", "w") as json_file:
    json.dump(character_episodes, json_file, indent=4)

print("episode")
