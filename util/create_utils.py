# IMPORT LIBRARIES

from random import choice

# FUNCTION TO GENERATE A LIST OF DEVICES


def create_devices(num_devices=1, num_subnets=1):

    # CREATE EMPTY LIST TO HOLD NETWORK DEVICES
    created_devices = list()

    if num_devices > 254 or num_subnets > 254:
        print("Error: Too many devices and/or subnets requested")
        return created_devices

    # FOR LOOP TO GENERATE X NUMBER OF DEVICES IN X NUMBER OF SUBNETS
    for third_octet_ip in range(1, num_subnets+1):

        for last_octet_ip in range(1, num_devices+1):

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
            device["ip_addr"] = "10.0." + str(third_octet_ip) + "." + str(last_octet_ip)

            # APPEND THE DEVICE TO THE LIST OF DEVICES
            created_devices.append(device)

    return created_devices
