#默认下班时间是：19:40。
#高级拓展：外置可配置的文件。界面美观。
import time
while True:
	current=time.strftime('%H:%M:%S',time.localtime(time.time()))

	list_current=current.split(':')

	current_hour=int(list_current[0])
	current_minute=int(list_current[1])
	current_second=int(list_current[2])

	target_hour=int('19')
	target_minute=int('40')
	target_second=int('60')


	remain_minute=target_minute - current_minute

	if remain_minute < 0:
		target_minute=target_minute+60
		target_hour=target_hour - 1
		
	remain_hour=target_hour - current_hour
	remain_minute=target_minute - current_minute	
	remain_second=target_second - current_second

	# print("shengyushijain:%d"%remain_hour)
	# print("shengyushijain:%d"%remain_minute)
	# print("shengyushijain:%d"%remain_second)
	print("距离玩耍时间还剩%d小时%d分钟%d秒"%(remain_hour,remain_minute,remain_second))
	time.sleep(1.7)

	

