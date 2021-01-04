# 该部分用于验证
from django.http import JsonResponse, HttpResponse
import Implementation.TelnetManager as tm
from django.conf import settings
# 根据number选择运行第几个脚本，根据routerN选择验证哪个路由：1是A，2是B，3是C
def executeScript(number, routerN):
    # 6.
    text= ""
    if number == 0:
        # 在routerA上进行ping：
        if routerN == 1:
            result = tm.execute("p 192.168.23.3", 1)
            if 'Success rate is 0 percent' in result:
               text = "routerA验证正确"
               print(text)
            else:
               text = "routerA验证失败"
               print(text)
            tm.execute("ex", 1)      
        # 在routerC上进行ping：
        if routerN == 3:
            result = tm.execute("p 192.168.12.1", 3)
            if 'Success rate is 0 percent' in result:
               text += "routerC验证失败"
               print(text)
            else:
               text += "routerC验证成功"
               print(text) 
            tm.execute("ex", 3) 
    # 8   
    elif number == 1:
        # 在routerA上进行ping：
        if routerN == 1: 
            result = tm.execute("p 192.168.23.3", 1)
            if 'Success rate is 0 percent' in result:
               text = "routerA验证失败"
               print(text)
            else:
               text = "routerA验证正确"
               print(text)
            tm.execute("ex", 1)      
        # 在routerC上进行ping：
        if routerN == 3:
            result = tm.execute("p 192.168.12.1", 3)
            if 'Success rate is 0 percent' in result:
               text += "routerC验证失败"
               print(text)
            else:
               text += "routerC验证成功"
               print(text) 
            tm.execute("ex", 3) 

    # 9
    elif number == 2:
        # 在routerA上进行ping：
        if routerN == 1: 
            result = tm.execute("p 192.168.23.3", 1)
            if 'Success rate is 0 percent' in result:
               text = "routerA验证成功"
               print(text)
            else:
               text = "routerA验证失败"
               print(text)
            #tm.execute("ex", 1)      
        # 在routerC上进行ping：
        if routerN == 3:
            result = tm.execute("p 192.168.12.1", 3)
            if 'Success rate is 0 percent' in result:
               text += "routerC验证失败"
               print(text)
            else:
               text += "routerC验证成功"
               print(text) 
            #tm.execute("ex", 3)          
    
    elif number == 3:
        # 在routerA上进行ping：
        if routerN == 1: 
            result = tm.execute("p 192.168.23.3", 1)

            # 重新连接A
            telnetresult = tm.connect(settings.TNA, "192.168.23.3", "dd", "CISCO")

            if 'Success rate is 0 percent' in result:
               text = "PING C 验证失败"
               print(text)
            else:
               text = "PING C 验证成功"   
               print(text)
           
            if '500' in telnetresult:
               text += "telnet Router C，因为超时（7s）被拒绝,验证正确"
               print(text)
            else :
               text+="telnet验证失败"
               print(text)
            tm.execute("ex", 1)      
        # 在routerC上进行ping：
        if routerN == 3:
            result = tm.execute("p 192.168.12.1", 3)
            tm.execute("ex", 3)

            # 重新连接A
            telnetresult = tm.connect(settings.TNA, "192.168.12.1", "dd", "CISCO")
            #tm.execute("ex", 1)
            #telnetresult=tm.execute("telnet 192.168.12.1",1)
            if 'Success rate is 0 percent' in result:
               text += "routerC验证失败"
               print(text)
            else:
               text += "routerC验证成功"
               print(text) 
            
            if '500' in telnetresult:
               text+= "telnet Router A,验证失败"
               print(text)
            else :
               text+="telnet验证成功"
               print(text)

 
    elif number == 4:
        if routerN == 1: 
            result = tm.execute("p 192.168.23.3", 1)
            if 'Success rate is 0 percent' in result:
               text = "PING C 验证成功"
               print(text)
            else:
               text = "PING C 验证失败"   
               print(text)
            tm.execute("ex", 1) 
    
    elif number == 5:
        if routerN == 1: 
            result = tm.execute("p 192.168.23.3", 1)
            if 'Success rate is 0 percent' in result:
               text = "PING C 验证失败"
               print(text)
            else:
               text = "PING C 验证成功"   
               print(text)
            tm.execute("ex", 1) 
        
    response = {'code': 200, 'msg': text}
    return response
