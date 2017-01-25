gource -1024x768 --seconds-per-day 1 --stop-position 1.0 --highlight-all-users --hide-filenames --output-framerate 60 --output-ppm-stream output.ppm --user-image-dir .git/avatar/  --title "Magic" --hide dirnames,filenames,usernames

ffmpeg -y -r 60 -f image2pipe -vcodec ppm -i output.ppm  -vcodec wmv1 -r 60 -qscale 0 out.wmv
