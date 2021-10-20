import os
from datetime import datetime


def cpu_rapport():
	date = datetime.now().strftime("%Y-%m-%d")
	full_time = datetime.now().strftime("%H:%M:%S")

	cpu_filename = '~/cpuUsage/report/cpu_' + date + '.log'
	f = open(cpu_filename, "a")
	f.write(full_time + '\n')

	ps_output = os.popen('ps -o pid,user,%mem,command ax | grep -v PID').read().splitlines()

	tmp_txt = ''

	for item in ps_output:
		tx = item.split()
		# wf = ps_output[item] +','+ ps_output[item+1] + ',' + ps_output[item+2] + '\n'
		if tx[2] != '0.0':
			wf = tx[0] + ',' + tx[1] + ',' + tx[2] + ','
			if len(tx) > 3:
				for i in range(3, len(tx) - 1):
					tmp_txt += tx[i] + ' '
				wf += tmp_txt
		f.write(wf + '\n')
	f.close()

def get_total_mem():
  total_raw_mem=os.popen('cat /proc/meminfo | grep MemTotal').read().split()
  return int(total_raw_mem[1])/1024/1024

def check_free_mem_per():
  mem_raw=os.popen('free -mw | grep Mem').read().split()
  free_mem_percent="{:.2}".format(int(mem_raw[3])/int(mem_raw[1]))
#  print(f"Total Memory: {mem_raw[1]}")
#  print(f"Free Memory: {mem_raw[3]}")
#  print(f"Free Memory Percent: {free_mem_percent}%")
#  print("#############################################")
  return float(free_mem_percent)

def check_cpu():
  mpstat_raw=os.popen('mpstat | grep all').read().split()
#  print(f"IO wait %: {mpstat_raw[5]}")
#  print(f"Idle %: {mpstat_raw[11]}")

