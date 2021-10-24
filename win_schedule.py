import requests
import time
from datetime import datetime
import winsound
fileName= open('log.txt','a')
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



    
try:
    result = requests.get(URL, headers=header)
except requests.exceptions.RequestException as e:  # This is the correct syntax
    raise SystemExit(e)
response_json = result.json()
data = response_json["sessions"]
#print(data)

now = datetime.now()
current_time = now.strftime("%H:%M:%S")
# print log as time and centres in log file
print("---------------------finder has begun-------------------------------",file=fileName)
print("Current Time = {}".format(current_time),file=fileName)
flag = False
#playsound(r'C:\Users\gengi\Desktop\Cowin_Bot\ding-sound.mp3') #remove it just for testing

for each in data:
    if((each["available_capacity_dose1"] > 0) & (each["min_age_limit"] == 18) & (each["fee"] == "0")):
        #print("Hello there")
        print("Name of Center : {}".format(each["name"]),file=fileName)
        print("Pincode of the Center : {}".format(each["pincode"]),file=fileName)
        print("Type of Vaccine : {}".format(each["vaccine"]),file=fileName)
        print("No of Vaccines Available : {}".format(each["available_capacity"]),file=fileName)
        flag = True
        #playsound(r'ding-sound.wav') #just check it
        #print the center details in a file

if(flag):
    winsound.PlaySound('notification_sound.wav', winsound.SND_FILENAME)


