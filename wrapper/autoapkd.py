import subprocess, os, glob, sys
from pathlib import Path
from subprocess import Popen 
from colorama import Fore, Back, Style

ok = Fore.GREEN+'['+Fore.RESET+'+'+Fore.GREEN+']'+Fore.RESET+' '
err = Fore.RED+'['+Fore.RESET+'!'+Fore.RED+']'+Fore.RESET+' '
info = Fore.BLUE+'['+Fore.RESET+'-'+Fore.BLUE+']'+Fore.RESET+' '
RS   = Style.RESET_ALL
FR   = Fore.RESET
YL   = Fore.YELLOW
RD   = Fore.RED


def log(msg):
    
    print(msg)

def banner():
    SIG = """
    _______  __   __  _______  _______  _______  _______  ___   _  ______  
    |   _   ||  | |  ||       ||       ||   _   ||       ||   | | ||      | 
    |  |_|  ||  | |  ||_     _||   _   ||  |_|  ||    _  ||   |_| ||  _    |
    |       ||  |_|  |  |   |  |  | |  ||       ||   |_| ||      _|| | |   |
    |       ||       |  |   |  |  |_|  ||       ||    ___||     |_ | |_|   |
    |   _   ||       |  |   |  |       ||   _   ||   |    |    _  ||       |
    |__| |__||_______|  |___|  |_______||__| |__||___|    |___| |_||______| 

    [*] AUTOAPKD is a wrapper script for apktool to decompile N apk files inside a target folder.
    [*] Author: xD0tz 
    """

    return SIG 

def main(apkdir):

    log(info + "APK directory " + apkdir)

    os.chdir(apkdir)
    for file in glob.glob("*.apk"):
        
        log(info + "Processing APK file: " + file)
        p = Popen(["apktool", "d","-r", file], stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
        output, errors = p.communicate()
        log(info + "Command output: " + output) 
        log(err + "Errors: " + errors) 
        log(ok + "APK decompilation finished")
if __name__ == "__main__":

    print(banner())
    if len(sys.argv) != 2:
        log(err + "usage: python " + sys.argv[0] + " /home/apk" + "\n")
        sys.exit(-1)
    
    apkdir = sys.argv[1]
    main(apkdir)
   


  
    