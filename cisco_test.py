"""
 连接Cisco网络设备测试
 作者：周亮
 创建时间：2021-10-20
 修改时间：2021-10-20
 说明：
"""


import os
import pandas
from getpass import getpass
from netmiko import ConnectHandler

def openFile(person, author):
    """
    :param person:
    :param author:
    :return:
    """
    pass

if __name__ == '__main__':
    # password = os.getenv('NETMIKO_PASSWORD') if os.getenv("NETMIKO_PASSWORD") else getpass

    # net_conn = ConnectHandler(
    #     device_type='cisco_ios',
    #     host='192.168.1.126',
    #     username='zhouliang',
    #     password='zl001'
    # )
    # device = {
    #     'device_type': 'cisco_ios',
    #     'host': '192.168.1.105',
    #     'username': 'cisco',
    #     'password': 'cisco',
    #     'secret': 'cisco'
    # }

    # 打开excel文件
    data_frame = pandas.read_excel('device.xlsx', sheet_name='Sheet1')
    device_info = data_frame.to_dict(orient='records')
    print(device_info)
    for device in device_info:
        with ConnectHandler(**device) as net_conn:
            # print(net_conn.find_prompt())
            device_name = net_conn.find_prompt()
            net_conn.enable()
            # print(net_conn.find_prompt())
            output = net_conn.send_command('show ip interface brief', expect_string=r'#')
            print(device_name)
            print(output)
