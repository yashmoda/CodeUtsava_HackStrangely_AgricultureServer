# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from random import randint

import jwt
from django.http.response import JsonResponse

import keys
from Feedback.models import FeedbackData, ComplaintData
from Register.models import UserData
from sms import send_sms


def add_feedback(request):
    response_json = {}
    try:
        if request.method == 'POST':
            access_token = request.POST.get(keys.ACCESS_TOKEN)
            user = jwt.decode(access_token, keys.ACCESS_TOKEN_SECRET, algorithms=['HS256'])
            mobile = user[keys.ACCESS_TOKEN_ENCRYPTION]
            print(mobile)
            subject = request.POST.get(keys.SUBJECT)
            query = request.POST.get(keys.QUERY)
            print(subject)
            print(query)
            try:
                user_instance = UserData.objects.get(mobile=mobile)
                feedback = FeedbackData.objects.create(user=user_instance, subject=subject, query=query)
                response_json['id'] = feedback.id
                response_json[keys.SUCCESS] = True
                response_json[keys.MESSAGE] = "Thank you for your valuable feedback."
                return JsonResponse(response_json)
            except Exception as e:
                print(str(e))
                response_json[keys.SUCCESS] = False
                response_json[keys.MESSAGE] = "Feedback could not be received."
                return JsonResponse(response_json)
    except Exception as e:
        print(str(e))
        response_json[keys.SUCCESS] = False
        response_json[keys.MESSAGE] = "Please try again later."
        return JsonResponse(response_json)


def add_complaint(request):
    response_json = {}
    try:
        if request.method == 'POST':
            access_token = request.POST.get(keys.ACCESS_TOKEN)
            user = jwt.decode(access_token, keys.ACCESS_TOKEN_SECRET, algorithms=['HS256'])
            mobile = user[keys.ACCESS_TOKEN_ENCRYPTION]
            print(mobile)
            subject = request.POST.get(keys.SUBJECT)
            query = request.POST.get(keys.QUERY)
            print(subject)
            print(query)
            try:
                user_instance = UserData.objects.get(mobile=mobile)
            except Exception as e:
                print(str(e))
                response_json[keys.SUCCESS] = False
                response_json[keys.MESSAGE] = "User does not exist."
                return JsonResponse(response_json)
            try:
                ticket_no = randint(10000000, 99999999)
                msg = "Your complaint has been recorded. Your complaint ticket number is " + str(ticket_no)
                send_sms(msg, str(mobile))
                ComplaintData.objects.create(user=user_instance, subject=subject, query=query, ticket_no=ticket_no)
                response_json[keys.SUCCESS] = True
                response_json[keys.MESSAGE] = "Complaint registered successfully."
                return JsonResponse(response_json)
            except Exception as e:
                print(str(e))
                response_json[keys.SUCCESS] = False
                response_json[keys.MESSAGE] = "Complaint could not be registered."
                return JsonResponse(response_json)
    except Exception as e:
        print(str(e))
        response_json[keys.SUCCESS] = False
        response_json[keys.MESSAGE] = "Please try again later."
        return JsonResponse(response_json)
