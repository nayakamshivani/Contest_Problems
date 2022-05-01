'''2255. Count Prefixes of a Given String

You are given a string array words and a string s, where words[i] and s comprise only of lowercase English letters.

Return the number of strings in words that are a prefix of s.

A prefix of a string is a substring that occurs at the beginning of the string. A substring is a contiguous sequence of characters within a string.

Input: words = ["a","b","c","ab","bc","abc"], s = "abc"
Output: 3
Explanation:
The strings in words which are a prefix of s = "abc" are:
"a", "ab", and "abc".
Thus the number of strings in words which are a prefix of s is 3.'''

class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
        ps=[]
        s1=""
        count=0
        for i in range(0,len(s)):
            s1=s1+s[i]
            ps.append(s1)
        
       
        for i in range(0,len(words)):
            if(words[i] in ps):
                count=count+1
                
        return count
        
