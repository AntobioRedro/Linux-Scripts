 #!/bin/bash 
 #============================================================================== 
 #title           :auser  
 #description     :This script can add users, quotas and sudo rights
 #author          :pedro 
 #date            :dom sep 16 12:17:26 CDT 2018 
 #version         :3.0
 #==============================================================================

echo -n "Enter a new user login and press [ENTER]: "
read login

echo -n "Enter a user name for "$login" and press [ENTER]: "
read username

echo -n "Enter a group for "$login" and press [ENTER]: "
read group

echo -n "Enter a home directory for "$login" and press [ENTER]: "
read home

groupadd $group

useradd -d $home -m -k /etc/skel -s /bin/sh -c $username -g $group $login
passwd $login 

echo -n "Add quota for "$login"? (y/n)"
read response
case "$response" in
    [yY][eE][sS]|[yY]) 
        echo -n "Enter the soft quota for "$login" and press [ENTER]:"
        read softquota
        
        echo -n "Enter the hard quota for "$login" and press [ENTER]: "
        read hardquota
        
        setquota -u $login $softquota $hardquota 0 0 /
        
        echo -n "User "$login" added with quotas"
        ;;
    *)
        echo -n "User "$login" added"
        ;;
esac

echo -n " Enable sudo rights? (y/n) \n"
read response
case "$response" in
    [yY][eE][sS]|[yY]) 
        sudo adduser $login sudo"$login"
        echo -n "Sudo rights granted for user "$login" "
        ;;
    *)
        echo -n "Sudo rights not granted for user "$login" "
        ;;
esac
