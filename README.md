# CPU_usage
The third assignment.
Collaborator:
  Java Ein Moghassemi, 
  Hadi Taghilouei, 
  MohammadHossein Labafbashi

This program's purpose is to keep the load on CPU in check. Users are able to set a critical threshhold for CPU usage and how often this program should monitor the system. The inputs are in Mega Bytes and time given in minutes. Bellow you can find instructions on how to run this program. After the instructions, you will find a list of contents of the files in CPU_usage, followed by a short description of what each file does.   

HOW TO RUN THE PROGRAM:
1) Execute the bash file "install.sh". Make sure install.sh is executable on your system by running this command first: chmod +x install.sh Then run this command in order to start the program: bash install.sh 
	
2) Execute the python script "cpuUsage.py" with this command: python3 cpuUsge.py. This script has its own default values for the crtitical CPU usage threshold and how often the python script checks the CPU usage. These default values are set to 75% of CPU being used and a reccurring evaluation of the system every 3 minutes. These default values can be changed manually within the python script. Open cpuUsage.py in Vim and under the "Variable Definition" section you will find the "default_limit" and "default min" variables. You can change these values as you wish.    

The contents of CPU_usage are listed bellow, followed by a short description of what each file does.  

install.sh:
This bash script creates a directory called "destinationDir" on your system. The path to this directory is: /etc/cpuUsage. Then it creates two files within this directory: 1)logname and 2)report. "logname" keeps track of ... and "report" is where this program will save the details of your system's status once your system has exceeded the critical threshold of CPU usage. 
This bash script will also copy the cpuUsage.py script in the "destinationDir" directory. It also copies the service file that is respinsoble for monitoring your system in this path: /etc/systemd/system
	
	// $destinationDir: 
	// $destinationDir/$logname:
	// $destinationDir/report:
	// $DestinationDir/cpuUsage.py:
	// $sourceDir/cpuUsage.service /etc/systemd/system:
	
		 	 
	
config.sh:
In a nutshell, this bash script is created so that any user can change certain components of this program more conviniently. For example, the script enables the program to recognize the user's machine's name. It enables the user to change the paths of the files that are going to be created by install.sh to whatever path they desire, change the name of the log file to any name the user sees fit, and it also stores the user's email so it can later email the report file to them. Alternatively, by modifying the config.sh script, the user can overcome the hassel of interacting with the more complex file of install.sh.
	// userName=`whoami`

	// sourceDir='/home/'${userName}'/CPU_usage'
	// destinationDir='/etc/cpuUsage'

	// logName='cpuUsage.log'

	// mailTo='user@example.com'

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
	


  
