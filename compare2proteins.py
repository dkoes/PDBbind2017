from Bio.PDB.PDBParser import PDBParser
from Bio.PDB.Polypeptide import is_aa
from Bio.PDB.Polypeptide import three_to_one
from Bio import pairwise2
import argparse
import sys

def getResidueString(structure):
    seq=''
    for model in structure:
        for residue in model.get_residues():
            if is_aa(residue.get_resname(), standard=True):
                seq+=(three_to_one(residue.get_resname()))
	    else:
		resname = residue.get_resname()
		if resname == 'HIE' or resname == 'HID': seq+=('H')
		elif resname == 'CYX' or resname == 'CYM': seq+=('C')
		else: seq+=('X')
    return seq

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-i','--input',type=str,required=True)
    args = parser.parse_args()
    p= PDBParser(PERMISSIVE=1,QUIET=1)

    f = open(args.input)
    for line in f:
        data= line.split("")
        firstName = data[0]
        secondName = data[1]
        firstHandle= ("/home/dkoes/PDBbind/general-set-with-refined/%s/%s_rec.pdb" %(firstName, firstName))
        secondHandle= ("/home/dkoes/PDBbind/general-set-with-refined/%s/%s_rec.pdb" %(secondName, secondName))
        firstStructure=p.get_structure(firstName,firstHandle)
        secondStructure=p.get_structure(secondName,secondHandle)
        firstSeq=getResidueString(firstStructure)
        secondSeq=getResidueString(secondStructure)

        score = pairwise2.align.globalxx(firstSeq, secondSeq, score_only=True)
        length= max(len(firstSeq), len(secondSeq))
        distance = (length-score)/length
        print firstName, secondName, distance
