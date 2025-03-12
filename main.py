import os
from urllib.parse import urlparse
from dotenv import load_dotenv

import requests


def shorten_link(token, user_input):
    payload = {"access_token": token, "v": 5.199, "url": user_input}
    response = requests.get(
        "https://api.vk.ru/method/utils.getShortLink", params=payload
    )
    response.raise_for_status()
    error_msg = response.json().get("error")
    if error_msg:
        raise requests.exceptions.HTTPError(error_msg)
    short_link = response.json()["response"]["short_url"]
    return short_link


def count_clicks(token, short_link):
    key = urlparse(short_link).path.strip("/")
    payload = {
        "access_token": token,
        "v": 5.199,
        "key": key,
        "interval": "forever"
    }
    response = requests.get(
        "https://api.vk.ru/method/utils.getLinkStats", params=payload
    )
    response.raise_for_status()
    error_msg = response.json().get("error")
    if error_msg:
        raise requests.exceptions.HTTPError(error_msg)
    clicks_count = response.json()["response"]["stats"][0].get("views")
    return clicks_count


def is_shorten_link(token, user_input):
    key = urlparse(user_input).path.strip("/")
    payload = {
        "access_token": token,
        "v": 5.199,
        "key": key,
        "interval": "forever"
    }
    response = requests.get(
        "https://api.vk.ru/method/utils.getLinkStats", params=payload
    )
    response.raise_for_status()
    return "error" not in response.json()


def main():
    load_dotenv()
    token = os.environ["VK_TOKEN"]
    user_input = input()

    try:
        if is_shorten_link(token, user_input):
            clicks_count = count_clicks(token, short_link=user_input)
            print("Количество переходов: ", clicks_count)
        else:
            short_link = shorten_link(token, user_input)
            print("Сокращенная ссылка: ", short_link)
    except requests.exceptions.HTTPError as error:
        print(f"ошибка api {error}")


if __name__ == "__main__":
    main()
