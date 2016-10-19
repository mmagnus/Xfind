rm ~/bin/xfind
#ln -s `pwd`/xfind.sh ~/bin/xfind
ln -s `pwd`/xfind.py ~/bin/xfind
rm  ~/bin/xfind_update
ln -s `pwd`/xfind_update.sh ~/bin/xfind_update
# HD
if [ -f ~/bin/xfind_update_hd ]; then
    rm ~/bin/xfind_update_hd
fi
ln -s `pwd`/xfind_update_hd.sh ~/bin/xfind_update_hd
