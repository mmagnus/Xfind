xfind - find at remote machines
-------------------------------------------------------------------------------

    magnus@malibu:~/bin$ cat xfind.sh
    locate -d ~/.locate.db $@

    magnus@malibu:~/bin$ cat xfind_update.sh
    updatedb --require-visibility 0 -o  ~/.local.db -U /home/magnus;
