import subprocess
cmd = "muscle -align data/ATP8.fasta -output alignments/ATP8.txt"
results = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, text=True)


from Bio import AlignIO
alignment = AlignIO.read("alignments/ATP8.txt", "fasta")
print(alignment)

print("Alignment length %i" % alignment.get_alignment_length())
for record in alignment:
    print("%s - %s" % (record.seq, record.id))
print()

from Bio.Phylo.TreeConstruction import DistanceCalculator, DistanceTreeConstructor

calculator = DistanceCalculator('identity')
constructor = DistanceTreeConstructor(calculator, 'nj')
tree = constructor.build_tree(alignment)
print(tree)

from Bio import Phylo
tree.ladderize()
Phylo.draw(tree)