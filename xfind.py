#!/usr/bin/env python

import os
import sys

hosts = ['peyote2', 'malibu', 'maximus']

args = sys.argv[1:]
#print args

os.system('toilet -f smmono9 xfind --filter gay')
 
#if '-l' in args:
if len(args) == 0:
    print 'local & hosts:', hosts
    sys.exit(1)

# local
print '> locate'
cmd = 'locate ' + ' '.join(args)
os.system(cmd)

# HD
print '> HD'
cmd = 'locate -d ~/.locate-hd ' + ' '.join(args)
os.system(cmd)

for h in hosts:
    print ('> ' + h)    
    cmd = 'ssh ' + h + ' ~/bin/xfind.sh ' + ' '.join(args)
    #print cmd
    os.system(cmd)
