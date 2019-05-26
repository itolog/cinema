from django.shortcuts import render
import json
import os

import requests
import pprint

file = os.path.join('config.json')

print(file)

with open(file) as conf:
    secrets = json.load(conf)
    token = secrets["TOKEN_MOON"]
    token_imdb = secrets["TOKEN_IMDB"]


def index(request):
    url = f"http://moonwalk.cc/api/movies_updates.json?api_token={token}"
    res = requests.get(url)
    res_json = res.json()
    # pprint.pprint(res_json)
    print(len(res_json))
    # print("res", res_json)
    # print(res_json['updates'])
    context = {
        "data": res_json['updates'],
        "title": "Sinema"
    }
    return render(request, "art/index.html", context)


def page(request, id):
    url = f"http://moonwalk.cc/api/movies_updates.json?api_token={token}&page={id}"
    res = requests.get(url)
    res_json = res.json()
    context = {
        "data": res_json['updates'],
        "title": "Sinema"
    }
    return render(request, "art/index.html", context)


def search(request):
    if request.method == "GET":
        url = f"https://api.themoviedb.org/3/search/movie?api_key={token_imdb}&language=ru&query={request.GET['q']}"
        res = requests.get(url)
        res_json = res.json()
        pprint.pprint(res_json)
        context = {
            "title": request.GET['q'],
            "query": request.GET['q']
        }
    return render(request, "art/search.html", context)


def video(request):
    if request.method == "GET":
        context = {
            "title": request.GET['title'],
            "query": request.GET['title']
        }
    return render(request, "art/video.html", context)
