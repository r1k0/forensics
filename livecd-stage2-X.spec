subarch: x86
version_stamp: 0.1
target: livecd-stage2
rel_type: default
profile: default/linux/x86/10.0
snapshot: 20130201
source_subpath: default/livecd-stage1-x86-0.1
portage_confdir: /etc/catalyst/forensics/portage

#livecd/bootargs: dokeymap
livecd/bootargs: nox
livecd/cdtar: /usr/lib/catalyst/livecd/cdtar/isolinux-elilo-memtest86+-cdtar.tar.bz2
livecd/fsscript: /etc/catalyst/forensics/fsscript.sh
livecd/fstype: squashfs
livecd/gk_mainargs: --lvm --dmraid --mdadm --makeopts=-j8
livecd/iso: livecd-x86-X-forenics-0.1.iso
#livecd/type: gentoo-release-minimal
#livecd/type: gentoo-release-livecd
livecd/type: generic-livecd
livecd/volid: Forensics 0.1 Linux x86
livecd/rcdel: keymaps|boot
livecd/motd: /etc/catalyst/forensics/motd
livecd/readme: /etc/catalyst/forensics/readme
#livecd/xdm: gdm
#livecd/xsession: xfce

boot/kernel: gentoo
boot/kernel/gentoo/sources: gentoo-sources
boot/kernel/gentoo/config: /etc/catalyst/forensics/kconfig-3.4.2-gentoo
boot/kernel/gentoo/use:
	-*
	alsa
	alsa_pcm_plugins_adpcm
	alsa_pcm_plugins_alaw
	alsa_pcm_plugins_asym
	alsa_pcm_plugins_copy
	alsa_pcm_plugins_dmix
	alsa_pcm_plugins_dshare
	alsa_pcm_plugins_dsnoop
	alsa_pcm_plugins_empty
	alsa_pcm_plugins_extplug
	alsa_pcm_plugins_file
	alsa_pcm_plugins_hooks
	alsa_pcm_plugins_iec958
	alsa_pcm_plugins_ioplug
	alsa_pcm_plugins_ladspa
	alsa_pcm_plugins_lfloat
	alsa_pcm_plugins_linear
	alsa_pcm_plugins_meter
	alsa_pcm_plugins_mmap_emul
	alsa_pcm_plugins_mulaw
	alsa_pcm_plugins_multi
	alsa_pcm_plugins_null
	alsa_pcm_plugins_plug
	alsa_pcm_plugins_rate
	alsa_pcm_plugins_route
	alsa_pcm_plugins_share
	alsa_pcm_plugins_shm
	alsa_pcm_plugins_softvol
	atm
	deprecated
	fbcon
	fbcondecor
	ipv6
	livecd
	loop-aes
	lvm1
	midi
	mng
	modules
	ncurses
	nls
	nptl
	nptlonly
	pam
	png
	portaudio
	readline
	socks5
	ssl
	truetype
	unicode
	usb

boot/kernel/gentoo/packages:
### These need to be added for software speech.
#	app-accessibility/espeakup
#	media-libs/alsa-oss
	media-sound/alsa-utils
#	net-dialup/globespan-adsl
#	net-wireless/hostap-utils
##	net-dialup/fritzcapi
##	net-dialup/fcdsl
#	sys-apps/pcmciautils

livecd/unmerge:
#	app-admin/eselect
#	app-admin/eselect-ctags
#	app-admin/eselect-vi
	app-admin/perl-cleaner
	app-admin/python-updater
	app-arch/cpio
#	dev-libs/gmp
#	dev-libs/libxml2
	dev-libs/mpfr
#	dev-python/pycrypto
	dev-util/pkgconfig
	perl-core/PodParser
	perl-core/Test-Harness
	sys-apps/debianutils
	sys-apps/diffutils
	sys-apps/groff
	sys-apps/man
	sys-apps/man-pages
	sys-apps/miscfiles
#	sys-apps/portage
#	sys-apps/sandbox
	sys-apps/texinfo
#	sys-devel/autoconf
#	sys-devel/autoconf-wrapper
#	sys-devel/automake
#	sys-devel/automake-wrapper
	sys-devel/binutils-config
	sys-devel/bison
	sys-devel/flex
#	sys-devel/gcc # This might be needed for software speech
#	sys-devel/gcc-config
#	sys-devel/gettext
#	sys-devel/gnuconfig
#	sys-devel/libtool
#	sys-devel/m4
#	sys-devel/make
#	sys-devel/patch
#	sys-libs/db
#	sys-libs/gdbm
	sys-libs/libkudzu
	sys-kernel/genkernel
	sys-kernel/gentoo-sources
	sys-kernel/linux-headers
	app-portage/gentoolkit

livecd/empty:
	/etc/cron.daily
	/etc/cron.hourly
	/etc/cron.monthly
	/etc/cron.weekly
	/etc/logrotate.d
	/etc/modules.autoload.d
	/etc/rsync
	/etc/runlevels/single
	/etc/skel
	/lib/dev-state
	/lib/udev-state
	/lib64/dev-state
	/lib64/udev-state
	/root/.ccache
	/tmp
	/usr/diet/include
	/usr/diet/man
	/usr/i?86-gentoo-linux-uclibc
	/usr/i?86-pc-linux-uclibc
	/usr/lib/X11/config
	/usr/lib/X11/doc
	/usr/lib/X11/etc
	/usr/lib/awk
	/usr/lib/ccache
#	/usr/lib/gcc-config
	/usr/lib/gconv
	/usr/lib/nfs
	/usr/lib/perl5/site_perl
	/usr/lib/portage
	/usr/lib/python2.2
	/usr/lib/python2.3
	/usr/lib/python2.4/test
	/usr/lib64/X11/config
	/usr/lib64/X11/doc
	/usr/lib64/X11/etc
	/usr/lib64/awk
	/usr/lib64/ccache
#	/usr/lib64/gcc-config
	/usr/lib64/gconv
	/usr/lib64/nfs
	/usr/lib64/perl5/site_perl
	/usr/lib64/portage
	/usr/lib64/python2.2
	/usr/lib64/python2.3
	/usr/lib64/python2.4/test
	/usr/local
	/usr/portage
	/usr/powerpc-unknown-linux-gnu
	/usr/powerpc64-unknown-linux-gnu
	/usr/share/aclocal
	/usr/share/baselayout
	/usr/share/binutils-data
	/usr/share/consolefonts/partialfonts
	/usr/share/consoletrans
	/usr/share/dict
	/usr/share/doc
	/usr/share/emacs
	/usr/share/et
#	/usr/share/gcc-data
	/usr/share/genkernel
	/usr/share/gettext
	/usr/share/glib-2.0
	/usr/share/gnuconfig
	/usr/share/gtk-doc
	/usr/share/i18n
	/usr/share/info
	/usr/share/lcms
	/usr/share/libtool
	/usr/share/locale
	/usr/share/man
	/usr/share/rfc
	/usr/share/ss
	/usr/share/state
	/usr/share/texinfo
	/usr/share/unimaps
	/usr/share/zoneinfo
	/usr/sparc-unknown-linux-gnu
	/usr/src
	/var/cache
	/var/empty
	/var/lib/portage
	/var/log
	/var/spool
	/var/state
	/var/tmp

livecd/rm:
	/usr/portage/* # Portage

	/boot/System*
	/boot/initr*
	/boot/kernel*
	/etc/*-
	/etc/*.old
	/etc/default/audioctl
	/etc/dispatch-conf.conf
	/etc/env.d/05binutils
#	/etc/env.d/05gcc
	/etc/etc-update.conf
	/etc/hosts.bck
	/etc/issue*
	/etc/genkernel.conf
	/etc/make.conf*
	/etc/make.globals
	/etc/make.profile
	/etc/man.conf
	/etc/resolv.conf
	/lib*/*.a
	/lib*/*.la
	/lib*/cpp
	/root/.bash_history
	/root/.viminfo
	/sbin/*.static
	/sbin/fsck.cramfs
	/sbin/fsck.minix
	/sbin/mkfs.bfs
	/sbin/mkfs.cramfs
	/sbin/mkfs.minix
	/usr/bin/addr2line
	/usr/bin/ar
	/usr/bin/as
	/usr/bin/audioctl
	/usr/bin/c++*
	/usr/bin/cc
	/usr/bin/cjpeg
	/usr/bin/cpp
	/usr/bin/djpeg
	/usr/bin/ebuild
	/usr/bin/emerge
	/usr/bin/elftoaout
	/usr/bin/f77
	/usr/bin/g++*
	/usr/bin/g77
#	/usr/bin/gcc*
	/usr/bin/genkernel
	/usr/bin/gprof
	/usr/bin/i?86-gentoo-linux-uclibc-*
	/usr/bin/i?86-pc-linux-*
	/usr/bin/jpegtran
#	/usr/bin/ld
	/usr/bin/libpng*
	/usr/bin/nm
	/usr/bin/objcopy
	/usr/bin/objdump
	/usr/bin/piggyback*
	/usr/bin/portageq
	/usr/bin/ranlib
	/usr/bin/readelf
	/usr/bin/repoman
#	/usr/bin/size
	/usr/bin/powerpc-unknown-linux-gnu-*
	/usr/bin/powerpc64-unknown-linux-gnu-*
	/usr/bin/sparc-unknown-linux-gnu-*
	/usr/bin/sparc64-unknown-linux-gnu-*
#	/usr/bin/strip
	/usr/bin/tbz2tool
	/usr/bin/xpak
	/usr/bin/yacc
	/usr/lib*/*.a
	/usr/lib*/*.la
	/usr/lib*/perl5/site_perl
#	/usr/lib*/gcc-lib/*/*/libgcj*
	/usr/sbin/archive-conf
	/usr/sbin/dispatch-conf
	/usr/sbin/emaint
	/usr/sbin/emerge-webrsync
	/usr/sbin/env-update
	/usr/sbin/fb*
	/usr/sbin/fixpackages
	/usr/sbin/quickpkg
	/usr/sbin/regenworld
	/usr/share/consolefonts/1*
	/usr/share/consolefonts/7*
	/usr/share/consolefonts/8*
	/usr/share/consolefonts/9*
	/usr/share/consolefonts/A*
	/usr/share/consolefonts/C*
	/usr/share/consolefonts/E*
	/usr/share/consolefonts/G*
	/usr/share/consolefonts/L*
	/usr/share/consolefonts/M*
	/usr/share/consolefonts/R*
	/usr/share/consolefonts/a*
	/usr/share/consolefonts/c*
	/usr/share/consolefonts/dr*
	/usr/share/consolefonts/g*
	/usr/share/consolefonts/i*
	/usr/share/consolefonts/k*
	/usr/share/consolefonts/l*
	/usr/share/consolefonts/r*
	/usr/share/consolefonts/s*
	/usr/share/consolefonts/t*
	/usr/share/consolefonts/v*
	/usr/share/misc/*.old

