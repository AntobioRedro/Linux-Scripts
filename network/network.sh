#!/bin/sh

ifdown wlan0

rm /etc/wpa_supplicant/wpa_supplicant.conf
touch /etc/wpa_supplicant/wpa_supplicant.conf
echo 'ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev' >> /etc/wpa_supplicant/wpa_supplicant.conf
echo 'update_config=1' >> /etc/wpa_supplicant/wpa_supplicant.conf
wpa_passphrase $1 $2 >> /etc/wpa_supplicant/wpa_supplicant.conf

ifup wlan0
