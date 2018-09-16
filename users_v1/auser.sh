 #!/bin/bash 
 #============================================================================== 
 #title           :auser  
 #description     :This script can add users
 #author          :pedro 
 #date            :dom sep 16 12:17:26 CDT 2018 
 #version         :1.0
 #==============================================================================

echo -n "Enter a new user login and press [ENTER]: "
read login

echo -n "Enter a user name for "$login" and press [ENTER]: "
read username

echo -n "Enter a group for "$login" and press [ENTER]: "
read group

echo -n "Enter a home dir:scriptectory for "$login" and press [ENTER]: "
read home

groupadd $group

useradd -d $home -m -k /etc/skel -s /bin/sh -c $username -g $group $login
passwd $login 

echo "User danny added"



