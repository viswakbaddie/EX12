import requests


def fetch_random_joke():
    url = 'https://api.chucknorris.io/jokes/random'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        joke_text = data['value']
        return joke_text
    else:
        return None


def main():
    print("Fetching a random Chuck Norris joke...\n")
    joke = fetch_random_joke()

    if joke:
        print("Chuck Norris Joke:")
        print(joke)
    else:
        print("Failed to fetch Chuck Norris joke. Please try again later.")


if __name__ == "__main__":
    main()
