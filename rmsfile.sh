 #!/bin/bash 
 #============================================================================== 
 #title           :rmsfile.sh  
 #description     :Safely deletes files 
 #author          :pedro 
 #date            :dom ago 26 14:21:51 CDT 2018 
 #version         :0.1 
 #==============================================================================

if [ -n "$1" ];
 then
    file=$1
    if [ ! -f "$file" ]
    then
        echo "$0: File '$file' not found."
    else
        echo "Deleting file '$file'"
        > "$file"
        rm "$file"
    fi
    exit 0
 else
    echo "Filename cannot be empty, please especify one"
    exit 1
 fi
