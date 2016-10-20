Xfind - find at eXternal machines and drives
-------------------------------------------------------------------------------

Xfind a new idea to do mmfinder (https://github.com/mmagnus/mmfinder). This is more like a concept so I encourge you to fork it if you wish and change it for setup.

![](doc/demo.gif)

server <-> client:

    magnus@malibu:~/bin$ cat xfind.sh
    locate -d ~/.local.db $@

    magnus@malibu:~/bin$ cat xfind_update.sh
    updatedb --require-visibility 0 -o  ~/.local.db -U /home/magnus;

and make dbs of external drives:

    updatedb --require-visibility 0 -o  ~/.hd.db -U /mmt/HD;

Good:

- fast!
- update under crontab on remote machines
- offline locate search for drives

Bad:

- you have to have access to machines to do a search

..

    export LOCATE_PATH="/home/magnus/.locate-mac"
