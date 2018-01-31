#!/usr/bin/python3
import subprocess
import os
import logging

'''
The script will check if nfs filesystems in /etc/fstab are mounted or not. If not, it will try to mount the same. 
Any errors will be stored in log
'''
args=['findmnt','--fstab','-t' 'nfs']
logging.basicConfig(filename='mount.log',level=logging.DEBUG)
logger=logging.getLogger(__name__)
#args=['findmnt','-t','vfat']
args=['findmnt','--fstab','-t' 'nfs']
logger.info('Executing command {}'.format(" ".join(args)))
chk=subprocess.run(args,stdout=subprocess.PIPE,universal_newlines=True)
try:
    chk.check_returncode()
except SubprocessError:
    code=chk.returncode
    if code==1:
        logger.warning('NFS filesystem not found!')
    else:
        logger.error('Failed to execute shell command: {}'.format(" ".join(args)))
out=chk.stdout
out=out.split('\n')
for fs in out[1:]:
    fs=fs.split(' ')
    if os.path.isdir(fs[0]) and not os.path.ismount(fs[0]):
        try:
            args='mount {} {}'.format(fs[1],fs[0])
            chk=subprocess.run([args],stdout=subprocess.PIPE,universal_newlines=True)
            chk.check_returncode()
        except SubprocessError:
            logger.error('failed to mount NFS {} at {}'.format(fs[1]),fs[0])
