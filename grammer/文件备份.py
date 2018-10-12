# !/usr/bin/python
# Filename:back_up.py
import os
import time

'''source = ['F:\\steam', 'F:\\word']
target_dir = 'F:\\Backup'
target = target_dir + os.sep + time.strftime('%Y%m%d%H%M%S') + '.zip'
zip_command = "zip -qr {0} {1}".format(target, '   '.join(source))
print(zip_command)
if os.system(zip_command) == 0:
    print("Successful backup to", target)
else:
    print('Backup failed!')     '''
# 获取系统时间
_time = time.strftime('%Y-%m-%d %H:%M:%S')
# format_time = _time[:4] + '年' + _time[4:6] + '月' + _time[6:8] + '日' + _time[8:10] + '时' + _time[10:12] + '分' + _time[12:] + '秒'
# Time = "系统时间：" + format_time
print(_time)
