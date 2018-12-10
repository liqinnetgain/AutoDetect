# coding=utf-8

"""
    __author__ : shachuan
    Issue Date : 2018.12.6
    Description :OLT掉线自动检测程序，通过pingIP地址，及时发现掉线的OLT，并发送邮件。初期使用命令行的形式，后期加GUI
    History :
    Version : 1.0

"""
import os
import IPy
from OLT import *
from telnet import *

__author__ = 'shachuan1992'

if __name__ == '__main__':
    with open("平邑OLT地址.txt", 'r') as f:
        iplist = f.readlines()
        for ip in iplist:
            # 对IP进行预处理，得到网络位和网段
            ip_pre = ip.rstrip('\n').split('.')
            network_1 = ip_pre[0]
            network_2 = ip_pre[1]
            network_3 = ip_pre[2]
            ip_type = network_1 + '.' + network_2 + '.' + network_3 + '.' + '0' + '/24'
            #Ping该IP
            info = os.system('ping %s' % ip)
            if info:
                print('%s不通，正在自动更换IP\n' % ip)
                #查找相同网段的IP，并存入ip_backuplist列表中
                ip_backuplist = []
                for ip_backup in iplist:
                    if ((ip_backup in IPy.IP(ip_type)) and (ip_backup != ip)) is True:
                        print(ip_backup)
                        print(type(ip_backup))
                        ip_backuplist.append(ip_backup)

                print(ip_backuplist)
                #有一个问题，就是需要提前判断OLT的IP满了吗？
            else:
                print('%s 正常' % ip)
