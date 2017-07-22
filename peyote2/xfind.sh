echo '>> locate'
locate -i -d ~/.local_locate.db $@
echo '>> archive'
locate -i -d ~/.archive_locate.db $@
