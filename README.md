# Cowin-Slots-Notifier

![COWIN-SLOTS-NOTIFIER](https://ibb.co/gmCm8M0)

## YouTube Demo
- Check the demo for how this works on YouTube [here](https://youtu.be/abZJ_-efGyE).

## Features
- Sit back and relax - the script will notify you whenever a slot is available in your area
- It makes API calls in every 10 seconds so that you get notified as soon as possible
- Don't like a feature? Change it! Raise a Pull Request too 😉

## Installation
- You need Python
- Install dependencies by running
```bash
pip install requests
```
- Clone this repo 
```bash
git clone https://github.com/gauravengine/Cowin-Slots-Notifier.git
cd Cowin-Slots-Notifier
python main_script.py
```
- If you want to search Vaccines by your Pin Code Enter 1 and then Enter your Pin Code
- Else Enter 2 if you want to Search Vaccines District Wise
    - Check your state_id from list and enter it
    - Then Check your  district_id and enter it
- Now the bot will check for `Free` vaccines available for age group 18+ 
- If Slots are available it will play a notification sound and will sleep for 30 seconds after notifying all centers available 
- If slots are not available it will sleep for 10 seconds and then will check again
- Currently the limit of this API is 100 calls per 5 minutes or 1 call in 3 seconds so make changes accordingly 😉