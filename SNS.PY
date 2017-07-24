import requests
import time
import re
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
url = 'https://sneakersnstuff.typeform.com/app/form/submit/Hathk3'
print("SNS raffle script for the Mars Yard sneakers written by @fockniketalk")
print("If u bought this from some1 please contact me on twitter @fockniketalk")
headers = {'User-Agent':
           'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}

def main(limit):
    for i in range(0, limit):
	payload ={
		'form[email:Fi1mS3bZn3VF]': 'youremail@gmail.com', #change to your email
		'form[landed_at]': '1500901708', # don't change 
		'form[language]': 'en', # don't change
		'form[terms:QS4P6gmSVp8s]': '1', # don't change
		'form[textfield:Boa0BNN75u6R]': 'Amsterdam', # change to ur city
		'form[textfield:EKZm78mYLBbE]': 'Streetname 2', # change to ur streetname + number
		'form[textfield:IIdtgeMwp8Gp]': 'Fock', # first name
		'form[textfield:MQfwQiem4TEw]': '1111AA', # zip code
		'form[textfield:bHSS1rapvhha]': 'NikeTalk', # Last name
		'form[textfield:n3yXjbpstFmJ]': 'None', # change to ur state, if EU set: None
		'form[textfield:u9og65Z22NNB]': 'The Netherlands', # change to ur country
		'form[token]': 'e5455f13bd09203c7f5f0b433129e116$2y$11$e2dJZC0zIXZQK1pxbSZbL.LzJE2QS5SFRX2Z7Lk/oL/j6JicEpiXS', # don't change
		'form[yes-no:warE3SilldbG]': '1', # don't change
		            }
        resp = requests.post(url, data=payload, headers=headers)
        if any(re.findall(r'succes', str(resp.text), re.IGNORECASE)):
			print(time.strftime("%H:%M:%S") + " / Successfully entered SNS raffle mars yard, written by @fockniketalk")
        else:
		print(time.strftime("%H:%M:%S") + " / Could not enter!")
main (500) # 100 will do 100 entries, u can change it. 
exit()
