# IMPORT LIBRARIES
# THE 'create_devices' FUNCTION IS IMPORTED FROM THE 'create_utils.py' MODULE
# THE ''create_utils.py' MODULE IS PART OF THE 'util' package

from util.create_utils import create_devices
from tabulate import tabulate

# MAIN PROGRAM -----------------------------
if __name__ == '__main__':

    devices = create_devices(num_subnets=5, num_devices=4)
    print("\n", tabulate(devices, headers="keys"))
