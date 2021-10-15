#!/usr/bin/env python3 

import os 
from datetime import datetime  




def cpu_rapport():
	date = datetime.now().strftime("%Y-%m-%d")
	full_time = datetime.now().strftime("%H:%M:%S")

	cpu_filename = 'cpu_' + date + '.log'
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
cpu_rapport()



