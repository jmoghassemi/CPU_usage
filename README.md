# CPU_usage
The third assignment.
Collaborators:
  Java Ein Moghassemi, 
  Hadi Taghilouei, 
  MohammadHossein Labafbashi

This program's purpose is to keep the load on a computer's CPU in check, using a python script. The python script accepts two inputs from its user: 1) a critical threshold of memory usage, given in Mega Bytes and 2) the time intervals between each session of monitoring the system, given in minutes, when that critical threshold has been surpassed. In order to improve the user's experience, two bash scripts have been included in this project (config.sh and install.sh). They automatically copy files and create directories that are essential to this program, therefore minimizing any manual adjustments. 
Bellow you can find instructions on how to run this program, and also, a table of contents that explains the inner workings of this program in more detail.


HOW TO RUN THE PROGRAM:
1) The first step is to clone this program from Github onto your own computer. Run this command on your terminal and the project will be cloned on your system: 
git clone git@github.com:jmoghassemi/CPU_usage.git
  
2) The developers of this program have assumed that the user will clone this project onto their "/home" directory. Therefore, the default settings of this program are configured as such. If you decide to clone this program into another directory on your system, then before any testing, you must first provide that address/absolute path to the bash script "config.sh". In "config.sh" set the variable "sourceDir" equal to the path where the project is cloned.
=> sourceDir = 'address of the directory where the project is cloned'

Once "sourceDir" has been set to the correct path, you can execute the bash script "config.sh" using either of these two commands: "./config.sh" or "bash config.sh". Failing to set "sourceDir" equal to the path where the project is cloned will stop this program from running properly.	
    
3) Next, execute the bash script "install.sh" by either of these commands "./install.sh" or "bash install.sh". This script creates multiple directories on your system that are going to be used by the program later on. Make sure install.sh is executable on your system by running this command first: "chmod +x install.sh". (for more information regarding "install.sh" please refer to the table of contents bellow).

4) After succesfuly running the "install.sh" script, the user can test the program. Execute the python script "cpuUsage.py" with this command and give it your inputs: "python3 cpuUsge.py [integer for MB] [integer for min]. You can also run the python script without any inputs since it has been assigned default arguments. These default values are set to 75 MB of memory being used and a reccurring evaluation of the system every 3 minutes. 
There are other ways to input your arguments into cpuUsage.py. For example, you can open the service file cpuUsage.service in vim and provide the arguments as such: "ExecStart=/usr/bin/python3 /home/paramont/CPU_usage/cpuUsage.py [integer for MB] [integer for min]". Or open cpuUsage.py in Vim and under the "Variable Definition" section you will find the "default_limit" and "default min" variables. You can change these values as you wish. 
After the cpuUsage.py has been executed, the user's system will be constantly monitored and once the critical threshold is reached, three report files will be generated in this address: '/etc/cpuUsage/destinationDir/report'. These files are "cpu_[date].log", "mem_[date].log", and "swap_[date].log". Here you can find what each entry represents in each file.  

cpu_date.log: 1) pid 2) user 3) %mem 4) command
mem_date.log: 1) total Mem (mebibytes) 2) used Mem (mebibytes) 3) free Mem (mebibytes) 4) shared (mebibytes)
swap_date.log: 1) total 2) used 3) free 
  
TABLE OF CONTENTS

config.sh:
In a nutshell, this bash script is created so that any user can change certain components of this program more conviniently. For example, the script enables the program to recognize the user's machine's name. It enables the user to change the paths of the files that are going to be created by install.sh to whatever path they desire, change the name of the log file to any name the user sees fit, and it also stores the user's email so it can later email the report file to them. 

install.sh:
This bash script creates mutiple directories and files on the user's computer. It imports the "config.sh" bash script and it makes a directory "destinationDir" with the path address "/etc/cpuUsage", where the cpuUsage.py and functions.py will be copied. It makes a directory called "report" within "destinationDir". This is where the system's report file will be saved once it has gone over the critical threshold. "install.sh" also copies the service file "cpuUsage.service" on the user's computer, located at "/etc/systemd/system". 

cpuUsage.py:
This is the python script that will moniter the user's system once executed.

functions.py:
cpuUsage.py utilizes this script and it imports all the required functions from it.

cpuUsage.service:
This is a customized service file created explicitly for this program. A version of it is copied onto the user's "/etc/systemd/system" directory. It enables the user to run this program as a systemd service, and it accepts the [MB] threshold and the [min] arguments from the user.  


  
