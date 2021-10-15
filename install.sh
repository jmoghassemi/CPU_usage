#! /usr/bin/env bash


source config.sh

if [[ ! -e $destinationDir ]]; then
    sudo -s mkdir -p $destinationDir
fi

if [[ ! -e $logDir ]]; then
    sudo -s mkdir -p $logDir
fi

if [[ ! -e $destinationDir/report ]]; then
	sudo -s mkdir -p $destinationDir/report
fi

if [[ ! -f $logDir/$logName ]]; then
	sudo -s touch $logDir/$logName
fi

if [[ ! -f /etc/systemd/system/cpuUsage.service ]]; then
	sudo -s cp $sourceDir/cpuUsage.service /etc/systemd/system &>> sudo -s $logDir/$logName
	date >> sudo -s $logDir/$logName
	echo "CPU usage service copied to systemd." >> sudo -s $logDir/$logName
fi

if [[ ! -f /etc/cpuUsage/cpuUsage.py ]]; then
sudo -s cp $sourceDir/cpuUsage.py /etc/cpuUsage &>> sudo -s $logDir/$logName
fi

#while true 
#do
#	echo The current time is $(date)
#	sleep 1
#done

sudo -s systemctl daemon-reload &>> sudo -s $logDir/$logName
sudo -s systemctl enable cpuUsage.service &>> sudo -s $logDir/$logName
sudo -s systemctl start cpuUsage.service &>> sudo -s $logDir/$logName
