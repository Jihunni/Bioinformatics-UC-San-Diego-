#Reverse Complement Problem
'''
1.3.2
Given a nucleotide p, we denote its complementary nucleotide as p*. The reverse complement of a string Pattern = p1 … pn is the string Patternrc = pn* … p1* formed by taking the complement of each nucleotide in Pattern, then reversing the resulting string. We will need the solution to the following problem throughout this chapter:
Reverse Complement Problem: Find the reverse complement of a DNA string.
•	Input: A DNA string Pattern.
•	Output: Patternrc , the reverse complement of Pattern.
Code Challenge: Solve the Reverse Complement Problem.

'''

def complementSeq(InputSeq):
    #InputSeq is string; OutputSeq is string
    OutputSeq = [0] * len(InputSeq)
    for k in range(len(InputSeq)):
        if InputSeq[k] == 'A' : 
            OutputSeq[len(OutputSeq)-1-k] = 'T'
        elif InputSeq[k] == 'T' : 
            OutputSeq[len(OutputSeq)-1-k] = 'A'
        elif InputSeq[k] == 'G' : 
            OutputSeq[len(OutputSeq)-1-k] = 'C'
        elif InputSeq[k] == 'C' : 
            OutputSeq[len(OutputSeq)-1-k] = 'G'
    #To Convert character list into string
    OutputSeq = ''.join(OutputSeq)
    
    return OutputSeq #string
