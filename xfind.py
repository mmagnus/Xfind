#!/usr/bin/env python

import os
import sys

hosts = ['peyote2', 'malibu', 'maximus', 'mq']

args = sys.argv[1:]
#print args

if sys.argv[1] == '--update':
    os.system("ssh malibu /home/magnus/bin/xfind_update.sh")
    os.system("ssh peyote2 /home/magnus/bin/xfind_update.sh")
    os.system("ssh maximus /home/magnus/bin/xfind_update.sh")
    os.system("ssh mq /home/magnus/bin/xfind_update.sh")
    os.system("gupdatedb --localpaths='/Volumes/HD' --output='/Users/magnus/.local/hd.db'")
    os.system("gupdatedb --localpaths='/home/magnus' --output='/Users/magnus/.local/mac.db'")
    sys.exit()
    
if sys.argv[1] == '--test':
    os.system('xfind xfind_update.sh')
    sys.exit(1)

if sys.argv[1] == '--help' or sys.argv[1] == '-h':
    print("--test    to search for xfind_update.sh, should be here: " + str(hosts))
    print("--update  update: " + str(hosts) + " and HD")
    sys.exit(1)

os.system('toilet -f smmono9 xfind --filter gay')
 
#if '-l' in args:
if len(args) == 0:
    print 'local & hosts:', hosts
    sys.exit(1)

# local # does not work on my mac
#print '# locate'
#cmd = 'glocate -d ~/.locate-mac ' + ' '.join(args)
print '# mdfind'
cmd = 'mdfind -name ' + ' '.join(args) # options for locate as -b wont work here
os.system(cmd)

# Mac
print '# Mac'
cmd = 'glocate -d ~/.local/mac.db ' + ' '.join(args)
os.system(cmd)

# HD - search indexed external drives
print '# HD'
cmd = 'glocate -d ~/.local/hd.db ' + ' '.join(args)
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
