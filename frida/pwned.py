#!/usr/bin/python
import frida, sys, time

encrypted = None

def on_message(message, data):
    
    if message['type'] == 'send':
      print('[*] {0}'.format(message['payload']))
    else:
      print message
      
jscode = open('pwned.js').read()

print('[+] Running')

process_name = 'com.pwned'
device = frida.get_usb_device()

try:
    pid = device.get_process(process_name).pid
    print('[+] Process found')
except frida.ProcessNotFoundError:
    print('[+] Starting process')
    pid = device.spawn([process_name])
    device.resume(pid)
    time.sleep(1)

process = device.attach(pid)

script = process.create_script(jscode)
script.on('message', on_message)
script.load()
while True:
    time.sleep(1)
sys.stdin.read()