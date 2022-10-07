from flask import Flask, request
import requests

from main import API

def reply():
    data = request.get_json()
    message=data['message']
    nickname=data['sender']['nickname']
    a="@%s %s" %(nickname,message)
    API.send(a)
    return "OK"
