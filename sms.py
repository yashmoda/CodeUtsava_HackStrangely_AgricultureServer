import requests


def send_sms(message, phone, sender='KNSEWA'):
    url = 'https://control.msg91.com/api/sendhttp.php?authkey=' + '196358AkpOgnMS05a74a71b'  + '&mobiles='
    url += str(phone)
    url += '&message=' + message
    url += '&sender=' + sender + '&route=4&country=91'
    print url
    print requests.request('GET', url)