from django.shortcuts import render
from django.http import JsonResponse
import json

def echo(requests):
    print(requests.method)
    r = requests.GET
    print(r)
    # dct = json.loads(r)
    dct = {'asd':'asdf'}
    return JsonResponse(r) 