'''
1.2.6
Code Challenge: Implement PatternCount (reproduced below).
Input: Strings Text and Pattern.
Output: Count(Text, Pattern).

PatternCount(Text, Pattern)
  count ← 0
  for i ← 0 to |Text| − |Pattern|
    if Text(i, |Pattern|) = Pattern
      count ← count + 1
  return count


'''
def PatternCount(text, pattern):
    count = 0
    for i in range(0, len(text)- len(pattern)+1):
        print(text[i : i+len(pattern)])
        if text[i : i+len(pattern)] == pattern:
            count += 1
    return count