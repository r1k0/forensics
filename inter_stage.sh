#!/bin/bash

TMPDIR=/var/tmp/catalyst/tmp/default/livecd-stage1-x86-0.1

#cp -r /usr/portage $TMPDIR/usr
#chroot $TMPDIR /usr/bin/emerge modutils -C

#cat $TMPDIR/etc/init.d/autoconfig | grep -v "xdm)" > $TMPDIR/etc/init.d/.autoconfig
#mv $TMPDIR/etc/init.d/.autoconfig $TMPDIR/etc/init.d/autoconfig

cp -r /pentest $TMPDIR
cp  /etc/catalyst/forensics/test-ldd.sh $TMPDIR/root
