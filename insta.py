#~ View Instagram Profile Picture at Full Size
#~ Coder : Cavid Rustamli
#~ Instagram : @rust4mlee

import requests,os,re,webbrowser

if os.name == "nt":
	os.system("cls")
else:
	os.system("clear")

print("""
#~ View Instagram Profile Picture at Full Size
#~ Coder : Cavid Rustamli
#~ Instagram : @rust4mlee
""")

user = input("Instagram user : ")

try:
	r = requests.get("https://www.instadp.com/fullsize/" + user)
	profile_pic = re.findall('<a class="download-btn" href="(.*?)" target="_blank"><i></i>Download</a>',r.text)
	print("\nProfile Picture URL Opened!")
	webbrowser.open(profile_pic[0])
except:
	print("Error! Please run again later!")