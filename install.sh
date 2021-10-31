#! /usr/bin/bash

source config.sh

if [[ ! -e $destinationDir ]]; then
	echo "${destinationDir} could not found. Start to creating."
	sudo -S mkdir -vp $destinationDir
else
	echo "${destinationDir} was exist."
fi

if [[ ! -f $destinationDir/$logName ]]; then
  sudo -S touch $destinationDir/$logName
	sudo -S bash -c 'date > $0/$1' $destinationDir $logName
	sudo -S bash -c 'echo "Application log created in $0/$1"' $destinationDir $logName
fi

if [[ ! -e $destinationDir/report ]]; then
	echo "${destinationDir}/report could not found. Start to creating."
	sudo -S mkdir -vp $destinationDir/report
	sudo -S chmod -R 777 $destinationDir/report
	sudo -s chmod -R +t $destinationDir/report
fi

if [[ ! -f $destinationDir/cpuUsage.py ]]; then
	echo "application was not find. Start to copy..."
	sudo -S cp -i $sourceDir/cpuUsage.py /etc/cpuUsage
	sudo -S cp -i $sourceDir/functions.py /etc/cpuUsage
fi

if [[ ! -f /etc/systemd/system/cpuUsage.service ]]; then
 sudo -S cp -i $sourceDir/cpuUsage.service /etc/systemd/system
 echo "CPU usage service copied to systemd." 
fi

sudo -S systemctl daemon-reload
echo "service daemon reloaded."
sudo -S systemctl enable cpuUsage.service
echo "Application service enabled."
sudo -S systemctl start cpuUsage.service
echo "Application service started."
echo "======================= Application service status ======================="
sudo -S systemctl status cpuUsage.service
