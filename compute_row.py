from Bio.PDB.PDBParser import PDBParser
from Bio.PDB.Polypeptide import is_aa
from Bio.PDB.Polypeptide import three_to_one
from Bio import pairwise2
import argparse
import sys
import glob

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
    #args = parser.parse_args()
    p= PDBParser(PERMISSIVE=1,QUIET=1)
    print str(sys.argv[1])
    #name = sys.argv[1]
    name = parser.parse_args()
    handle = ("/home/dkoes/PDBbind/general-set-with-refined/%s/%s_rec.pdb" %(name, name))
    structure = p.get_structure(name, handle)
    seq=getResidueString(structure)

    for secondHandle in glob.glob('/home/dkoes/PDBbind/general-set-with-refined/*/*_rec.pdb'):
        secondName = secondHandle[50:54]
        secondStructure = p.get_structure(secondName, secondHandle)
        score = pairwise2.align.globalxx(seq, secondSeq, score_only=True)
        length= max(len(seq), len(secondSeq))
        distance = (length-score)/length
        print distance
