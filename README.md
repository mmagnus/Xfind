xfind - find at remote machines
-------------------------------------------------------------------------------
xfind:

![](doc/demo.gif)

server <-> client:

    magnus@malibu:~/bin$ cat xfind.sh
    locate -d ~/.local.db $@

    magnus@malibu:~/bin$ cat xfind_update.sh
    updatedb --require-visibility 0 -o  ~/.local.db -U /home/magnus;

Good:

- fast!
- update under crontab on remote machines
- offline locate search for drives

Bad:

- you have to have access to machines to do a search
