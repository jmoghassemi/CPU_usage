import os  
from datetime import datetime
#####################################
####### Global Variables ############
date = datetime.now().strftime("%Y-%m-%d")
full_time = datetime.now().strftime("%H:%M:%S")

#####################################

def cpu_rapport():
 # When system memory usage is larger than the critical threshold, this function will be executed. This function logs the information about the proccesses running on the user's systm into cpu_[date].log, located at /etc/cpuUsage/report.  
  
        cpu_filename = '/etc/cpuUsage/report/cpu_' + date + '.log'
        with open(cpu_filename, "a+") as f:
            f.write(full_time + '\n')

            ps_output = os.popen('ps -o pid,user,%mem,command ax | grep -v PID | grep -v 0.0').read().splitlines()

            tmp_txt = ''

            for item in ps_output:
                    tx = item.split()
                    if tx[2] != '0.0':
                            wf = tx[0] + ',' + tx[1] + ',' + tx[2] + ','
                            if len(tx) > 3:
                                    for i in range(3, len(tx) - 1):
                                            tmp_txt += tx[i] + ' '
                                    wf += tmp_txt
                    f.write(wf + '\n')
            f.close()

def mem_rapport():
 # When system's memory usage is larger than the critical threshold, this function will be executed. This function logs the user's memory and swap information into mem_[date].log and swp_[date].log, located at /etc/cpuUsage/report.
  
 
        mem_filename = '/etc/cpuUsage/report/mem_' + date + '.log'
        swp_filename = '/etc/cpuUsage/report/swp_' + date + '.log'

        mem_output = os.popen('free -mw | grep Mem').read().split()
        swap_output = os.popen('free -mw | grep Swap').read().split()
        mem_output[0] = full_time
        swap_output[0] = full_time
        
        with open(mem_filename, "a+") as mf:
            mf.write(mem_output[0]+','+mem_output[1]+','+mem_output[2]+','+mem_output[3]+','+mem_output[6]+'\n')
            mf.close()
        
        with open(swp_filename, "a+") as sf:
            sf.write(swap_output[0]+','+swap_output[1]+','+swap_output[2]+','+swap_output[3]+'\n')
            sf.close()

def get_total_mem():
  total_raw_mem=os.popen('cat /proc/meminfo | grep MemTotal').read().split()
  return round(int(total_raw_mem[1])/1024)

def check_free_mem_per():
  mem_raw=os.popen('free -mw | grep Mem').read().split()
  free_mem_percent="{:.2}".format(int(mem_raw[3])/int(mem_raw[1]))
  return float(free_mem_percent)

def check_mem_used():
        mem_raw=os.popen('free -mw | grep Mem').read().split()
        return int(mem_raw[2])

def check_cpu():
  mpstat_raw=os.popen('mpstat | grep all').read().split()

def make_alert_wall():
        print(f"System total memory \033[1;36;40m {get_total_mem()}MB \033[0;37;40m")
        print(f"System memory usage \033[1;31;40m {check_mem_used()}MB \033[0;37;40m")
        print("Please check the report files in this path \n\t \033[1;32;40m /etc/cpuUsage/report/ \033[0;37;40m")
        print("======================================== \n")
