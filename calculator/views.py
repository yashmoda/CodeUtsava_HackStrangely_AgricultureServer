# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import jwt
import os
from django.http.response import JsonResponse
from django.shortcuts import render

# Create your views here.
from selenium import webdriver

import keys
from Register.models import UserData
from calculator.models import CropSpacingData, CropArrangementData


def seed_required(request):
    response_json = {'data':[]}
    try:
        print("--------------Outside GET-------------------------")
        if request.method == 'GET':
            print("-----------------Inside GET-----------------------")
            access_token = request.GET.get(keys.ACCESS_TOKEN)
            print(access_token)
            user = jwt.decode(access_token, keys.ACCESS_TOKEN_SECRET, algorithms=['HS256'])
            mobile = user[keys.ACCESS_TOKEN_ENCRYPTION]
            print(mobile)
            crop = request.GET.get(keys.CROP)
            bed_size = request.GET.get(keys.BED_SIZE)
            bed_lines = request.GET.get(keys.BED_LINES)
            print(crop)
            print(bed_size)
            print(bed_lines)
            try:
                spacing_instance = CropSpacingData.objects.get(crop=crop)
                spacing = spacing_instance.spacing
                print(spacing)
            except Exception as e:
                print(str(e))
                response_json[keys.SUCCESS] = False
                response_json[keys.MESSAGE] = "Crop not found."
                return JsonResponse(response_json)
            driver = webdriver.Chrome('/home/yash/Downloads/chromedriver')
            driver.get('http://www.shamrockseed.com/Links/seeds_per.html')
            elem = driver.find_element_by_id('input_3')
            elem.send_keys(bed_size)
            elem = driver.find_element_by_id('input_4')
            elem.send_keys(spacing)
            elem = driver.find_element_by_id('input_5')
            elem.send_keys(bed_lines)
            elem = driver.find_element_by_id('input_1')
            seeds = elem.get_attribute('value')

            driver.close()
            print(seeds)
            try:
                user_instance = UserData.objects.get(mobile=mobile)
                crop_arrangement_instance = CropArrangementData.objects.create(user=user_instance,
                                                                               crop_spacing=spacing_instance,
                                                                               bed_size=bed_size,
                                                                               bed_lines=bed_lines,
                                                                               seeds=seeds)
                temp_json = {}
                temp_json[keys.SPACING] = str(spacing) 
                temp_json[keys.SEEDS] = str(int(float(seeds)))
                response_json['data'].append(temp_json)
                response_json[keys.SUCCESS] = True
                response_json[keys.MESSAGE] = "The data has been shown."
                print(str(response_json))
                return JsonResponse(response_json)
            except Exception as e:
                print(str(e))
                response_json[keys.SUCCESS] = False
                response_json[keys.MESSAGE] = "User does not exist."
                print(str(response_json))
                return JsonResponse(response_json)
    except Exception as e:
        print(str(e))
        response_json[keys.SUCCESS] = False
        response_json[keys.MESSAGE] = "Please try again later."
        print(str(response_json))
        return JsonResponse(response_json)