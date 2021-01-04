from django.http import JsonResponse, HttpResponse
import Implementation.TelnetManager as tm
import Implementation.ValidationManager as vm
from django.conf import settings
# 该部分用于执行已有配置脚本

# 根据number选择运行第几个脚本
def executeScript(number):
    result = "success\n"
    if number == 0:
        # 重新连接B
        tm.connect(settings.TNB, "192.168.0.4", "dd", "CISCO")
        # 6.RouterB
        tm.execute("conf t", 2)
        tm.execute("access-list 100 deny ospf any any", 2)
        tm.execute("access-list 100 permit ip any any", 2)
        tm.execute("int s2/0", 2)
        tm.execute("ip access-group 100 in", 2)
        tm.execute("ex", 2)
        tm.execute("router ospf 1", 2)
        tm.execute("network 192.168.12.0 0.0.0.255 a 0", 2)
        tm.execute("network 192.168.23.0 0.0.0.255 a 0", 2)
        tm.execute("network 192.168.0.0 0.0.0.255 a 0", 2)
        tm.execute("end", 2)
        tm.execute("ex", 2)
        # 6.RouterA
        # 重新连接A
        tm.connect(settings.TNA, "192.168.0.3", "dd", "CISCO")
        tm.execute("conf t", 1)
        tm.execute("router ospf 1", 1)
        tm.execute("network 192.168.12.0 0.0.0.255 a 0", 1)
        tm.execute("network 192.168.0.0 0.0.0.255 a 0", 1)
        tm.execute("end", 1)
        tm.execute("ex", 1)
        # 6.RouterC
        # 重新连接C
        tm.connect(settings.TNC, "192.168.0.5", "dd", "CISCO")
        tm.execute("conf t", 3)
        tm.execute("router ospf 1", 3)
        tm.execute("network 192.168.12.0 0.0.0.255 a 0", 3)
        tm.execute("network 192.168.0.0 0.0.0.255 a 0", 3)
        tm.execute("end", 3)
        tm.execute("ex", 3)


    elif number == 1:
        #重新连接B
        tm.connect(settings.TNB,"192.168.0.4","dd","CISCO")
        # 7.
        tm.execute("conf t", 2)
        tm.execute("int s2/0", 2)
        tm.execute("no ip access-group 100 in", 2)
        tm.execute("end", 2)
        tm.execute("ex", 2)
        #tm.execute("conf t", 2)
        #重新连接A
        tm.connect(settings.TNA, "192.168.0.3", "dd", "CISCO")
        #tm.execute("ping 192.168.0.3", 1)
        response = vm.executeScript(1, 1)
        result += response['msg']+"\n"
        # 重新连接C
        tm.connect(settings.TNC, "192.168.0.5", "dd", "CISCO")
        response = vm.executeScript(1, 3)
        result += response['msg']+"\n"

    elif number == 2:
        # 9.
        # 重新连接B
        tm.connect(settings.TNB, "192.168.0.4", "dd", "CISCO")
        tm.execute("en", 2)
        tm.execute("conf t", 2)
        tm.execute("access-list 101 permit icmp any any echo-reply", 2)
        tm.execute("en", 2)
        tm.execute("int s2/0", 2)
        tm.execute("ip access-group 101 in", 2)
        tm.execute("end", 2)
        tm.execute("ex", 2)
        # 重新连接A
        tm.connect(settings.TNA, "192.168.0.3", "dd", "CISCO")
        response = vm.executeScript(2, 1);
        result += response['msg'] + "\n"
        # 重新连接C
        tm.connect(settings.TNC, "192.168.0.5", "dd", "CISCO")
        response = vm.executeScript(2, 3);
        result += response['msg'] + "\n"
    elif number == 3:
        # 10.恢复RouterB的ACL配置
        # 重新连接B
        tm.connect(settings.TNB, "192.168.0.4", "dd", "CISCO")
        tm.execute("en", 2)
        tm.execute("conf t", 2)
        tm.execute("int s2/0", 2)
        tm.execute("no ip access-group 101 in", 2)

        # 11.
        tm.execute("access-list 102 deny tcp any any eq telnet", 2)
        tm.execute("access-list 102 permit ip any any", 2)
        tm.execute("int s2/0", 2)
        tm.execute("ip access-group 102 in", 2)

        tm.execute("end", 2)
        tm.execute("ex", 2)
        # 重新连接A
        tm.connect(settings.TNA, "192.168.0.3", "dd", "CISCO")
        response = vm.executeScript(3, 1);
        result += response['msg'] + "\n"
        # 重新连接C
        tm.connect(settings.TNC, "192.168.0.5", "dd", "CISCO")
        response = vm.executeScript(3, 3);
        result += response['msg'] + "\n"

    elif number == 4:
        # 12.恢复RouterB的ACL配置
        # 重新连接B
        tm.connect(settings.TNB, "192.168.0.4", "dd", "CISCO")
        tm.execute("en", 2)
        tm.execute("conf t", 2)
        tm.execute("int s2/0", 2)
        tm.execute("no ip access-group 102 in", 2)

        # 13.
        tm.execute("ip dns server", 2)
        tm.execute("ip domain lookup", 2)
        tm.execute("ip host router_c 192.168.23.3", 2)
        tm.execute("access-list 103 deny udp any any eq domain", 2)
        tm.execute("access-list 103 permit ip any any", 2)
        tm.execute("int s2/0", 2)
        tm.execute("ip access-group 103 in", 2)

        tm.execute("end", 2)
        tm.execute("ex", 2)

        # RouterA操作
        # 重新连接A
        tm.connect(settings.TNA, "192.168.0.3", "dd", "CISCO")
        tm.execute("en", 1)
        tm.execute("conf t", 1)
        tm.execute("ip domain lookup", 1)
        tm.execute("ip name-server 192.168.0.4", 1)
        tm.execute("end", 1)

        response = vm.executeScript(4, 1);
        result += response['msg'] + "\n"

    elif number == 5:
        # 14.
        # 重新连接B
        tm.connect(settings.TNB, "192.168.0.4", "dd", "CISCO")
        tm.execute("en", 2)
        tm.execute("conf t", 2)
        tm.execute("int s2/0", 2)
        tm.execute("no ip access-group 103 in", 2)
        tm.execute("end", 2)
        tm.execute("ex", 2)
        # 重新连接A
        tm.connect(settings.TNA, "192.168.0.3", "dd", "CISCO")
        response = vm.executeScript(5, 1);
        result += response['msg'] + "\n"

    print("RESULT：" + result)
    response = {'code': 200, 'msg': result}
    return HttpResponse(JsonResponse(response))


# 时时显示各条操作的执行情况
def getScriptStatus(address):
    return
