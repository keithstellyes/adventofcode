BEGIN {
	RS = "\n\n";
	FS = "\n";
	MAX=-1;
}

{
	SUM=0;
	for(i=1; i<=NF; i++) {
		SUM += $i;	
	}
	if(SUM > MAX) MAX=SUM
}

END {
	print MAX
}
