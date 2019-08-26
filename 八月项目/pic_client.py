#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @Author  :   {Titanxz}
# @Time    :   2019/8/23 20:18
# @License :   (C) Copyright 2019, {python_1904}


# 客户端

# 导包
from socket import *

# 初始化信息
ip = '169.254.190.190'
port = 6636
buf_size = 1024
address = (ip, port)

# 创捷套接字
tcp_client_socket = socket(AF_INET, SOCK_STREAM)

# 连接服务器
tcp_client_socket.connect(address)

# 接受数据
file = open('i1.jpg', 'wb')
while 1:
    image_data = tcp_client_socket.recv(buf_size)
    if not image_data:
        print('数据读取完毕...')
        break
    file.write(image_data)


# 关闭资源
tcp_client_socket.close()