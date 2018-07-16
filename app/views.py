from django.shortcuts import render
import json, ast
# Create your views here.
from django.shortcuts import render, HttpResponse
import requests
from birdy.twitter import UserClient


client = UserClient('TlE56fey9n1McJDevlQDzHTgT',
                   'hLgCCzGz4SAWNhKRQHnnD3wc5ulQ9LMcM7apm9l84FBemXII21',
                    '17506920-4pvKThAPOPW6MUHNWGXO8QRCf6Hp17tq0cz9rE40f',
                    'cfnQAK4yBDsgiaIlpIavRb9BbdudbAqzZ8fvWVx9W5PGf')

# Create your views here.

def index(request):
    return HttpResponse('Hello World!')


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

def profile(request):
    jsonList = []
    req = requests.get('https://api.github.com/users/DrkSephy')
    jsonList.append(json.loads(req.content))
    parsedData = []
    userData = {}
    for data in jsonList:
        userData['name'] = data['name']
        userData['blog'] = data['blog']
        userData['email'] = data['email']
        userData['public_gists'] = data['public_gists']
        userData['public_repos'] = data['public_repos']
        userData['avatar_url'] = data['avatar_url']
        userData['followers'] = data['followers']
        userData['following'] = data['following']
        parsedData.append(userData)
    return HttpResponse(parsedData)