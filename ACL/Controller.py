from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.http import JsonResponse
from django.core import serializers
import json
import Implementation.ScriptManager as sm
import Implementation.TelnetManager as tm
import Implementation.ValidationManager as vm

from django.conf import settings

@require_http_methods(["POST"])
def test_connection(request):
    body = json.loads(request.body)
    print(body['test'])
    response = {}
    try:
        books = ['Book1', 'Book2', 'Book3']
        # response['list'] = json.loads(serializers.serialize("json", books))
        response['list'] = json.dumps(books)
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1

    return JsonResponse(response)


@require_http_methods(["POST"])
def connect(request):
    body = json.loads(request.body)
    connectData = body['connectData']
    address = connectData['address']
    username = connectData['username']
    password = connectData['password']

    print(connectData)
    if address== "192.168.0.2":
        return tm.connect(settings.TND,address,username,password)
    if address== "192.168.0.3":
        return tm.connect(settings.TNA,address,username,password)
    if address== "192.168.0.4":
        return tm.connect(settings.TNB,address,username,password)
    if address== "192.168.0.5":
        return tm.connect(settings.TNC,address,username,password)
    #具体获取参数逻辑自己编写
    #把实现逻辑写到Implementation
    #tm.connect()

@require_http_methods(["POST"])
def getCurrentAddress(request):
    response = {}
    # 具体获取参数逻辑自己编写
    # 把实现逻辑写到Implementation
    # tm.getAddress()
    return JsonResponse(response)


@require_http_methods(["POST"])
def executeScript(request):
    # 具体获取参数逻辑自己编写
    # 把实现逻辑写到Implementation
    # sm.executeScript()
    body = json.loads(request.body)
    id = body['id']
    return sm.executeScript(id)


@require_http_methods(["POST"])
def getScriptStatus(request):
    response = {}
    # 具体获取参数逻辑自己编写
    # 把实现逻辑写到Implementation
    # sm.getScriptStatus()
    return JsonResponse(response)


@require_http_methods(["POST"])
def executeValidation(request):
    response = {}
    # 具体获取参数逻辑自己编写
    # 把实现逻辑写到Implementation
    # vm.executeScript()
    return JsonResponse(response)


@require_http_methods(["POST"])
def getValidationStatus(request):
    response = {}
    # 具体获取参数逻辑自己编写
    # 把实现逻辑写到Implementation
    # sm.getScriptStatus()
    # vm.getScriptStatus()
    return JsonResponse(response)
