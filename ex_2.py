# I did not want to add my payment details to a weather service
# just for this single use, therefore I created a similar program,
# but using a free api tvmaze

import requests

while True:

    ans = input("Type a show that you are interested in or q to quit >> ").lower()

    if ans == 'q':
        break

    try:
        request = requests.get(f"https://api.tvmaze.com/singlesearch/shows?q={ans}")

        show = request.json()
        print(f"\nShow name: {show['name']}\n"
              f"Language: {show['language']}\n"
              f"Genres: {', '.join(show['genres'])}\n"
              f"Premiered: {show['premiered']}\n"
              f"Status: {show['status']}\n"
              f"Rating: {show['rating']['average']}")

        seasons = requests.get(f"https://api.tvmaze.com/shows/{show['id']}/seasons").json()
        print(f"Number of seasons: {len(seasons)}")

        episodes = requests.get(f"https://api.tvmaze.com/shows/{show['id']}/episodes").json()
        print(f"Number of episodes: {len(episodes)}\n")

    except Exception as e:
        print(e)