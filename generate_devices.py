# IMPORT LIBRARIES

from random import choice
from tabulate import tabulate
from operator import itemgetter
from pprint import pprint

# CREATE EMPTY LIST TO HOLD NETWORK DEVICES
devices = list()

# FOR LOOP TO GENERATE X NUMBER OF DEVICES
for last_octet_ip in range(1, 20):

    # EACH DEVICE TO BE CREATED IS A DICTIONARY
    device = dict()

    # RANDOM VALUE FOR DEVICE KEY 'hostname'
    device["hostname"] = (
        choice(["uk-", "us-"])
        + choice(["east-", "west-", "north-", "south-"])
        + choice(["r1", "r2", "r3", "r4", "r5"])
    )

    # RANDOM VALUE FOR DEVICE KEYS 'vendor', 'os', and 'version'
    device["vendor"] = (choice(["cisco", "juniper", "arista"]))
    if device["vendor"] == "cisco":
        device["os"] = choice(["ios", "iosxe", "iosxr", "nxos"])
        device["version"] = choice(["11.1", "11.5", "12.2", "15.6"])
    elif device["vendor"] == "juniper":
        device["os"] = "junos"
        device["version"] = choice(["10.5", "10.8", "12.1"])
    elif device["vendor"] == "arista":
        device["os"] = "eos"
        device["version"] = choice(["6.5", "7.8", "9.1"])

    # SET VALUE FOR KEY 'ip_addr'
    device["ip_addr"] = "10.0.0." + str(last_octet_ip)

    # NICELY FORMAT AND PRINT THE DEVICE
    for key, value in device.items():
        print(f"{key:>10s} : {value}")

    # APPEND THE DEVICE TO THE LIST OF DEVICES
    devices.append(device)

# USE PPRINT TO PRINT THE DATE AS-IS
print("\n______ PRINT DEVICES AS LIST OF DICTS __________")
pprint(devices)

# USE 'TABULATE' TO PRINT A TABLE OF THE DEVICES
print("\n______ SORTED DEVICES IN TABULAR FORMAT __________")
print(tabulate(sorted(devices, key=itemgetter("vendor", "os", "version")), headers="keys"))
