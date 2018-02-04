# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http.response import JsonResponse
from django.shortcuts import render
import urllib2
# Create your views here.
import keys


def show_news(request):
    response_json = {keys.NEWS: []}
    try:
        if request.method == 'GET':
            news_url = 'http://eventregistry.org/json/article?query=%7B%22%24query%22%3A%7B%22%24and%22%3A%5B%7B%22conceptUri%22%3A%7B%22%24and%22%3A%5B%22http%3A%2F%2Fen.wikipedia.org%2Fwiki%2FAgriculture%22%5D%7D%7D%2C%7B%22categoryUri%22%3A%7B%22%24and%22%3A%5B%22dmoz%2FBusiness%2FAgriculture_and_Forestry%2FField_Crops%22%2C%22dmoz%2FScience%2FAgriculture%22%5D%7D%7D%2C%7B%22%24or%22%3A%5B%7B%22sourceUri%22%3A%22timesofindia.indiatimes.com%22%7D%2C%7B%22sourceUri%22%3A%22thehindu.com%22%7D%2C%7B%22sourceUri%22%3A%22bhaskar.com%22%7D%2C%7B%22sourceUri%22%3A%22economictimes.indiatimes.com%22%7D%2C%7B%22sourceUri%22%3A%22indianexpress.com%22%7D%2C%7B%22sourceUri%22%3A%22in.reuters.com%22%7D%2C%7B%22sourceUri%22%3A%22dnaindia.com%22%7D%5D%7D%2C%7B%22lang%22%3A%22eng%22%7D%5D%7D%7D&action=getArticles&resultType=articles&articlesSortBy=rel&articlesCount=10&articlesArticleBodyLen=-1&apiKey=1d149793-9d64-4ebe-bd70-9d82cc8126aa&callback=JSON_CALLBACK'
            response_json[keys.NEWS] = urllib2.urlopen(news_url).read()
            response_json[keys.SUCCESS] = True
            response_json[keys.MESSAGE] = "All news shown."
            return JsonResponse(response_json)
    except Exception as e:
        print(str(e))
        response_json[keys.SUCCESS] = False
        response_json[keys.MESSAGE] = "Please try again later."
        return JsonResponse(response_json)
