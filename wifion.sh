cd /etc/wpa_supplicant/

echo "ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
update_config=1
country=IN
network={
        ssid="Nokia7.2"
        psk="aaaaaaaa"
        key_mgmt=WPA-PSK
}

network={
        ssid="PARIFLOWR41"
        psk="Jesus@7274"
        key_mgmt=WPA-PSK
        disabled=1
}
" >> wpa_supplicant.conf

cd ~
sudo /usr/bin/autohotspotN