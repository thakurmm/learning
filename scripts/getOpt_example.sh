#!/bin/bash

# Check who owns the cvs directory.
# Options: 	getOpt_example [-a | -b <arg>] [-h] [args]
# Examples
#	Valid
#		./getOpt_example.sh 
#		./getOpt_example.sh -a
#		./getOpt_example.sh -ab abcd
#		./getOpt_example.sh -ab abcd xyz
#		./getOpt_example.sh -ab abcd xyz dddd
#		./getOpt_example.sh xyz dddd -a
#		./getOpt_example.sh xyz dddd -a xyz
#	Invalid
#		./getOpt_example.sh -ab
#	This is valid, but will yield a wrong result (bArg will be "a" and there will be no "-a" option)
#		./getOpt_example.sh -ba xyz


scriptName=`basename $0`
scriptDir=`dirname $0`
scriptDir=`cd $scriptDir;pwd`

logf="/tmp/${scriptName}.${USER}"

aOpt=0
bOpt=0
bArg=""
otherArgs=""

parseCmdline()
{
	USEROPTS=`getopt -o ab:h -n "$scriptName" -- "$@"`
	eval set -- "$USEROPTS"

	while [ 1 ]; do
		case "$1" in
			-a)	aOpt=1; shift ;;
			-b) bOpt=1; bArg=$2; shift 2 ;;
			-h) echo "Display help and exit"; exit ;;
			--) shift ; break ;;
			*)  echo "Display invalid opt error, help and exit"; exit ;;
		esac
	done

	otherArgs=$*
}

parseCmdline $*

echo "aOpt=$aOpt, bOpt=$bOpt bArg=$bArg, otherArgs=$otherArgs"
