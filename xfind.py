#!/usr/bin/env python

import os
import sys

hosts = ['peyote2', 'malibu', 'maximus']

args = sys.argv[1:]
#print args

os.system('toilet -f smmono9 xfind --filter gay')
 
#if '-l' in args:
if len(args) == 0:
    print 'hosts:', hosts
    sys.exit(1)
    
for h in hosts:
    print ('> ' + h)    
    cmd = 'ssh ' + h + ' ~/bin/xfind.sh ' + ' '.join(args)
    #print cmd
    os.system(cmd)
