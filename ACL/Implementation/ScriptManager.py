from django.http import JsonResponse, HttpResponse
import Implementation.TelnetManager as tm


# 该部分用于执行已有配置脚本

# 根据number选择运行第几个脚本
def executeScript(number):
    if number == 0:
        # 6.RouterB
        tm.execute("en", 2)
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
        tm.execute("en", 1)
        tm.execute("conf t", 1)
        tm.execute("router ospf 1", 1)
        tm.execute("network 192.168.12.0 0.0.0.255 a 0", 1)
        tm.execute("network 192.168.0.0 0.0.0.255 a 0", 1)
        tm.execute("end", 1)
        tm.execute("ex", 1)
        # 6.RouterC
        tm.execute("en", 3)
        tm.execute("conf t", 3)
        tm.execute("router ospf 1", 3)
        tm.execute("network 192.168.12.0 0.0.0.255 a 0", 3)
        tm.execute("network 192.168.0.0 0.0.0.255 a 0", 3)
        tm.execute("end", 3)
        tm.execute("ex", 3)

    elif number == 1:
        # 7.
        tm.execute("en", 2)
        tm.execute("conf t", 2)
        tm.execute("int s2/0", 2)
        tm.execute("no ip access-group 100 in", 2)
        tm.execute("end", 2)
        tm.execute("ex", 2)
    elif number == 2:
        # 9.
        tm.execute("en", 2)
        tm.execute("conf t", 2)
        tm.execute("access-list 101 permit icmp any any echo-reply", 2)
        tm.execute("en", 2)
        tm.execute("int s2/0", 2)
        tm.execute("ip access-group 101 in", 2)
        tm.execute("end", 2)
        tm.execute("ex", 2)
    elif number == 3:
        # 10.恢复RouterB的ACL配置
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

    elif number == 4:
        # 12.恢复RouterB的ACL配置
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
        tm.execute("en", 1)
        tm.execute("conf t", 1)
        tm.execute("ip domain lookup", 1)
        tm.execute("ip name-server 192.168.0.4", 1)
        tm.execute("end", 1)
    elif number == 5:
        # 14.
        tm.execute("en", 2)
        tm.execute("conf t", 2)
        tm.execute("int s2/0", 2)
        tm.execute("no ip access-group 103 in", 2)
        tm.execute("end", 2)
        tm.execute("ex", 2)

    response = {'code': 200, 'msg': 'success'}
    return HttpResponse(JsonResponse(response))


# 时时显示各条操作的执行情况
def getScriptStatus(address):
    return
