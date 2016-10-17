#! /bin/bash -ex

# Combine two A5 PDFs into one A4

if [ "$1" == "" ]; then
    echo Usage: $0 filename

    echo Example: $0 basic-functions/basic-functions-cs.pdf
else
    pdfjam --landscape --paper a4paper --nup 2x1 "$1" 1,1 -o combined-a4.pdf
fi
