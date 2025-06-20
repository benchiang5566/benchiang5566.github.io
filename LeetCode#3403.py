## LeetCode 3403. Find the Lexicographically Largest String From the Box I

class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        if numFriends==1: return word   ## 碞だ 1 琿
        N = len(word)   ## ﹃穦∕﹚癹伴 i 璶眖秨﹍
        M = N - (numFriends - 1)
        ## 程﹃: N - (n-1) ㄤ (n-1) 常琌 1 ダ
        ans = word[0:M] ## 程娩程盽êダ
        for i in range(N):  ## –秨﹍ i
            ans = max(ans, word[i:i+M]) ## 眖 i 秨﹍程﹃琌
        return ans
