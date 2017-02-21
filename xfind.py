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

# local # does not work on my mac
#print '# locate'
#cmd = 'glocate -d ~/.locate-mac ' + ' '.join(args)
print 'mdfind'
cmd = 'mdfind -name ' + ' '.join(args) # options for locate as -b wont work here
os.system(cmd)

# HD - search indexed external drives
print '# HD'
cmd = 'glocate -d ~/.locate-hd ' + ' '.join(args)
os.system(cmd)

# run xfind remotely to find your shit
print '# locate (global) malibu'
cmd = 'ssh malibu locate ' + ' '.join(args)
os.system(cmd)

# run xfind remotely to find your shit
print '# locate (global) peyote'
cmd = 'ssh peyote2 locate ' + ' '.join(args)
os.system(cmd)

for h in hosts:
    print ('# ' + h)    
    cmd = 'ssh ' + h + ' ~/bin/xfind.sh ' + ' '.join(args)
    #print cmd
    os.system(cmd)
