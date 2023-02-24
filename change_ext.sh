###	byt filändelse från till exempel .EX till .ex	###
###	på alla filer i aktuell katalog 		###
###	linum-2-2					###
###	author: jgaforsberg gufo0047 gusfor-1 gufr22	###
###							###

#!/bin/bash
EXT=$1
ext=$2

if [ -z "$1" ] || [ -z "$2" ];
then echo "Skicka med argument i format: ./change_ext.sh [gammal filändelse] [ny filändelse] för att köra skriptet"
	
else 
for i in *.$EXT
	do
		mv -v "$i" "${i%.$EXT}.$ext"
	done;
fi;
