import requests
import time
from playsound import playsound
from datetime import datetime
import winsound

today = datetime.today()

d1 = today.strftime("%d-%m-%Y")
#implement search 

pinCode = 110043 #hardcoded for Najafgarh
date = d1
district_id = 150 #hardcoded for South West Delhi



URL = 'https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByPin?pincode={}&date={}'.format(
    pinCode, date)
# URL='https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByDistrict?district_id={}&date={}'.format(district_id,date)
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'}

# 1 for availaibility play shape of you and sleep for 30seconds
# 2 for not availaibility sleep for 10 seconds


def isAvailable():
    
    try:
        result = requests.get(URL, headers=header)
    except requests.exceptions.RequestException as e:  # This is the correct syntax
        raise SystemExit(e)
    response_json = result.json()
    data = response_json["sessions"]
    #print(data)
    print("---------------------finder has begun-------------------------------")
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print("Current Time = ", current_time)
    flag = False
    #playsound(r'C:\Users\gengi\Desktop\Cowin_Bot\ding-sound.mp3') #remove it just for testing
    
    for each in data:
        if((each["available_capacity_dose1"] > 0) & (each["min_age_limit"] == 18) & (each["fee"] == "0")):
            #print("Hello there")
            print("Name of Center : {}".format(each["name"]))
            print("Pincode of the Center : {}".format(each["pincode"]))
            print("Type of Vaccine : {}".format(each["vaccine"]))
            print("No of Vaccines Available : {}".format(each["available_capacity"]))
            flag = True
            #playsound(r'ding-sound.wav') #just check it

    if(flag==False):
        print("No Available Slots")
        return 2
    else :
        return 1


# while(True):
#     if(isAvailable() == 1):
#         print("Vaccine available please Register")
#         count = 0
#         while (count < 3):   
#             count = count + 1
#             winsound.PlaySound('notification_sound.wav', winsound.SND_FILENAME)
#         print("Sleeping for 30 seconds")
#         time.sleep(30)

#     else:
#         print("Sleeping for 10 seconds")
#         time.sleep(10)
class Requester(threading.Thread):
  def __init__(self, url, credentials, payload):
    threading.Thread._init__(self)
    self.url = url
    self.credentials = credentials
    self.payload = payload        
  def run(self):
    # do the post request here
    # you may want to write output (errors and content) to a file
    # rather then just printing it out sometimes when using threads 
    # it gets really messing if you just print everything out


if __name__ == '__main__':
  counter = 0
  while counter < 1800:
    req = Requester(url, credentials, payload)
    req.start()
    counter++
    time.sleep(10)