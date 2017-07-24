import requests, time, re, sys, random
#reload(sys)
#sys.setdefaultencoding('utf-8')
url = 'https://sneakersnstuff.typeform.com/app/form/submit/Hathk3'
print("SNS raffle script for the Mars Yard sneakers written by @fockniketalk")
print("If u bought this from some1 please contact me on twitter @fockniketalk")
print("btw if u need verified nike accounts usa & eu hit my dm @fockniketalk")

headers = {'User-Agent':
           'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}

sizes = ['US 6','US 7', 'US 8', 'US 8.5', 'US 9', 'US 9.5', 'US 10' ,'US 10.5' ,'US 11' ,'US 11.5' ,'US 12', 'US 13']

def dot_trick(username): # PUT UR GMAIL IN LINE 54
    emails = list()
    username_length = len(username)
    combinations = pow(2, username_length - 1)
    padding = "{0:0" + str(username_length - 1) + "b}"
    for i in range(0, combinations):
        bin = padding.format(i)
        full_email = ""

        for j in range(0, username_length - 1):
            full_email += (username[j]);
            if bin[j] == "1":
                full_email += "."
        full_email += (username[j + 1])
        emails.append(full_email + "@gmail.com")
    return emails

def main(limit, emails):
    for i in range(0, limit):
        payload ={
            'form[email:Fi1mS3bZn3VF]': emails [i], #PUT UR GMAIL WITH @GMAIL.COM IN LINE 54
			'form[list:56641463][choices]': sizes[random.randint(0, 11)],
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
emails = dot_trick('FockNikeTalk') #Gmail ONLY, PUT UR GMAIL HERE
main (len(emails),emails) 
exit()
