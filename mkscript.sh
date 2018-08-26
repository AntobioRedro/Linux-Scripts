#!/bin/bash
#title           :mkscript.sh
#description     :Creates an executable script.
#author          :pedro
#date            :20111101
#version         :0.1    
#==============================================================================

if [ -n "$1" ] && [ -n "$2" ] && [ -n "$3" ]; then
    title=$1
    description=$2
    version=$3
    autor=$(whoami)
    d=$(date)

    printf " #!/bin/bash \n #============================================================================== \n #title           :$title  \n #description     :$description \n #author          :$autor \n #date            :$d \n #version         :$version \n #=============================================================================="> "$title"
    
    chmod 744 "$title"
    exit 0
else
    echo "Usage: mkscript.sh name description version"
    exit 1
fi

