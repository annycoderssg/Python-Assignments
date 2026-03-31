import datetime
import schedule
import time

def Schedule_Minute():
    print("Schedular schedules after every minute... ")
    print( "Current time is: ", datetime.datetime.now() )

def Schedule_Hour():
    print(" *** Schedular schedules after every hour... *** ")
    print( "Current time is: ", datetime.datetime.now() )

def Schedule_Sunday():
    print(" *** Schedular schedules after every sunday... *** ")
    print( "Current time is: ", datetime.datetime.now() )

def main():

    schedule.every(1).minute.do(Schedule_Minute)

    schedule.every().hour.do(Schedule_Hour)

    schedule.every().sunday.do(Schedule_Sunday)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()

# py -m pip install schedule