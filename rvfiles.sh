 #!/bin/bash 
 #============================================================================== 
 #title           :rvfiles.sh  
 #description     :Recovers deleted files 
 #author          :pedro 
 #date            :dom ago 26 14:21:02 CDT 2018 
 #version         :0.1 
 #==============================================================================
 if [ -n "$1" ];
 then
    file=$1
    cd
    cd .local/share/Trash/files
    if [ ! -f "$file" ]
    then
        echo "$0: File '$file' not found."
    else
        echo "Recovering file '$file'"
        mv "$file" ~/
        rm "$file"
    fi
    exit 0
 else
    echo "Filename cannot be empty, please especify one"
    exit 1
 fi
