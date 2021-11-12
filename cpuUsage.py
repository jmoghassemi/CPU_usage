#! /usr/bin/env python3

########### Import Section #####################
import os
import sys
import argparse
import time
from datetime import datetime
import functions as func

########## Variable Definition ################
default_limit = round(func.get_total_mem()*0.75)
default_min=3

########## Main Section ####################
if __name__ == "__main__":
    
	parser = argparse.ArgumentParser(description='This program monitors CPU and Memory usage via a specially designed service file.')
	
	parser.add_argument('byte_limit_value', type=int, nargs='?', help=f'This parameter specifies the critial threshold for memory usage. Once memory usage exceeds this value, the python script starts to create a status report, which by default is saved at /etc/cpuUsage. \n The Default value for byte_limit_value is 75%% of {int(func.get_total_mem())} GB.\n byte_limit_value needs to be a positive integer and in MB.', default=default_limit)

	parser.add_argument('minutes', type=int, nargs='?', help='This parameter indicates at what time intervals the script needs to check memory usage and is measured in minutes.\n The default value is 3 minutes. \nThe accepted values for this variable range from 1 to 60 minutes.', default=default_min)
	
	args = parser.parse_args()
	
	if args.byte_limit_value < 0:
		parser.error("byte_limit_value cannot be less than 0.")
	if args.minutes > 60 or args.minutes<1:
		parser.error("minutes cannot be larger than 60 or less than 1.")

	while True: 
		if func.check_mem_used()>args.byte_limit_value:
			print(f"Initiating system monitoring each {args.minutes} minutes. Creating alert wall")
			func.cpu_rapport()
			func.mem_rapport()
			func.make_alert_wall()
			time.sleep(args.minutes*60)
		else:
			print("==> System's state is not critical. <==")
			print(f"This service checks the status of the system every {args.minutes} minuts.")
			print("==================================================================== \n")
			time.sleep(args.minutes*60)

