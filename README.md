# benchiang5566.github.io
website test

![picture01](https://github.com/user-attachments/assets/8544d28d-a896-46c2-be39-6c946928a796)

## LeetCode 3403. Find the Lexicographically Largest String From the Box I

class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        if numFriends==1: return word   ## 就只分 1 段，全上即可
        N = len(word)   ## 字串的長度，會決定迴圈 i 要從哪開始
        M = N - (numFriends - 1)
        ## 「最長」可能的字串的長度: N - (n-1) 其他 (n-1) 都是 1 個字母
        ans = word[0:M] ## 最長邊的最常那個字母
        for i in range(N):  ## 每個可能的開始的格子 i
            ans = max(ans, word[i:i+M]) ## 從 i 開始，最長的字串，是否更大
        return ans
