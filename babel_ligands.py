import os
infile = open('Problem_Ligands', 'r')
string = infile.readline()
    
while string !=' ':
	string = string[0:3]
	smiItem = "/home/dkoes/PDBbind/general-set-except-refined/"+string + "/" + string + "_lig.smi"
	sdfItem = "/home/dkoes/PDBbind/general-set-except-refined/"+string + "/" + string + "_lig.sdf"
	cmd1 = ("babel --gen3D " + smiItem +" " + sdfItem)
	os.system(cmd1)
	string = infile.readline()
	break

infile.close()
