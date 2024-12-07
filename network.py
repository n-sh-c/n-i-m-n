import pyfiglet
from termcolor import colored
result = colored(pyfiglet.figlet_format('naser', font = 'banner3-D'), 'white')
print(result)
print('N-I-M-N'.center(50))
print('[1] My Ip Address')
print('[2] My Mac Address')
print('[3] Range Ip Address (Network Lan)')
print('[4] Exit')
input_user = input('Select the desired option : ')
while True :
    if input_user == '1' :
        print('[1] Ip Address (Wireless)')
        print('[2] Ip Address (Ethernet)')
        input_ip = input('Select the desired option : ')
        if input_ip == '1' :
            pass 
        elif input_ip == '2' :
            pass 
        