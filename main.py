import requests, os
from dotenv import load_dotenv

load_dotenv()

thread_ids = list(map(int, os.getenv("THREAD_IDS").split(",")))
token = os.getenv("TOKEN")



url = "https://prod-api.lolz.live/threads/%thread_id%/bump"

headers = {
    "accept": "application/json",
    "authorization": f"Bearer {token}"
}


def main():
    for thread_id in thread_ids:
        response = requests.post(url.replace("%thread_id%", str(thread_id)), headers=headers)
        print(response.text)


if __name__ == "__main__":
    main()

