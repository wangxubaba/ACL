#用户通过telnet连接到路由器的实现逻辑
from django.http import JsonResponse
from django.conf import settings
import telnetlib
import time
#用户通过传递地址、用户名、密码，使用telnet与远程路由进行连接，返回连接结果
def connect(tn,address,username,password):
    response = {}
    #tn = telnetlib.Telnet()
    try:
        tn.open(address)
    except:
        text = '{}网络连接失败'.format(address)
        response['code'] = 500
        response['msg'] = text
        return JsonResponse(response)

    # 等待login出现后输入用户名，最多等待10秒
    tn.read_until(b'Username: ', timeout=10)
    tn.write(username.encode('ascii') + b'\n')
    # 等待Password出现后输入用户名，最多等待10秒
    tn.read_until(b'Password: ', timeout=10)
    tn.write(password.encode('ascii') + b'\n')

    tn.write("en".encode('ascii') + b'\n')
    tn.read_until(b'Password: ', timeout=10)
    tn.write(password.encode('ascii') + b'\n')
    # 延时5秒再收取返回结果，给服务端足够响应时间
    time.sleep(5)
    result = tn.read_very_eager().decode('utf-8')
    if 'Login invalid' in result:  # Cisco交换登录失败提示语
        text = '{} 登录失败，用户名或密码错误'.format(address)
        print(text)
        response['code'] = 500
        response['msg'] = text
        return JsonResponse(response)
    else:
        text = '{} 登录成功'.format(address)
        print(text)
        response['code'] = 200
        response['msg'] = text
        return JsonResponse(response)
# 用户获取当前连接的路由器的telnet地址
def getAddress():
    return

# 执行某个命令
def execute(command,routerNum):
    response = {}
    if routerNum==0:
        settings.TND.write(command.encode()+b'\n')
        time.sleep(1)
        #获取命令结果
        result=settings.TND.read_very_eager().decode('utf-8')
        response['code'] = 200
        response['msg'] = '执行完成'
        response['data']=result
        return JsonResponse(response)
    if routerNum==1:

        settings.TNA.write(command.encode()+b'\n')
        if command.startswith('p'):
            time.sleep(15)
        else:
            time.sleep(1)
        #获取命令结果
        result=settings.TNA.read_eager().decode('utf-8')
        response['code'] = 200
        response['msg'] = '执行完成'
        response['data']=result
        return JsonResponse(response)
    if routerNum==2:
        settings.TNB.write(command.encode()+b'\n')
        time.sleep(1)
        #获取命令结果
        result=settings.TNB.read_very_eager().decode('utf-8')
        response['code'] = 200
        response['msg'] = '执行完成'
        response['data']=result
        return JsonResponse(response)
    if routerNum==3:
        settings.TNC.write(command.encode()+b'\n')
        time.sleep(1)
        #获取命令结果
        result=settings.TNC.read_very_eager().decode('utf-8')
        response['code'] = 200
        response['msg'] = '执行完成'
        response['data']=result
        return JsonResponse(response)