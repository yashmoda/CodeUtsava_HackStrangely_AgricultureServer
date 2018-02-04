# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from random import randint

import jwt
from django.http.response import JsonResponse
from django.shortcuts import render

# Create your views here.
import keys
from Order.models import OrderData
from Products.models import ProductData
from Register.models import AddressData, UserData


def add_order(request):
    address_response = {keys.ADDRESS: []}
    response_json = {}
    try:
        if request.method == 'GET':
            access_token = request.GET.get(keys.ACCESS_TOKEN)
            print(access_token)
            user = jwt.decode(access_token, keys.ACCESS_TOKEN_SECRET, algorithms=['HS256'])
            mobile = user[keys.ACCESS_TOKEN_ENCRYPTION]
            print(mobile)
            user = UserData.objects.get(mobile=mobile)
            language = request.session.get(keys.LANGUAGE)
            if language == '1':
                for obj in AddressData.objects.filter(user=user):
                    temp_json = {}
                    temp_json['id'] = str(obj.id)
                    temp_json['name'] = str(obj.name_english)
                    temp_json['house_number'] = str(obj.house_number)
                    temp_json['locality'] = str(obj.locality_english)
                    temp_json['area'] = str(obj.area_english)
                    temp_json['city'] = str(obj.city_english)
                    temp_json['state'] = str(obj.state_english)
                    address_response[keys.ADDRESS].append(temp_json)
                print("Address in english")
                address_response[keys.SUCCESS] = True
                return JsonResponse(address_response)
            elif language == '2':
                for obj in AddressData.objects.filter(user=user):
                    temp_json = {}
                    temp_json['id'] = obj.id
                    temp_json['name'] = obj.name_hindi
                    temp_json['house_number'] = obj.house_number
                    temp_json['locality'] = obj.locality_hindi
                    temp_json['area'] = obj.area_hindi
                    temp_json['city'] = obj.city_hindi
                    temp_json['state'] = obj.state_hindi
                    address_response[keys.ADDRESS].append(temp_json)
                print("Address in english")
                address_response[keys.SUCCESS] = True
                return JsonResponse(address_response)
        if request.method == 'POST':
            access_token = request.POST.get(keys.ACCESS_TOKEN)
            print(access_token)
            user = jwt.decode(access_token, keys.ACCESS_TOKEN_SECRET, algorithms=['HS256'])
            mobile = user[keys.ACCESS_TOKEN_ENCRYPTION]
            print(mobile)
            user = UserData.objects.get(mobile=mobile)
            address_id = request.POST.get(keys.ADDRESS_ID)
            product_id = request.POST.get(keys.PRODUCT_ID)
            quantity = request.POST.get(keys.QUANTITY)
            address = AddressData.objects.get(id=address_id)
            product = ProductData.objects.get(id=product_id)
            amount = int(quantity)*int(product.price)
            order_id = randint(100000, 999999)
            order_obj = OrderData.objects.create(user=user, product=product, address=address,
                                                 quantity=quantity, amount=amount, order_id=order_id)

            response_json['order_id'] = order_obj.order_id
            response_json[keys.SUCCESS] = True
            response_json[keys.MESSAGE] = "Order Successfully created."
            print(str(response_json))
            return JsonResponse(response_json)
    except Exception as e:
        print (str(e))
        response_json[keys.SUCCESS] = False
        response_json[keys.MESSAGE] = "Please try again later."
        return JsonResponse(response_json)


def my_orders(request):
    response_json = {keys.ORDER: []}
    try:
        if request.method == 'GET':
            access_token = request.GET.get(keys.ACCESS_TOKEN)
            print(access_token)
            user = jwt.decode(access_token, keys.ACCESS_TOKEN_SECRET, algorithms=['HS256'])
            mobile = user[keys.ACCESS_TOKEN_ENCRYPTION]
            print(mobile)
            user_instance = UserData.objects.get(mobile=mobile)
            for obj in OrderData.objects.filter(user=user_instance):
                temp_json = {}
                temp_json['product_name'] = str(obj.product.name_eng)
                temp_json['quantity'] = str(obj.quantity)
                temp_json['amount'] = str(obj.amount)
                temp_json['order_id'] = str(obj.order_id)
                response_json[keys.ORDER].append(temp_json)
            print("Showing my orders.")
            response_json[keys.SUCCESS] = True
            response_json[keys.MESSAGE] = "All your orders have been listed."
            return JsonResponse(response_json)
    except Exception as e:
        print(str(e))
        response_json[keys.SUCCESS] = False
        response_json[keys.MESSAGE] = "Please try again later."
        return JsonResponse(response_json)


def delete_order(request):
    response_json = {}
    try:
        if request.method == 'POST':
            access_token = request.POST.get(keys.ACCESS_TOKEN)
            print(access_token)
            user = jwt.decode(access_token, keys.ACCESS_TOKEN_SECRET, algorithms=['HS256'])
            mobile = user[keys.ACCESS_TOKEN_ENCRYPTION]
            print(mobile)
            user_instance = UserData.objects.get(mobile=mobile)
            order_id = request.POST.get(keys.ORDER_ID)
            order_obj = OrderData.objects.get(user=user_instance, order_id=order_id)
            order_obj.delete()
            print("Successfully deleted.")
            response_json[keys.SUCCESS] = True
            response_json[keys.MESSAGE] = "Order Successfully deleted."
            return JsonResponse(response_json)
    except Exception as e:
        print(str(e))
        response_json[keys.SUCCESS] = False
        response_json[keys.MESSAGE] = "Please try again later."
        return JsonResponse(response_json)
