#! /usr/bin/env python3

########### Import Section #####################
import os
import sys
import argparse
import time

########## Variable Definition ################
default_limit = 60.0
default_min=3

######### Function Definition ################
def get_total_mem():
	total_raw_mem=os.popen('cat /proc/meminfo | grep MemTotal').read().split()
	return int(total_raw_mem[1])/1024/1024

def check_free_mem_per():
  mem_raw=os.popen('free -mw | grep Mem').read().split()
  free_mem_percent="{:.2}".format(int(mem_raw[3])/int(mem_raw[1]))
  print(f"Total Memory: {mem_raw[1]}")
  print(f"Free Memory: {mem_raw[3]}")
  print(f"Free Memory Percent: {free_mem_percent}%")
  print("#############################################")
  return float(free_mem_percent)

def check_cpu():
	mpstat_raw=os.popen('mpstat | grep all').read().split()
	print(f"IO wait %: {mpstat_raw[5]}")
	print(f"Idle %: {mpstat_raw[11]}")
	
########## Main Section ####################
if __name__ == "__main__":
    
	parser = argparse.ArgumentParser(description='CPU usage and Memory check. This program can using a serviced.')
	
	parser.add_argument('byte_limit_value', type=float, nargs='?', help=f'specifies when the script should respond (create alert sound and write status report). \n Default value for this action is 60%% of {int(get_total_mem())} GB.\n Accepted value between 10 to 99.9', default=default_limit)

	parser.add_argument('minutes', type=int, nargs='?', help='indicates at what intervals in minutes the script should check CPU usage.\n Default value is 3 minutes. \nAccepted value between 1 to 60.', default=default_min)
	
	args = parser.parse_args()
	
	print("Argument values:")
	print(args.byte_limit_value)
	print(args.minutes)

	if args.byte_limit_value > 99.99 or args.byte_limit_value < 0:
		parser.error("byte_limit_value cannot be larger than 99.99 and less than 0.")
	if args.minutes > 60 or args.minutes<1:
		parser.error("minutes cannot be larger than 60 and less than 1.")

	while check_free_mem_per()>args.byte_limit_value:
		print(f"Start to monitor system each {args.minutes} minutes. make alert wall")
		time.sleep(args.minutes*60)
