import requests
import time
from datetime import datetime
import winsound




today = datetime.today()
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'}
d1 = today.strftime("%d-%m-%Y")
date = d1
print("Do You Want To search by Pin Code or by District ?")
print("Enter 1 for by Pin Code and 2 for by District ")
a = int(input())
if(a == 1):
    print("Please Enter Your Pin Code ")
    userPin = int(input())
    URL = 'https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByPin?pincode={}&date={}'.format(
        userPin, date)
else:
    stateURL = 'https://cdn-api.co-vin.in/api/v2/admin/location/states'
    statesData = requests.get(stateURL, headers=header)
    statesJson = statesData.json()
    list_states = statesJson["states"]
    print(type(list_states))
    for each in list_states:
        print("State Name = {} , state_id = {} \n".format(
            each["state_name"], each["state_id"]))
    print("Please Enter the corresponding state_id of your state")
    userStateID = int(input())
    districtURl = 'https://cdn-api.co-vin.in/api/v2/admin/location/districts/{}'.format(
        userStateID)
    districtData = requests.get(districtURl, headers=header)
    districtJson = districtData.json()
    list_districts = districtJson["districts"]
    for each in list_districts:
        print("District Name = {} District ID = {} \n ".format(
            each["district_name"], each["district_id"]))
    print("Please Enter the corresponding district ID of the state you want to search ")
    userDistrictID = int(input())
    URL = 'https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByDistrict?district_id={}&date={}'.format(
        userDistrictID, date)


def isAvailable():

    result = requests.get(URL, headers=header)
    response_json = result.json()
    data = response_json["sessions"]
    # print(data)
    print("---------------------finder has begun-------------------------------")
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print("Current Time = ", current_time)
    flag = False
    # playsound(r'C:\Users\gengi\Desktop\Cowin_Bot\ding-sound.mp3') #remove it just for testing

    for each in data:
        if((each["available_capacity_dose1"] > 0) & (each["min_age_limit"] == 18) & (each["fee"] == "0")):
            #print("Hello there")
            print("Name of Center : {}".format(each["name"]))
            print("Pincode of the Center : {}".format(each["pincode"]))
            print("Type of Vaccine : {}".format(each["vaccine"]))
            print("No of Vaccines Available : {} ".format(
                each["available_capacity"]))
            print("-"*50)
            winsound.PlaySound('new_notif.wav', winsound.SND_FILENAME)

            flag = True
            

    if(flag == False):
        print("No Available Slots")
        return 2
    else:
        return 1


while(True):
    if(isAvailable() == 1):
        print("Vaccine available please Register")
        count = 0
        while (count < 3):
            count = count + 1
            winsound.PlaySound('notification_sound.wav', winsound.SND_FILENAME)
        print("Sleeping for 30 seconds")
        time.sleep(30)

    else:
        print("Sleeping for 10 seconds")
        time.sleep(10)
