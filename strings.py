from pprint import pprint

device1_str = "   r3-l-n7, cisco , catalyst 2960, ios  "

# SPLIT
print("STRING STRIP, SPLIT, REPLACE")
device1 = device1_str.split(",")
print("\ndevice1 using split:")
print("    ", device1)

# STRIP
device1 = device1_str.strip().split(",")
print("device1 using strip and split:")
print("    ", device1)

# REMOVE BLANKS
device1 = device1_str.replace(" ", "").split(",")
print("device1 replaced blanks using split:\n    ", device1)

# REMOVE BLANKS, CHANGE COMMA TO COLON
device1_str_colon = device1_str.replace(" ", "").replace(",", ":")
print("device1 replaced blanks, comma to colon:")
print("    ", device1_str_colon)

# LOOP WITH STRIP AND SPLIT
device1 = list()
for item in device1_str.split(","):
    device1.append(item.strip())
print("device1 using loop and strip for each item:")
print("    ", device1)

# STRIP AND SPLIT, SINGLE LINE USING LIST COMPREHENSION
device1 = [item.strip() for item in device1_str.split("'")]
print("device1 using list comprehension:")
print("    ", device1)

# IGNORING CASE
print("\n\nIGNORING CASE")
model = "CSR1000V"
if model == "CSR1000V":
    print(f"matched: {model}")
else:
    print(f"didn't match: {model}")

model = "CSR1000V"
if model.lower() == "csr1000v":
    print(f"matched using lower: {model}")
else:
    print(f"didn't match: {model}")

# FIND SUBSTRING
print("\n\nFINDING SUBSTRING")
version = "Cisco IOS Software, ISR Software (X86_64_LINUX_IOSD-UNIVERSALK9-M), Version 15.5(3)S4b, RELEASE SOFTWARE (fc1)"
expected_version = "Version 15.5(3)S4b"
index = version.find(expected_version)
if index >= 0:
    print(f"found version: {expected_version} at location {index}")
else:
    print(f"not found version: {expected_version}")

# SEPARATING STRING COMPONENTS
print("\n\nSEPARATING VERSION STRING COMPONENTS")
version_info = version.split(",")
for version_info_part in version_info:
    print(f"version part: {version_info_part.strip()}")

show_interface_stats = """
Vlan711
          Switching path    Pkts In   Chars In   Pkts Out  Chars Out
               Processor  969462630 73620298779          0          0
             Route cache          0          0   42456252 11473769102
                   Total  969462630 73620298779   42456252 11473769102
GigabitEthernet1/0/1
          Switching path    Pkts In   Chars In   Pkts Out  Chars Out
               Processor     718194  303795707          0          0
             Route cache          0          0    6885344  718457903
                   Total     718194  303795707    6885344  718457903
"""

interface_counters = dict()
show_interface_stats_lines = show_interface_stats.splitlines()
for index, stats_line in enumerate(show_interface_stats_lines):
    if stats_line.find('GigabitEthernet1', 0 ) == 0:

        totals_line = show_interface_stats_lines[index + 4]
        interface_counters[stats_line] = totals_line.split()[1:]

print("\n\n--------- Interface Counters------------------")
pprint(interface_counters)

show_arp = """
Protocol  Address          Age (min)  Hardware Addr   Type   Interface
Internet  10.26.40.1              5   ec1d.8b20.1b90  ARPA   Vlan711
Internet  10.26.40.2              -   d42c.440f.bb6f  ARPA   Vlan711
Internet  10.26.40.129            -   d42c.440f.bb56  ARPA   Vlan20
Internet  172.26.40.1             -   d42c.440f.bb46  ARPA   Vlan10
Internet  172.26.40.129           -   d42c.440f.bb54  ARPA   Vlan15
"""

arp_table = dict()
for arp_line in show_arp.splitlines():
    if arp_line.lower().find("internet", 0) == 0:
        arp_table[arp_line[10:25].strip()] = arp_line[38:52]

print("\n\n--------- ARP Table ------------------")
pprint(arp_table)
