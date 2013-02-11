subarch: x86
version_stamp: 0.1
target: livecd-stage1
rel_type: default
profile: default/linux/x86/10.0
snapshot: 20130201
source_subpath: default/stage3-i486-20121213
portage_confdir: /etc/catalyst/forensics/portage

livecd/use:
	deprecated
	fbcon
	ipv6
	livecd
	loop-aes
	lvm1
	modules
	ncurses
	nls
	pam
	readline
	socks5
	ssl
	static-libs
	unicode
	xml

livecd/packages:
	app-accessibility/brltty
	app-admin/hddtemp
	app-admin/passook
	app-admin/pwgen
	app-admin/syslog-ng
	app-arch/unzip
	app-crypt/gnupg
	app-crypt/johntheripper
	app-editors/mg
	app-misc/screen
	app-misc/vlock
	app-portage/mirrorselect
	app-text/wgetpaste
	dev-util/strace
	dev-vcs/git
	dev-vcs/cvs
        app-portage/genlop
        app-portage/gentoolkit
        app-portage/gentoolkit-dev
        app-portage/layman
        app-portage/mirrorselect
        app-portage/portage-utils
        app-portage/ufed
        app-shells/bash-completion
        app-shells/gentoo-bashcomp
        app-shells/tcsh
        app-shells/zsh
        app-shells/zsh-completion
	app-editors/gvim
	app-editors/xemacs
        app-cdr/cdrkit
        app-cdr/dvd+rw-tools
        app-arch/unrar
        app-arch/unzip
	app-admin/gkrellm
	media-gfx/fbgrab
        media-video/mplayer
        net-analyzer/ettercap
        net-analyzer/netcat
        net-analyzer/nmap
        net-analyzer/snort
        net-analyzer/tcpdump
        net-analyzer/tcptraceroute
        net-analyzer/traceroute
        net-analyzer/wireshark
        net-firewall/iptables
        net-fs/cifs-utils
        net-fs/nfs-utils
#        net-fs/samba
        net-im/pidgin
        net-irc/irssi
        net-irc/xchat
        net-misc/bridge-utils
        net-misc/dhcpcd
        net-misc/iputils
        net-misc/ntp
        net-misc/rdate
        net-misc/rdesktop
        net-misc/tightvnc
        net-misc/vpnc
        net-misc/whois
        net-print/cups
        net-wireless/aircrack-ng
        net-wireless/airsnort
	net-dialup/mingetty
	net-dialup/pptpclient
	net-dialup/rp-pppoe
	net-fs/cifs-utils
	net-fs/nfs-utils
	net-irc/irssi
	net-misc/dhcpcd
	net-misc/iputils
	net-misc/ndisc6
	net-misc/ntp
	net-misc/rdate
	net-misc/rsync
	net-misc/vconfig
	net-proxy/dante
	net-proxy/ntlmaps
	net-proxy/tsocks
	net-wireless/b43-fwcutter
	net-wireless/ipw2100-firmware
	net-wireless/ipw2200-firmware
	net-wireless/prism54-firmware
	net-wireless/rfkill
	net-wireless/wireless-tools
	net-wireless/wpa_supplicant
	net-wireless/zd1201-firmware
	net-wireless/zd1211-firmware
	sys-apps/apmd
	sys-apps/busybox
	sys-apps/dmidecode
	sys-apps/ethtool
	sys-apps/fxload
	sys-apps/gptfdisk
	sys-apps/hdparm
	sys-apps/hwsetup
	sys-apps/iproute2
	sys-apps/memtester
	sys-apps/netplug
	sys-apps/sdparm
	sys-block/parted
	sys-block/partimage
	sys-block/qla-fc-firmware
	sys-firmware/iwl3945-ucode
	sys-firmware/iwl4965-ucode
	sys-firmware/iwl5000-ucode
	sys-fs/cryptsetup
	sys-fs/dmraid
	sys-fs/dosfstools
	sys-fs/e2fsprogs
	sys-fs/jfsutils
	sys-fs/lsscsi
	sys-fs/lvm2
	sys-fs/mac-fdisk
	sys-fs/mdadm
	sys-fs/multipath-tools
	sys-fs/ntfs3g
	sys-fs/reiserfsprogs
	sys-fs/xfsprogs
	sys-libs/gpm
	sys-power/acpid
        sys-process/htop
        sys-process/lsof
        sys-process/vixie-cron
	sys-process/iotop
	net-analyzer/iftop
	www-client/links
        www-client/firefox
        x11-base/xorg-x11
        x11-misc/xscreensaver
        x11-themes/gentoo-artwork-livecd
        xfce-base/xfce4-meta
	xfce-base/thunar
	net-analyzer/metasploit
	x11-terms/xfce4-terminal
	x11-terms/xterm
	net-p2p/rtorrent
	net-analyzer/yersinia
	net-analyzer/wireshark
	net-analyzer/gnu-netcat
	app-crypt/bcrypt
	net-analyzer/dnstracer
	net-dns/dnswalk
	net-analyzer/arping
	net-analyzer/fping
	net-analyzer/hping
	net-analyzer/netdiscover
	net-analyzer/fragroute
	net-analyzer/dsniff
	net-analyzer/sniffit
	app-emulation/wine
	net-analyzer/netcat
	sys-boot/unetbootin
	net-analyzer/etherape
	app-crypt/chntpw
	app-crypt/ophcrack-tables
	app-crypt/ophcrack
	app-crypt/hashcat-gui
	virtual/jdk

	# forensics only
        app-forensics/afflib
        app-forensics/aide
        app-forensics/air
        app-forensics/autopsy
        app-forensics/chkrootkit
        app-forensics/cmospwd
        app-forensics/examiner
        app-forensics/foremost
        app-forensics/galleta
        app-forensics/libewf
        app-forensics/lynis
        app-forensics/mac-robber
        app-forensics/magicrescue
        app-forensics/memdump
        app-forensics/openscap
        app-forensics/ovaldi
        app-forensics/pasco
        app-forensics/rdd
        app-forensics/rifiuti
        app-forensics/rkhunter
        app-forensics/scalpel
        app-forensics/sleuthkit
        app-forensics/unhide
        app-forensics/yasat
        app-forensics/zzuf

        # required for stage2
        lbzip2
