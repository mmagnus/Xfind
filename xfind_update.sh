echo 'malibu...'
ssh malibu ~/bin/xfind_update.sh
echo 'peyote2...'
ssh peyote2 ~/bin/xfind_update.sh

export LOCATE_CONFIG="/Users/magnus/Dropbox/workspace/xfind/mac-locate.rc"
updatedb
