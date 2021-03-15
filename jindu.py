import sys,time
for i in range(30):
    sys.stdout.write('*')
    sys.stdout.flush()  #更新缓冲区
    time.sleep(0.5)

print('*',end='',flush=True)