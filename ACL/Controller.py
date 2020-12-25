from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.http import JsonResponse
from django.core import serializers
import json

@require_http_methods(["POST"])
def test_connection(request):
    body=json.loads(request.body)
    print(body['test'])
    response = {}
    try:
        books = ['Book1','Book2','Book3']
        #response['list'] = json.loads(serializers.serialize("json", books))
        response['list'] = json.dumps(books)
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1

    return JsonResponse(response)

# 用户通过telnet连接到路由器/交换机
# 使用TelnetConnect.py
@require_http_methods(["POST"])
def connect(request):
    response={}
    #具体获取参数逻辑自己编写
    #把实现逻辑写到Implementation
    return JsonResponse(response)

# 用户在完成前端页面配置之后，传递数据给execute方法，
# 该方法调用GenerateCommand.py讲前端传递的数据转化为可用的ACL命令
# 然后再嗲用ExecuteCommand.py把命令一条一条输进去
@require_http_methods(["POST"])
def execute(request):
    response={}
    # 具体获取参数逻辑自己编写
    # 把实现逻辑写到Implementation
    return JsonResponse(response)

# 打开之前保存的脚本文件，返回前端需要的显示参数
# 调用TransformFormat.py
@require_http_methods(["POST"])
def open(request):
    response={}
    # 具体获取参数逻辑自己编写
    # 把实现逻辑写到Implementation
    return JsonResponse(response)

# 保存当前脚本文件，将形成的文件保存下来（后端存/传到前端存）
# 调用TransformFormat.py
@require_http_methods(["POST"])
def save(request):
    response={}
    # 具体获取参数逻辑自己编写
    # 把实现逻辑写到Implementation
    return JsonResponse(response)

