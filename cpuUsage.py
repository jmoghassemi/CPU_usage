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
    
	parser = argparse.ArgumentParser(description='CPU usage and Memory check. This program can using a serviced.')
	
	parser.add_argument('byte_limit_value', type=int, nargs='?', help=f'specifies when the script should respond in MB (create alert sound and make status report). \n Default value for this action is 75%% of {int(func.get_total_mem())} GB.\n Accepted value is integer and possitive number in MB.', default=default_limit)

	parser.add_argument('minutes', type=int, nargs='?', help='indicates at what intervals in minutes the script should check CPU usage.\n Default value is 3 minutes. \nAccepted value between 1 to 60.', default=default_min)
	
	args = parser.parse_args()
	
	if args.byte_limit_value < 0:
		parser.error("byte_limit_value cannot be less than 0.")
	if args.minutes > 60 or args.minutes<1:
		parser.error("minutes cannot be larger than 60 and less than 1.")

	while True: 
		if func.check_mem_used()>args.byte_limit_value:
			print(f"Start to monitor system each {args.minutes} minutes. make alert wall")
			func.cpu_rapport()
			func.mem_rapport()
			func.make_alert_wall()
			time.sleep(args.minutes*60)
		else:
			print("==> System is in normal mode and healthy. <==")
			print(f"This service check status of system every {args.minutes} minuts.")
			print("==================================================================== \n")
			time.sleep(args.minutes*60)

