import os
infile = open('dock180.txt', 'r')
string = infile.readline()
    
while string !=' ':
	string = string[0:4]
	dockedItem = "/home/dkoes/PDBbind/general-set-except-refined/"+string + "/" + string + "_docked.sdf.gz"
	cmd1 = ("gninatyper " + dockedItem)
	os.system(cmd1)
	print(string)
	string = infile.readline()

infile.close()
