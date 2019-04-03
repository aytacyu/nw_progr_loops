#!/usr/bin/env python
"""
[Optional/bonus]

*** Note, to actually test this in your environment, change the test IP addresses to something in
your environment that you can ping successfully. ***

Construct a list of 254 IP addresses. The base IP address should be equal to '10.10.100.0' or
'10.10.100.'.

You should use the 'range' builtin to accomplish this.

Your list should have all of the IP addresses from 10.10.100.1 to 10.10.100.254.

Use Python's enumerate to print out all of the IP addresses and their corresponding list index.
The output should look similar to the following:

0 ---> 10.10.100.1
1 ---> 10.10.100.2
2 ---> 10.10.100.3
3 ---> 10.10.100.4
4 ---> 10.10.100.5
...

Use a list slice to create a new list that goes from 10.10.100.3 to 10.10.100.6.

Using a loop and os.system("ping -c 3 10.10.100.3") try pinging all of the IP addresses in this
short list. For Windows the command will probably be os.system("ping -n 3 10.10.100.3").

Put a variable at the top to define whether you are using Windows or Linux/MacOs. This should be
similar to the following:

WINDOWS = False

base_cmd_linux = 'ping -c 2'
base_cmd_windows = 'ping -n 2'
# Ternary operator
base_cmd = base_cmd_windows if WINDOWS else base_cmd_linux

"""
import os
WINDOWS = True

base_cmd_linux = 'ping -c 2'
base_cmd_windows = 'ping -n 2'
# Ternary operator
base_cmd = base_cmd_windows if WINDOWS else base_cmd_linux


ip_list=[]
for i in range(1,255):
    ip_list.append("192.168.1."+str(i))
for i,ip_addr in enumerate(ip_list):
    print("{} ---> {}".format(i,ip_addr))
new_list = ip_list[253:254]

print()
print('-' * 80)
for ip_addr in new_list:
    print("IP Addr: ", ip_addr)
    return_code = os.system("{} {}".format(base_cmd, ip_addr))
    print('-' * 80)
print()