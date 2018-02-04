# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import jwt
from django.http.response import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from passlib.hash import pbkdf2_sha256

import keys
from OTP.views import send_otp
from Register.models import UserData, AddressData


@csrf_exempt
def register_user(request):
    response_json = {}
    try:
        if request.method == 'POST':
            name = request.POST.get(keys.NAME)
            contact = request.POST.get(keys.CONTACT)
            email = request.POST.get(keys.EMAIL)
            password = request.POST.get(keys.PASSWORD)
            print(name)
            print(contact)
            print(email)
            print(password)
            try:
                UserData.objects.get(mobile=contact, email=email)
                print("User already exists.")
                response_json[keys.SUCCESS] = False
                response_json[keys.MESSAGE] = "User already exists."
                return JsonResponse(response_json)
            except Exception as e:
                print("Creating User.")
                hash_pass = pbkdf2_sha256.hash(password)
                print (hash_pass)
                UserData.objects.create(name=name, mobile=contact, email=email, password=hash_pass)
                send_otp(contact)
                response_json[keys.SUCCESS] = True
                response_json[keys.MESSAGE] = "User created successfully."
                return JsonResponse(response_json)
    except Exception as e:
        print(str(e))
        response_json[keys.SUCCESS] = False
        response_json[keys.MESSAGE] = "Please try again later."
        return JsonResponse(response_json)


@csrf_exempt
def login(request):
    response_json = {}
    try:
        if request.method == 'POST':
            access_token = request.POST.get(keys.ACCESS_TOKEN)
            password = request.POST.get(keys.PASSWORD)
            user = jwt.decode(access_token, keys.ACCESS_TOKEN_SECRET, algorithms=['HS256'])
            mobile = user[keys.ACCESS_TOKEN_ENCRYPTION]
            print(mobile)
            try:
                user_obj = UserData.objects.get(mobile=mobile)
                user_password = user_obj.password
                hash_pass = pbkdf2_sha256.hash(password)
                if pbkdf2_sha256.verify(user_password, hash_pass):
                    print("Password correct")
                    response_json[keys.SUCCESS] = True
                    response_json[keys.MESSAGE] = "Successfully logged in."
                    return JsonResponse(response_json)
                else:
                    print("Password do not match")
                    response_json[keys.SUCCESS] = False
                    response_json[keys.MESSAGE] = "Incorrect Password."
                    return JsonResponse(response_json)
            except Exception as e:
                print(str(e))
                response_json[keys.SUCCESS] = False
                response_json[keys.MESSAGE] = "User does not exist."
                return JsonResponse(response_json)
    except Exception as e:
        print(str(e))
        response_json[keys.SUCCESS] = False
        response_json[keys.keys.MESSAGE] = "Please try again later."
        return JsonResponse(response_json)


@csrf_exempt
def set_language(request):
    response_json = {}
    if request.method == 'POST':
        language = request.POST.get(keys.language)
        request.session[keys.LANGUAGE] = language
        response_json[keys.SUCCESS] = True
        return JsonResponse(response_json)


@csrf_exempt
def add_address(request):
    response_json = {}
    try:
        if request.method == 'POST':
            access_token = request.POST.get(keys.ACCESS_TOKEN)
            user = jwt.decode(access_token, keys.ACCESS_TOKEN_SECRET, algorithms=['HS256'])
            mobile = user[keys.ACCESS_TOKEN_ENCRYPTION]
            print(mobile)
            name = request.POST.get(keys.NAME)
            house_number = request.POST.get(keys.HOUSE_NO)
            locality = request.POST.get(keys.LOCALITY)
            area = request.POST.get(keys.AREA)
            city = request.POST.get(keys.CITY)
            print(name)
            print(house_number)
            print(locality)
            print(area)
            print(city)
            language = request.session.get(keys.LANGUAGE)
            state = request.POST.get(keys.STATE)
            if language == '1':
                try:
                    user_instance = UserData.objects.get(mobile=mobile)
                    try:
                        address_instance = AddressData.objects.get(user=user_instance,
                                                                   name_english=name,
                                                                   house_number=house_number,
                                                                   locality_english=locality,
                                                                   area_english=area,
                                                                   city_english = city,
                                                                   state_english=state
                                                                   )
                        response_json[keys.SUCCESS] = False
                        response_json[keys.MESSAGE] = "Address already exists."
                        return JsonResponse(response_json)
                    except Exception as e:
                        print(str(e))
                        address_instance = AddressData.objects.create(user=user_instance,
                                                                      name_english=name,
                                                                      house_number=house_number,
                                                                      locality_english=locality,
                                                                      area_english=area,
                                                                      city_english=city,
                                                                      state_english=state
                                                                      )
                        response_json[keys.SUCCESS] = True
                        response_json[keys.MESSAGE] = "Address added successfully."
                        return JsonResponse(response_json)
                except Exception as e:
                    print(str(e))
                    response_json[keys.SUCCESS] = False
                    response_json[keys.MESSAGE] = "Invalid user."
                    return JsonResponse(response_json)
            elif language == '2':
                try:
                    user_instance = UserData.objects.get(mobile=mobile)
                    try:
                        address_instance = AddressData.objects.get(user=user_instance,
                                                                   name_hindi=name,
                                                                   house_number=house_number,
                                                                   locality_hindi=locality,
                                                                   area_hindi=area,
                                                                   city_hindi = city,
                                                                   state_hindi=state
                                                                   )
                        response_json[keys.SUCCESS] = False
                        response_json[keys.MESSAGE] = "Address already exists."
                        return JsonResponse(response_json)
                    except Exception as e:
                        print(str(e))
                        address_instance = AddressData.objects.create(user=user_instance,
                                                                      name_hindi=name,
                                                                      house_number=house_number,
                                                                      locality_hindi=locality,
                                                                      area_hindi=area,
                                                                      city_hindi=city,
                                                                      state_hindi=state
                                                                      )
                        response_json[keys.SUCCESS] = True
                        response_json[keys.MESSAGE] = "Address added successfully."
                        return JsonResponse(response_json)
                except Exception as e:
                    print(str(e))
                    response_json[keys.SUCCESS] = False
                    response_json[keys.MESSAGE] = "Invalid user."
                    return JsonResponse(response_json)
    except Exception as e:
        print(str(e))
        response_json[keys.SUCCESS] = False
        response_json[keys.MESSAGE] = "Please try again later."
        return JsonResponse(response_json)


def all_address(request):
    response_json = {keys.ADDRESS: []}
    try:
        if request.method == 'GET':
            access_token = request.GET.get(keys.ACCESS_TOKEN)
            user = jwt.decode(access_token, keys.ACCESS_TOKEN_SECRET, algorithms=['HS256'])
            mobile = user[keys.ACCESS_TOKEN_ENCRYPTION]
            print(mobile)
            language = request.session.get(keys.LANGUAGE)
            if language == '1':
                try:
                    user_instance = UserData.objects.get(mobile=mobile)
                    address_obj = AddressData.objects.filter(user=user_instance)
                    for obj in address_obj:
                        temp_json = {}
                        temp_json['id'] = str(obj.id)
                        temp_json['name'] = str(obj.name_english)
                        temp_json['house_no'] = str(obj.house_number)
                        temp_json['locality'] = str(obj.locality_english)
                        temp_json['area'] = str(obj.area_english)
                        temp_json['city'] = str(obj.city_english)
                        temp_json['state'] = str(obj.state_english)
                        response_json[keys.ADDRESS].append(temp_json)
                    print ("Appending address done.")
                    response_json[keys.SUCCESS] = True
                    response_json[keys.MESSAGE] = "All address shown."
                    return JsonResponse(response_json)
                except Exception as e:
                    print(str(e))
                    response_json[keys.SUCCESS] = False
                    response_json[keys.MESSAGE] = "The address could be shown."
                    return JsonResponse(response_json)
            elif language == '2':
                try:
                    user_instance = UserData.objects.get(mobile=mobile)
                    address_obj = AddressData.objects.filter(user=user_instance)
                    for obj in address_obj:
                        temp_json = {}
                        temp_json['id'] = obj.id
                        temp_json['name'] = obj.name_hindi
                        temp_json['house_no'] = obj.house_number
                        temp_json['locality'] = obj.locality_hindi
                        temp_json['area'] = obj.area_hindi
                        temp_json['city'] = obj.city_hindi
                        temp_json['state'] = obj.state_hindi
                        response_json[keys.ADDRESS].append(temp_json)
                    print ("Appending address done.")
                    response_json[keys.SUCCESS] = True
                    response_json[keys.MESSAGE] = "All address shown."
                    return JsonResponse(response_json)
                except Exception as e:
                    print(str(e))
                    response_json[keys.SUCCESS] = False
                    response_json[keys.MESSAGE] = "The address could be shown."
                    return JsonResponse(response_json)
    except Exception as e:
        print(str(e))
        response_json[keys.SUCCESS] = False
        response_json[keys.MESSAGE] = "Please try again later."
        return JsonResponse(response_json)


def delete_address(request):
    response_json = {}
    try:
        if request.method == 'GET':
            access_token = request.GET.get(keys.ACCESS_TOKEN)
            user = jwt.decode(access_token, keys.ACCESS_TOKEN_SECRET, algorithms=['HS256'])
            mobile = user[keys.ACCESS_TOKEN_ENCRYPTION]
            address_id = request.GET.get(keys.ADDRESS_ID)
            print(mobile)
            try:
                user_instance = UserData.objects.get(mobile=mobile)
                address_instance = AddressData.objects.get(user=user_instance, id=address_id)
                address_instance.delete()
                response_json[keys.SUCCESS] = True
                response_json[keys.MESSAGE] = "Address deleted."
                return JsonResponse(response_json)
            except Exception as e:
                print(str(e))
                response_json[keys.SUCCESS] = False
                response_json[keys.MESSAGE] = "The address could be deleted."
                return JsonResponse(response_json)

    except Exception as e:
        print(str(e))
        response_json[keys.SUCCESS] = False
        response_json[keys.MESSAGE] = "Please try again later."
        return JsonResponse(response_json)
