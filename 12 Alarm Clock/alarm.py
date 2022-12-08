#pip install playsound==1.2.2

from playsound import playsound
import datetime

beep = 'beep_alarm.mp3'
alarmHour = int(input('Enter hour: '))
alarmMin = int(input('Enter Mins: '))
alarmAm = input('am/pm: ')
if alarmAm == 'pm':
	alarmHour += 12

while True:
	if alarmHour == datetime.datetime.now().hour and alarmMin == datetime.datetime.now().minute:
		print('Playing ')
		playsound(beep)
		break
