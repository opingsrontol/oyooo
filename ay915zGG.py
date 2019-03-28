import requests
import random
import string
import json

s = requests.Session()

nope = str(raw_input('No.: '))
# ref = int(raw_input('Referral: '))
data = {
'screen_densityDpi':480,
'sdk':24,
'sign':'E9HfcF7QHJtHOejV2H/Mdz4OrJw=',
'source':'android_app',
'country_code':'+1',
'phone':nope,
'screen_density':'3.0',
'client_user_id':'-1',
'os':'7.0',
'screen_height':1920,
'device_id_type':3,
'yd_network_status':8,
'device_id':'2974ddad0adb5fde',
'xyy':'',
'local_date':'2019-03-28',
'language':'id',
'screen_width':1080,
'phone_type':'xiaomi_redminote7.0',
'channel':'channel_googleplay_abroad',
'ver':'4.2.2.0.9',
'android_id':'2974ddad0adb5fde',
		}

headers={
	'Connection': 'Keep-Alive',
	'Content-Type': 'application/x-www-form-urlencoded',
	'Host': 'api.yodorun.com',
	'Accept-Encoding': 'gzip',
	'User-Agent': 'okhttp/3.9.1'}
r = s.post('http://api.yodorun.com/sport/login/phone/upload', data=data, headers=headers)
result = json.loads(str(r.text))
if result['code'] == 0:
	print "[+] Success Daftar"
elif result['code'] == 2:
	print "[+] Limit"
else:
	print r.text
otp = int(raw_input('[+] OTP: '))
data2 = {
'screen_densityDpi':480,
'sdk':24,
# 'sign':'6AcTpUBl250ifLjD80KwGqtV+M0',
'source':'android_app',
'country_code':'+1',
'phone':nope,
'screen_density':'3.0',
'client_user_id':'-1',
'code': otp,
'os':'7.0',
'screen_height':1920,
'device_id_type':3,
'yd_network_status':8,
'device_id':'e5d76fb091183ca7',
'xyy':'',
'local_date':'2019-03-28',
'language':'id',
'screen_width':1080,
'phone_type':'xiaomi_redminote7.0',
'channel':'channel_googleplay_abroad',
'ver':'4.2.2.0.9',
'android_id':'e5d76fb091183ca7',
		}
f = s.post('http://api.yodorun.com/sport/login/phone/verify', data=data2, headers=headers)
# print f.text
f_res = json.loads(f.text)
user_id = f_res['user_id']
if user_id:
	print "[+] Verified"
else:
	print f.text
ref = int(raw_input("[+]Referral: "))
data3 = {'user_id':user_id,
'code':ref,
'language':'en'}
g = s.post('http://api.yodorun.com/sport/v2/upload_invite_code', data=data3, headers=headers)
g_res = json.loads(str(g.text))
if g_res['code'] == 0:
	print "[+] Success!"
else:
	print g.text