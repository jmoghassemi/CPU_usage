#! /usr/bin/bash

source config.sh

if [[ ! -e $destinationDir ]]; then
	echo "${destinationDir} could not be found. Starting to create the directory."
	sudo -S mkdir -vp $destinationDir
else
	echo "${destinationDir} already exists."
fi

if [[ ! -f $destinationDir/$logName ]]; then
  sudo -S touch $destinationDir/$logName
	sudo -S bash -c 'date > $0/$1' $destinationDir $logName
	sudo -S bash -c 'echo "Application log created on $0/$1"' $destinationDir $logName
else
	echo "${destinationDir}/${logName} already exists."
fi

if [[ ! -e $destinationDir/report ]]; then
	echo "${destinationDir}/report could not be found. Starting to create the directory."
	sudo -S mkdir -vp $destinationDir/report
	sudo -S chmod -R 777 $destinationDir/report
	sudo -s chmod -R +t $destinationDir/report
else
	echo "${destinationDir}/report already exists."
fi

if [[ ! -f $destinationDir/cpuUsage.py ]]; then
	echo "cpuUsage.py could not be found. Starting to copy..."
	sudo -S cp -iv $sourceDir/cpuUsage.py $destinationDir
	sudo -S cp -iv $sourceDir/functions.py $destinationDir
else
	echo "cpuUsage.py already exists."
fi

if [[ ! -f /etc/systemd/system/cpuUsage.service ]]; then
 sudo -S cp -iv $sourceDir/cpuUsage.service /etc/systemd/system
 echo "CPU usage service has been copied to systemd." 
else
	echo "CPU usage service already exists."
fi

sudo -S systemctl daemon-reload
echo "service daemon reloaded."
sudo -S systemctl enable cpuUsage.service
echo "Application service enabled."
sudo -S systemctl start cpuUsage.service
echo "Application service started."
echo "======================= Application Service Status ======================="
sudo -S systemctl status cpuUsage.service
