#!/bin/bash
 
if [ -z "$(which inotifywait)" ]; then
    echo "inotifywait not installed."
    echo "In most distros, it is available in the inotify-tools package."
    exit 1
fi
 
inotifywait --recursive --monitor --format "%e %w%f" \
--event modify,move,create,delete ./ \
| while read changed; do
    echo "reload"
done
