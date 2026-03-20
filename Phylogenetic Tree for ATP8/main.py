from Bio import SeqIO

import glob
import matplotlib.pyplot as plt

recs = { file_name: rec for file_name in glob.glob('data/*.fasta') for rec in SeqIO.parse(file_name, "fasta")}

# for file_name, rec in recs.items():
#     print(file_name)
#     print(rec.id)
#     print(repr(rec.seq))
#     print(len(rec))

sizes = [len(rec) for rec in recs.values()]

plt.hist(sizes, bins=20)
plt.title(
    "%i ATP8 sequences\nLengths %i to %i" % (len(sizes), min(sizes), max(sizes))
)
plt.xlabel("Sequence length (bp)")
plt.ylabel("Count")
plt.show()