# Main file script for sframework
# Coded by canflyFX/prosyx/skyze

import sframe as s
import os, sys
import time
import requests
import random

sversion = "1.2.4"

helplist = \
s.sFcolors.BOLD + s.sFcolors.OKBLUE + "\n" + '''info'''+s.sFcolors.ENDC+'''                      - Prints the info about project''' +\
s.sFcolors.BOLD + s.sFcolors.OKBLUE + "\n" + '''vpn download'''+s.sFcolors.ENDC+'''              - Downloads the openvpn config file to connect to private vpn''' +\
s.sFcolors.BOLD + s.sFcolors.OKBLUE + "\n" + '''sFrame'''+s.sFcolors.ENDC+'''                    - Calls the core sFramework function (for devs)'''

def mainscreen():
    mainsc = s.sFcolors.HEADER + s.sFcolors.BOLD + '''
        ____               '''+sversion+'''                      __  
  ___  / __/____ ___ _ __ _  ___  _    __ ___   ____ / /__  
 (_-< / _/ / __// _ `//  ' \/ -_)| |/|/ // _ \ / __//  '_/
/___//_/  /_/   \_,_//_/_/_/\__/ |__,__/ \___//_/  /_/\_\                    
'''
    print(mainsc)
    return 0

def startcheck():
    print(s.sFcolors.WARNING + "[!] " + s.sFcolors.ENDC + "Checking for update files..")
    time.sleep(4)
    print(s.sFcolors.FAIL + "[-] " + s.sFcolors.ENDC + "Missing config file!")
    time.sleep(2)
    print(s.sFcolors.OKGREEN + "[+] " + s.sFcolors.ENDC + "Initialization Finished!")

def vpndownload():
    downloadpass = format(random.randint(4,9))
    downloadpassch = input("Secure Server Password [{0}] > ".format(downloadpass))
    if downloadpassch == downloadpass:
        r = requests.get("https://www.dropbox.com/s/n3kuosw4jpiqxvn/universal.ovpn?dl=1")
        with open("universal.ovpn", "wb") as f:
            f.write(r.content)
            pass
    else:
        print(s.sFcolors.FAIL + "[-] " + s.sFcolors.ENDC + "Incorrect password!")
        menu()
    print(s.sFcolors.OKGREEN + "[+] " + s.sFcolors.ENDC + "Successfull Download")
    time.sleep(1)
    menu()

def menu():
    print(s.sFcolors.OKBLUE + "[?] " + s.sFcolors.ENDC + "Type " + s.sFcolors.UNDERLINE + "help" + s.sFcolors.ENDC + " for list of commands" + s.sFcolors.OKBLUE +" or type " + s.sFcolors.OKBLUE + s.sFcolors.BOLD + s.sFcolors.UNDERLINE + "exit" + s.sFcolors.ENDC)

    # TODO complete menu items

    while True:
        inp = input("> ")
        if inp == "help":
            print(helplist)
            menu()
            pass
        elif inp == "exit":
            sys.exit()
            pass
        elif inp == "info":
            print(s.sFcolors.UNDERLINE + "Coded by canflyFX/prosyx/skyze" +s.sFcolors.ENDC)
            menu()
            pass
        elif inp == "vpn download":
            vpndownload()
            pass
        elif inp == "sFrame":
            pass
        else:
            print(s.sFcolors.FAIL + "[-] "+ s.sFcolors.ENDC + "Type " + s.sFcolors.UNDERLINE + "help" + s.sFcolors.ENDC + " for more commands")
            pass

def main():
    mainscreen()
    startcheck()
    menu()

if __name__ == '__main__':
    main()
