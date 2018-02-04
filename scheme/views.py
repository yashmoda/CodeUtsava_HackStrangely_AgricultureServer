# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import jwt
from django.http.response import JsonResponse
from django.shortcuts import render

# Create your views here.
import keys
from scheme.models import SchemeData


def show_all_scheme(request):
    response_json = {keys.SCHEME: []}
    try:
        if request.method == 'GET':
            # access_token = str(request.GET.get(keys.ACCESS_TOKEN))
            # print(access_token)
            # user = jwt.decode(str(access_token), keys.ACCESS_TOKEN_SECRET, algorithms=['HS256'])
            # mobile = user[keys.ACCESS_TOKEN_ENCRYPTION]
            # print(mobile)
            for obj in SchemeData.objects.all():
                temp_json = {}
                temp_json['id'] = str(obj.id)
                temp_json['scheme'] = str(obj.scheme)
                temp_json['ministry'] = str(obj.ministry)
                temp_json['objective'] = str(obj.objective)
                response_json[keys.SCHEME].append(temp_json)
            print("Scheme")
            response_json[keys.SUCCESS] = True
            response_json[keys.MESSAGE] = "All data shown."
            return JsonResponse(response_json)
    except Exception as e:
        print(str(e))
        response_json[keys.SUCCESS] = False
        response_json[keys.MESSAGE] = "Please try again later."
        print(str(response_json))
        return JsonResponse(response_json)