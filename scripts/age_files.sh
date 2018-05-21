#!/bin/bash
scriptname=`basename $0`
scriptdir=`dirname $0`

BaseDir=$1
OlderThanDays=$2
AlsoDeleteDirectories=$3

usage()
{
    echo "Usage: $scriptname <BaseDir> <Num Days> [<Also Delete Dirs and Symlinks>]"
    echo ""
    echo "  BaseDir: All files under this dir will be deleted"
    echo "  Num Days: Delete files not accessed in Num Days (not created or modified, but accessed)"
    echo "  Also Delete Dirs and Symlinks: Specify anything as 3rd arg to cause this"
    echo ""
    echo "Eg.: $scriptname /tmp 10 --- Delete all files under /tmp not accessed in the last 10 days"
    echo "     $scriptname /tmp 10 dummy --- same as above, but also clean old dirs and symlinks"
}

if [ "x$BaseDir" = "x" ]; then
    echo "No base directory specified"
    usage
    exit 1
fi

if [ "x$OlderThanDays" = "x" ]; then
    echo "Specify how many days you want to keep files around"
    usage
    exit 1
fi

tmpwatch_exe=`which tmpwatch 2> /dev/null`
if [ "x$tmpwatch_exe" = "x" ]; then
    tmpwatch_exe=/usr/sbin/tmpwatch
fi

if [ ! -x $tmpwatch_exe ]; then
    echo "Unable to find the executable tmpwatch in path or in /usr/sbin"
    exit 1
fi

monthDay=`date +"0%0d%^b"`
#logfile=/tmp/age_files.${monthDay}
logfile=/tmp/age_files.log
errfile=/tmp/age_files.err
tmpwatch_options=""
tmpwatch_options="$tmpwatch_options --verbose"

if [ "x$AlsoDeleteDirectories" = "x" ]; then
    tmpwatch_options="$tmpwatch_options --nodirs --nosymlinks"
fi

tmpwatch_options="$tmpwatch_options --fuser"    # Attempt  to  use the /sbin/fuser
                                                # to see if a file is already open before 
                                                # removing it.

#tmpwatch_options="$tmpwatch_options --test"

if [ -f $logfile ]; then mv -f $logfile ${logfile}_bak; fi
if [ -f $errfile ]; then mv -f $errfile ${errfile}_bak; fi

hours=`expr $OlderThanDays \* 24`
echo "$tmpwatch_exe $tmpwatch_options $hours $BaseDir" > $logfile
#$tmpwatch_exe $tmpwatch_options $hours $BaseDir 2> $errfile | tee -a $logfile
$tmpwatch_exe $tmpwatch_options $hours $BaseDir 2> $errfile >> $logfile
cat $errfile >> $logfile
