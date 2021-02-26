#自动同步时间 kvm虚拟机长时间就会产生这种问题
import os 
import time 
import ntplib 
 
 
 
client = ntplib.NTPClient() #create a object 
response = client.request('europe.pool.ntp.org') #pool.ntp.org is null. 
 
ts = response.tx_time #ntp server return 时间戳
 
_date = time.strftime('%Y-%m-%d',time.localtime(ts)) #time.localtime() change 时间戳 to local struct time
_time = time.strftime('%X',time.localtime(ts))  #time.strftime() change local struct time to string time

#print(_date)
#print(_time)
 
os.system('date {} && time {}'.format(_date,_time)) #date is windows system command, to set year,month,day
#time is windows systemctl command,to set hour,minute,seconds

print("synchronize is ok!")
time.sleep(2)
