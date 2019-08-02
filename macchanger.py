#Dependency of Python3 function
#Linux Only

import subprocess

print("[+] Enter the interface to be adjusted below (EX: wlan0)")

interface = input("Interface referenced > ")

print("[+] Enter the MAC address to be adjusted below (EX: 00:11:22:33:44:55)")

new_mac = input("New MAC address > ")

print("[+] Changing MAC address for " + interface + " to " + new_mac)

subprocess.cal(["ifconfig", interface, "down"])
subprocess.cal(["ifconfig", interface, "hw", "ether", new_mac])
subprocess.cal(["ifconfig", interface, "up"])
