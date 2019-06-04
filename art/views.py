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


def data_context(url):
    res = requests.get(url)
    res_json = res.json()
    current_page = res_json['current_page']
    start_loop = current_page
    stop_loop = current_page + 3
    revers_step = current_page - 2

    pprint.pprint(res_json['updates'])

    context = {
        "data": res_json['updates'],
        "current_page": current_page,
        "loop_pagination": range(start_loop, stop_loop),
        "reverse_loop": range(start_loop),
        "revers_step": revers_step,
        "title": "Sinema"
    }
    return context


def index(request):
    url = f"http://moonwalk.cc/api/movies_updates.json?api_token={token}"

    context = data_context(url)
    return render(request, "art/index.html", context)


def serials(request):
    url = f"http://moonwalk.cc/api/serials_updates.json?api_token={token}"

    context = data_context(url)
    return render(request, "art/serials.html", context)

def page_serials(request, id):
    url = f"http://moonwalk.cc/api/serials_updates.json?api_token={token}&page={id}"
    context = data_context(url)
    return render(request, "art/serials.html", context)

def page(request, id):
    url = f"http://moonwalk.cc/api/movies_updates.json?api_token={token}&page={id}"
    context = data_context(url)
    return render(request, "art/index.html", context)


def search(request, page):
    if request.method == "GET":
        url = f"http://moonwalk.cc/api/videos.json?title={request.GET['q']}&api_token={token}"
        res = requests.get(url)
        res_json = res.json()
        # results = res_json['results']
        # total_pages = res_json['total_pages']
        # revers_step = res_json["page"] - 2

        # pprint.pprint(res_json)


        context = {
            "title": request.GET['q'],
            "query": request.GET['q'],
            "data":  res_json,
            # "reverse_loop": range(res_json["page"]),
            # "revers_step": revers_step,
            # "pages": range(res_json["page"], res_json["page"]+3),
            # 'total_pages': total_pages
        }
    return render(request, "art/search.html", context)


def video(request):
    if request.method == "GET":
        id = request.GET['title']
        url = f"http://moonwalk.cc/api/videos.json?kinopoisk_id={id}&api_token={token}"
        res = requests.get(url)
        res_json = res.json()

        title = res_json[0].get('title_ru')
        title_en = res_json[0].get('title_en')

        if res_json[0].get('material_data'):
            material_data = res_json[0].get('material_data')
        else:
            material_data = res_json[1].get('material_data')

        description = material_data['description']
        poster = material_data['poster']
        raite = material_data['imdb_rating']

        # pprint.pprint(res_json)

        context = {
            "title": title,
            "description": description,
            "material_data": material_data,
            "title_en": title_en,
            "poster": poster,
            "raite": raite,
            "query": request.GET['title']
        }
    return render(request, "art/video.html", context)
