# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from random import randint

import jwt
from django.http.response import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt

import keys
from OTP.models import OTPData
from Register.models import UserData
from sms import send_sms


@csrf_exempt
def send_otp(contact):
    response_json = {}
    try:
        # contact = request.POST.get(keys.CONTACT)
        try:
            user_instance = UserData.objects.get(mobile=contact)
            otp = randint(1000, 9999)
            try:
                otp_instance = OTPData.objects.get(user=user_instance)
                otp_instance.otp = otp
                otp_instance.save()
            except Exception as e:
                otp_instance = OTPData.objects.create(user=user_instance, otp=otp)
            try:
                msg = "Your one time password is " + str(otp)
                print(msg)
                send_sms(msg, str(contact))
            except Exception as e:
                print(str(e))
                response_json[keys.SUCCESS] = False
                response_json[keys.MESSAGE] = "Otp could not be sent"
                return JsonResponse(response_json)
            response_json[keys.SUCCESS] = True
            response_json[keys.MESSAGE] = "Otp sent successfully."
            return JsonResponse(response_json)
        except Exception as e:
            print (str(e))
            response_json[keys.SUCCESS] = False
            response_json[keys.MESSAGE] = "Otp could not be sent."
            return JsonResponse(response_json)
    except Exception as e:
        print(str(e))
        response_json[keys.SUCCESS] = False
        response_json[keys.MESSAGE] = "Otp could not be sent"
        return JsonResponse(response_json)


@csrf_exempt
def verify_otp(request):
    response_json = {}
    if request.method == 'POST':
        try:
            contact = request.POST.get(keys.CONTACT)
            otp = request.POST.get(keys.OTP)
            print(contact)
            print(otp)
            user = UserData.objects.get(mobile=contact)
            otpobj = OTPData.objects.get(user=user)
            if otpobj.otp == int(otp):
                access_token = jwt.encode({keys.ACCESS_TOKEN_ENCRYPTION: str(contact)},
                                          keys.ACCESS_TOKEN_SECRET, algorithm='HS256')
                otpobj.save()
                print(str(access_token))
                response_json['access_token'] = str(access_token)
                print('Access Token Created')
                response_json[keys.SUCCESS] = True
                response_json[keys.MESSAGE] = "Successful"
            else:
                response_json[keys.SUCCESS] = False
                response_json[keys.MESSAGE] = "Invalid OTP"
        except Exception as e:
            print e
            response_json[keys.SUCCESS] = False
            response_json[keys.MESSAGE] = "Invalid Mobile Number"
        print 23456
        return JsonResponse(response_json)