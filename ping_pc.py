import subprocess
from config import Config
from arpnet import arp_a


def main():
    # IP address to look for
    address = Config.LOOK_FOR_IP

    # run ping command
    cmd = ['ping -n 3' + ' ' + address]
    res = str(subprocess.run([cmd], capture_output=True))
    if res:
        arp_a()


if __name__ == '__main__':
    main()
