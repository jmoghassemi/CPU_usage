#!/usr/bin/env bash

userName=`whoami`

sourceDir='/home/'${userName}'/CPU_usage'
destinationDir='/etc/cpuUsage'

logName='cpuUsage.log'

mailTo='user@example.com'

