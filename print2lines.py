#!/usr/bin/python
# -*- coding: utf-8 -*-

###	enkelt pythonskript för att iterera genom filer	###
###	i en angiven sökväg samt skriva ut delar av dess###
###	innehåll till stdout				###
###							###
###	author: jgaforsberg gufo0047 gusfor-1 gufr22	###
###							###

# för att hämta argument för sökväg
from sys import argv
# för att hämta filer i sökvägen
import glob

# undantagshantering vid felangiven sökväg som ger feedback i exceptblocket
try:
	rev_s = argv[1][::-1] # reversera angiven sökväg för att använda i if-villkor
	# testa om sökvägen är användbar genom att se om sista elementet i argv[0] är '/'
	if rev_s[0] == '/':
		# skriv ut sökvägen
		print('Angiven sökväg: '+argv[1]+'\n')
		# skriv ut .txt-filer i sökvägen
		print 'Filer i sökväg:',
		print(glob.glob(argv[1]+'*.txt'))
		print
		#iterera genom .txt-filerna i angiven sökväg
		for file in glob.glob(argv[1]+'*.txt'):
			f1 = open(file, 'r') # läser filerna som unicode
			print (f1.name+'\n') # skriver ut filnamnet
			text = f1.readlines() # sparar filinnehållet i en lista där varje element utgörs av en rad
			f1.close() # stänger den lästa filen
			print(text[0] + text[1]) # skriver ut de två första raderna av listan
	else:
		print('Ange sökväg i relativt eller absolutformat enligt path/to/dir/ eller ../path/to/dir/ eller ./dir/') # feedback om sökvägen är felskriven
except:
	print('Ange sökväg vid körning av skriptet i relativt eller absolutformat enligt path/to/dir/ eller ../path/to/dir/ eller ./') # feedback om argument saknas

###	pseudokod utkast				####

#path = read user input
#files = txt-files in dir

#for(.txt files in path)
#	file = filename
#	filecontent = filecontent.readlines()
#	print(file)
#	print(filecontent)
