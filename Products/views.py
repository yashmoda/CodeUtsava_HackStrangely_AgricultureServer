# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import jwt
from django.http.response import JsonResponse
from django.shortcuts import render

# Create your views here.
import keys
from Products.models import ProductTypeData, ProductData, ProductImage


def all_product_type(request):
    response_json = {'data' : []}
    try:
        if request.method == 'GET':
            # access_token = request.GET.get(keys.ACCESS_TOKEN)
            language = request.GET.get(keys.LANGUAGE)
            request.session[keys.LANGUAGE] = language
            print(request.session.get(keys.LANGUAGE))
            # print(access_token)
            # user = jwt.decode(access_token, keys.ACCESS_TOKEN_SECRET, algorithms=['HS256'])
            # mobile = user[keys.ACCESS_TOKEN_ENCRYPTION]
            # print(mobile)
            print(language)
            if language == '1':
                for obj in ProductTypeData.objects.all():
                    temp_json = {}
                    temp_json[keys.PRODUCT_TYPE] = str(obj.product_type_eng)
                    temp_json[keys.IMAGE] = request.scheme + "://" + request.get_host() + '/' + str(obj.image)
                    response_json['data'].append(temp_json)
            elif language == '2':
                for obj in ProductTypeData.objects.all():
                    temp_json = {}
                    temp_json[keys.PRODUCT_TYPE] = obj.product_type_hi
                    temp_json[keys.IMAGE] = request.scheme + "://" + request.get_host() + '/' + str(obj.image)
                    response_json['data'].append(temp_json)
            print("All product type got")
            response_json[keys.SUCCESS] = True
            response_json[keys.MESSAGE] = "All the product types have been listed."
            print(str(response_json))
            return JsonResponse(response_json)
    except Exception as e:
        print("Exception while listing all product types.")
        print(str(e))
        response_json[keys.SUCCESS] = False
        response_json[keys.MESSAGE] = "Please try again later."
        return JsonResponse(response_json)


def products_type(request):
    response_json = {'get_products':[]}
    try:
        if request.method == 'GET':
            access_token = request.GET.get(keys.ACCESS_TOKEN)
            print(access_token)
            user = jwt.decode(access_token, keys.ACCESS_TOKEN_SECRET, algorithms=['HS256'])
            mobile = user[keys.ACCESS_TOKEN_ENCRYPTION]
            print(mobile)
            product_type = request.GET.get(keys.PRODUCT_TYPE)
            print(product_type)
            # language = request.session.get(keys.LANGUAGE)
            language = '1'
            print(language)
            if language == '1':
                try:
                    product_type_obj = ProductTypeData.objects.get(product_type_eng=product_type)
                except Exception as e:
                    print("Exception while getting Product type")
                    print (str(e))
                    response_json[keys.SUCCESS] = False
                    response_json[keys.keys.MESSAGE] = "Product type does not exist."
                    return JsonResponse(response_json)
                try:
                    product_obj_list = ProductData.objects.filter(product_type=product_type_obj)
                    for obj in product_obj_list:
                        temp_json = {}
                        temp_json['product_id'] = str(obj.id)
                        temp_json['product_name'] = str(obj.name_eng)
                        temp_json['product_image'] = request.scheme + "://" + request.get_host() + '/' + str(obj.image)
                        temp_json['product_price'] = str(obj.price)
                        response_json['get_products'].append(temp_json)
                    print("Products found.")
                    response_json[keys.SUCCESS] = True
                    response_json[keys.MESSAGE] = "All the products have been listed."
                    print(str(response_json))
                    return JsonResponse(response_json)
                except Exception as e:
                    print(str(e))
                    response_json[keys.SUCCESS] = False
                    response_json[keys.MESSAGE] = "Please try again later."
                    print(str(response_json))
                    return JsonResponse(response_json)
            elif language == '2':
                try:
                    product_type_obj = ProductTypeData.objects.get(product_type_hi=product_type)
                except Exception as e:
                    print("Exception while getting Product type")
                    print (str(e))
                    response_json[keys.SUCCESS] = False
                    response_json[keys.keys.MESSAGE] = "Product type does not exist."
                    return JsonResponse(response_json)
                try:
                    product_obj_list = ProductData.objects.filter(product_type=product_type_obj)
                    for obj in product_obj_list:
                        temp_json = {}
                        temp_json['product_id'] = str(obj.id)
                        temp_json['product_name'] = obj.name_hindi
                        temp_json['product_image'] = request.scheme + "://" + request.get_host() + '/' + str(obj.image)
                        temp_json['product_price'] = str(obj.price)
                        response_json['get_products'].append(temp_json)
                    print("Products found.")
                    response_json[keys.SUCCESS] = True
                    response_json[keys.MESSAGE] = "All the products have been listed."
                    print(str(response_json))
                    return JsonResponse(response_json)
                except Exception as e:
                    print(str(e))
                    response_json[keys.SUCCESS] = False
                    response_json[keys.MESSAGE] = "Please try again later."
                    print(str(response_json))
                    return JsonResponse(response_json)
    except Exception as e:
        print (str(e))
        response_json[keys.SUCCESS] = False
        response_json[keys.MESSAGE] = "Please try again later."
        print(str(response_json))
        return JsonResponse(response_json)


def show_product_details(request):
    response_json = {keys.PRODUCTS : []}
    try:
        if request.method == 'GET':
            access_token = request.GET.get(keys.ACCESS_TOKEN)
            print(access_token)
            user = jwt.decode(access_token, keys.ACCESS_TOKEN_SECRET, algorithms=['HS256'])
            mobile = user[keys.ACCESS_TOKEN_ENCRYPTION]
            print(mobile)
            product_id = request.GET.get(keys.PRODUCT_ID)
            language = request.session.get(keys.LANGUAGE)
            # language = '1'
            if language == '1':
                try:
                    product_obj = ProductData.objects.get(id=product_id)
                    temp_json = {'name': str(product_obj.name_eng), 'price': str(product_obj.price),
                                 'key_features': str(product_obj.key_features_english),
                                 'description': str(product_obj.description_english),
                                 }
                    print("abc")
                    product_image = ProductImage.objects.filter(product=product_obj)
                    temp_json1 = {}
                    images = []
                    for img in product_image:
                        temp_json1[keys.IMAGE] = request.scheme + "://" + request.get_host() + '/' + str(img.image)
                        images.append(temp_json1[keys.IMAGE])
                    temp_json[keys.IMAGE] = images
                    response_json[keys.SUCCESS] = True
                    response_json[keys.MESSAGE] = "All the details of the product have been listed."
                    print(str(response_json))
                    return JsonResponse(response_json)
                except Exception as e:
                    print(str(e))
                    response_json[keys.SUCCESS] = False
                    response_json[keys.MESSAGE] = "Please try again later."
                    print str(response_json)
                    return JsonResponse(response_json)
            elif language == '2':
                try:
                    product_obj = ProductData.objects.get(id=product_id)
                    temp_json = {'name': product_obj.name_hindi, 'price': str(product_obj.price),
                                 'key_features': product_obj.key_features_hindi,
                                 'description': product_obj.description_hindi,
                                 }
                    product_image = ProductImage.objects.filter(product=product_obj)
                    temp_json1 = {}
                    images = []
                    for img in product_image:
                        temp_json1[keys.IMAGE] = request.scheme + "://" + request.get_host() + '/' + str(img.image)
                        images.append(temp_json1[keys.IMAGE])
                    temp_json[keys.IMAGE] = images
                    response_json[keys.SUCCESS] = True
                    response_json[keys.MESSAGE] = "All the details of the product have been listed."
                    print(str(response_json))
                    return JsonResponse(response_json)
                except Exception as e:
                    print(str(e))
                    response_json[keys.SUCCESS] = False
                    response_json[keys.MESSAGE] = "Please try again later."
                    print str(response_json)
                    return JsonResponse(response_json)
    except Exception as e:
        print(str(e))
        response_json[keys.SUCCESS] = False
        response_json[keys.MESSAGE] = "Please try again later."
        print(str(response_json))
        return JsonResponse(response_json)

