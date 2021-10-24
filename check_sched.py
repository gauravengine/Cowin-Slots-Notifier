import schedule
import time
fileName= open('log.txt','a')
def job():
    print("Hello world",file=fileName)

#time 
schedule.every(10).seconds.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)