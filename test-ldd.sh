IFS=:;for BINDIR in $PATH; do ldd $BINDIR/*|grep "not found"|sort -u;done
