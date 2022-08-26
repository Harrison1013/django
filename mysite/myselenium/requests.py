import requests


def post(url, request):
    return requests.post(url, json=request).json()


def get(url, request):
    return requests.get(url, json=request).json()
