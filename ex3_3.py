#!/usr/bin/env python
'''
Read the 'show_lldp_neighbors_detail.txt' file. Loop over the lines of this file. Keep reading the
lines until you have encountered the remote "System Name" and remote "Port id". Save these two items
into variables and print them to the screen. You should extract only the system name and port id
from the lines (i.e. your variables should only have 'twb-sf-hpsw1' and '15'). Break out of your
loop once you have retrieved these two items.
'''


with open("show_lldp_neighbors_detail.txt","r") as f:
    show_lldp = f.read()
found_port_id = False
found_system_name = False
for line in show_lldp.splitlines():
    if "Port id:" in line:
        _, port_id = line.split('Port id: ')
        found_port_id = True
    elif "System Name:" in line:
        _, system_name = line.split('System Name: ')
        found_system_name = True
    if found_system_name and found_port_id:
        break
print("Port id: {}".format(port_id))
print("System Name: {}".format(system_name))
