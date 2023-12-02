#!/usr/bin/env bash

TMPFILE=`mktemp`
for fn in $@; do
	echo "\`$fn\`" >> $TMPFILE
	echo >> $TMPFILE
	cat $fn | sed -e 's/^/    /' >> $TMPFILE 
done

# may need to modify the -selection
cat $TMPFILE | xclip -selection clipboard
rm $TMPFILE
