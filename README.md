# CPU_usage
The third assignment.
Collaborator:
  Java Ein Moghassemi, 
  Hadi Taghilouei, 
  MohammadHossein Labafbashi

This program's purpose is to keep the load on CPU in check. Users are able to set a critical threshhold for CPU usage and how often this program should monitor the system. The inputs are in Mega Bytes and time given in minutes. Bellow you can find instructions on how to run this program. After the instructions, you will find a list of contents of the files in CPU_usage, followed by a short description of what each file does.   

HOW TO RUN THE PROGRAM:
	1) Execute the bash file "install.sh". Make sure install.sh is executable on 		your system by running this command first: chmod +x install.sh Then run this command in order to start the program: bash install.sh 
	
	2) Execute the python script "cpuUsage.py" with this command: python3 cpuUsge.py. This script has its own default values for the crtitical CPU usage threshold and how often the python script checks the CPU usage. These default values are set to 75% of CPU being used and a reccurring evaluation of the system every 3 minutes. These default values can be changed manually within the python script. Open cpuUsage.py in Vim and under the "Variable Definition" section you will find the "default_limit" and "default min" variables. You can change these values as you wish.    

The contents of CPU_usage are listed bellow, followed by a short description of what each file does.  

install.sh:
	$destinationDir: 
	$destinationDir/$logname:
	$destinationDir/report:
	$DestinationDir/cpuUsage.py:
	$sourceDir/cpuUsage.service /etc/systemd/system:
	
	install.sh creates a cpuUsage directory (/etc/cpuUsage).This directory 		has 3 sub-directories: 1)/etc/cpuUsage/cpuUsage.py
			       2)/etc/cpuUsage/cpuUsage.log
			       3)/etc/spuUsage/report	 	 
	
config.sh:
	userName=`whoami`

	sourceDir='/home/'${userName}'/CPU_usage'
	destinationDir='/etc/cpuUsage'

	logName='cpuUsage.log'

	mailTo='user@example.com'

cpuUasge.service:
	[Unit]
	Description=CPU usage report

	[Service]
	ExecStart=/usr/bin/python3 /home/paramont/CPU_usage/cpuUsage.py
	Restart=always

	[Install]
	WantedBy=multi-user.target

cpuUsage.py:
	default_limit: 75% of cpu usage
	default_min: 3 min

functions.py:
	


  
