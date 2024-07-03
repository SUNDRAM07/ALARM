from playsound import playsound
import time

def alarm(seconds):
    time_elapsed=0
    time_left=12
    CLEAR="\033[2J"
    CLEAR_AND_RETURN="\033[3H"
    print(CLEAR)
    while time_left>0:
        time.sleep(1)
        time_elapsed+=1
        time_left=seconds-time_elapsed
        minutes=time_left//60
        s= time_left% 60
        print(f"{CLEAR_AND_RETURN}Time left:{minutes:02d}:{s:02d}")
    playsound("masha-ultrafunk.mp3")

Hours=input("Input the hours you want the alarm to sound in: ")
minutes=input("Input the minutes you want the alarm to sound in: ")
seconds=input("Input the seconds you want the alarm to sound in: ")
if minutes.isdigit() and seconds.isdigit() and Hours.isdigit():
    minutes=int(minutes)
    seconds=int(seconds)
    Hours=int(Hours)

total_seconds=(Hours*60*60)+(minutes*60) + seconds
alarm(total_seconds)
print("ALARM IS DONE")