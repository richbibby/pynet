# IMPORT LIBRARIES
# THE 'create_devices' FUNCTION IS IMPORTED FROM THE 'utils.py' MODULE

from utils import create_devices
from tabulate import tabulate

# MAIN PROGRAM -----------------------------
if __name__ == '__main__':

    devices = create_devices(num_subnets=2, num_devices=10)
    print("\n", tabulate(devices, headers="keys"))
