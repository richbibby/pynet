# import libraries

from pprint import pprint
# a dictionary to represent a network device

device = {
    "hostname": "router-1",
    "ip_addr": "10.10.10.1",
    "vendor": "cisco",
    "model": "ISR4321/K9",
    "os": "Cisco IOS-XE 15.5(3)S4b",
    "role": "spoke-router",
}

# simple print the device dictionary

print("\n______ SIMPLE PRINT __________")
print("device: ", device)
print("device name: ", device['hostname'])

# pretty print the device dictionary
print("\n______ PRETTY PRINT __________")
pprint(device)

# loop over the dictionary items and print nicely formatted key/value pairs
print("\n______ FOR LOOP, F-STRINGS __________")
for key, value in device.items():
    print(f"{key:>10s} : {value}")
