import requests
from flask import abort
from config import API_KEY


def parse_json(res):
    try:
        data = res.json()
    except (TypeError, AttributeError):  # usually would log here but probably not necessary for this purpose
        abort(502, "Received a response for URL data but unable to parse from request.")
    return data


def get_all_links_data():
    url = "https://api.rebrandly.com/v1/links"
    querystring = {"orderBy": "createdAt", "orderDir": "desc", "limit": "25"}
    headers = {'apikey': API_KEY}
    res = requests.request("GET", url, headers=headers, params=querystring)
    if not res:
        abort(502, "Error during request to retrieve data for URL; no data returned. Please try again.")
    data = parse_json(res)
    return data


def create_new_short_url(long_url):
    url = "https://api.rebrandly.com/v1/links"
    headers = {'Content-Type': 'application/json',
               'apikey': API_KEY}
    payload = {
        "destination": long_url
    }
    res = requests.request("POST", url, json=payload, headers=headers)
    if not res:
        abort(502, "Error during request to retrieve data for URL; no data returned. Please try again.")
    data = parse_json(res)
    short_url = data.get('shortUrl')
    if not short_url:
        abort(502, "No Short URL returned. Invalid response from data source.")
    return short_url

