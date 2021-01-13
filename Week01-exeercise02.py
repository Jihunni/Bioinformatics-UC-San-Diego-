#Frequent Words Probelms : Find the most frequent k-mers in a string

'''
1.2.13
Code Challenge: Solve the Frequent Words Problem.
•	Input: A string Text and an integer k.
•	Output: All most frequent k-mers in Text.

-------------------------------------------
Sample Input:
ACGTTGCATGTCGCATGATGCATGAGAGCT
4

Sample Output:
CATG GCAT

'''

def FrequencyTable(text, k):
    #text is a string, k is a integer
    freqMap = {} #empty dictionary
    n = len(text) #integer
    
    for i in range(0, n-k+1): #from 0 to n-k+1
        pattern = text[i:i+k]
        if pattern in freqMap.keys():
            freqMap[pattern] += 1
        else :
            freqMap[pattern] = 1
    return freqMap

def BetterFrequentWords(text, k):
    frequentPatterns = [] #an array of strings of length 0
    freqMap = FrequencyTable(text, k)
    max_value = max(freqMap.values())
    #Get the key with a maximum value from a given dictionary
    for key, value in freqMap.items():
        if value == max_value:
            frequentPatterns.append(key)
    #frequentPatterns = list(freqMap.keys())[list(freqMap.values()).index(max_value)]
    return frequentPatterns