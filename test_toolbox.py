import toolbox

print(toolbox.transcribe('ACGT'))
print(toolbox.revcomp('AAAACGT'))

print(toolbox.translate('ATGTAA'))

s = 'ACGTGGGGGGCATATG'
print(toolbox.gc_comp(s))
print(toolbox.gc_skew(s), toolbox.gc_skew(toolbox.revcomp(s)))


print(toolbox.translate('AATGAAGTTGAGCGTTAAGGTCAAAATAACGCTTAAGGTATTGTTGAATAGGTTTAAGTCCCT'))