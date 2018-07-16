from django.shortcuts import render
import json, ast
from django.shortcuts import render, HttpResponse
import requests
from birdy.twitter import UserClient
import os

client = UserClient(os.getenv("CONSUMER_KEY"),
                    os.getenv("CONSUMER_SECRET"),
                    os.getenv("ACCESS_TOKEN"),
                    os.getenv("ACCESS_TOKEN_SECRET"))




def users(request):
    parsedData = []
    term = request.GET.get('q', None) or 'a'
    response = client.api.users.search.get(q=term)
    for data in response.data:
        userData = {}
        userData['id'] = data['id']
        userData['screen_name'] = data['screen_name']
        parsedData.append(userData)

    return HttpResponse(json.dumps(parsedData))

def statuses(request):
    parsedData = []
    screenName = request.GET.get('screenname', None) or 'a'
    response = client.api.statuses.user_timeline.get(screen_name=screenName)
    for data in response.data:
        statusData = {}
        statusData['id'] = data['id_str']
        statusData['text'] = data['text']
        parsedData.append(statusData)
    
    return HttpResponse(json.dumps(parsedData))