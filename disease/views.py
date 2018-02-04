# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import jwt
from django.http.response import JsonResponse

# Create your views here.
import keys
from disease.models import DiseaseData


def show_disease(request):
    response_json = {keys.DISEASE: []}
    try:
        print("-------------------Outside Get-------------------------")
        if request.method == 'GET':
            print("--------------GET-----------------------")
            access_token = request.GET.get(keys.ACCESS_TOKEN)
            print(access_token)
            user = jwt.decode(access_token, keys.ACCESS_TOKEN_SECRET, algorithms=['HS256'])
            mobile = user[keys.ACCESS_TOKEN_ENCRYPTION]
            print(mobile)
            # language = request.session.get(keys.LANGUAGE)
            language = '1'
            if language == '1':
                print("1")
                for obj in DiseaseData.objects.all():
                    temp_json = {}
                    temp_json['name'] = str(obj.disease_name_english)
                    # temp_json['symptoms'] = str(obj.symptoms_english)
                    temp_json['prevention'] = str(obj.symptoms_english) + str(obj.prevention_english)
                    temp_json['image'] = request.scheme + "://" + request.get_host() + '/' + str(obj.image)
                    response_json[keys.DISEASE].append(temp_json)
                print("Disease")
                response_json[keys.SUCCESS] = True
                response_json[keys.MESSAGE] = "All diseases have been shown"
                print(str(response_json))
                return JsonResponse(response_json)
            elif language == '2':
                for obj in DiseaseData.objects.all():
                    temp_json = {}
                    temp_json['name'] = obj.disease_name_hindi
                    # temp_json['symptoms'] = obj.symptoms_hindi
                    temp_json['prevention'] = obj.symptoms_hindi + obj.prevention_hindi
                    temp_json['image'] = request.scheme + "://" + request.get_host() + '/' + str(obj.image)
                    response_json[keys.DISEASE].append(temp_json)
                print("Disease")
                response_json[keys.SUCCESS] = True
                response_json[keys.MESSAGE] = "All disease have been shown."
                return JsonResponse(response_json)
            else:
                response_json[keys.SUCCESS] = False
                return JsonResponse(response_json)
    except Exception as e:
        print(str(e))
        response_json[keys.SUCCESS] = False
        response_json[keys.MESSAGE] = "Please try again later."
        print(str(response_json))
        return JsonResponse(response_json)
