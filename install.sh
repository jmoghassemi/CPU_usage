#! /usr/bin/env bash
source config.sh

if [[ ! -e $destinationDir ]]; then
    sudo -s mkdir -p $destinationDir
fi

if [[ ! -e $logDir ]]; then
    sudo -s mkdir -p $logDir
fi

if [[ ! -f $logDir/$logName ]]; then
	sudo -s touch $logDir/$logName
fi

if [[ ! -f /etc/systemd/system/cpuUsage.service ]]; then
	sudo -s cp $sourceDir/cpuUsage.service /etc/systemd/system
fi

if [[ ! -f /etc/cpuUsage/cpuUsage.py ]]; then
	sudo -s cp $sourceDir/cpuUsage.py /etc/cpuUsage
fi

sudo -s systemctl daemon-reload
sudo -s systemctl enable cpuUsage.service
