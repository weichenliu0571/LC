class Solution:
    def firstUniqChar(self, s: str) -> int:
         
         storage = defaultdict(int)

         for i in s:
            storage[i] += 1

         for i in range(len(s)):
             if storage[s[i]] == 1:
                 return i

         return -1
