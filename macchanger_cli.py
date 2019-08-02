#MM - Linux Only.
#MM - Dependency of Python3 functions with input. To use 2.*, change to raw_input.
#MM - 08.02.2019 - Have removed all shell=True because it is a security hazard.
#MM - 08.02.2019 - Updated to pass parameters in CLI using optparse.

import subprocess
import optparse

#Parser object variable is a child of the class/parent OptionParser.
parser = optparse.OptionParser()

#2 options the user can enter. The dest is where we will be retrieving the user input.
parser.add_option("-i", "--interface", dest="interface", help="Interface to have its MAC address changed")
parser.add_option("-m", "--mac", dest="new_mac", help="New MAC address")

#Method that allows the object to understand what the user has entered and handle it.
(options, arguments) = parser.parse_args()

interface = options.interface
new_mac = options.new_mac

print("[+] Changing MAC address for " + interface + " to " + new_mac)

subprocess.cal(["ifconfig", interface, "down"])
subprocess.cal(["ifconfig", interface, "hw", "ether", new_mac])
subprocess.cal(["ifconfig", interface, "up"])
