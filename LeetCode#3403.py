## LeetCode 3403. Find the Lexicographically Largest String From the Box I

class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        if numFriends==1: return word   ## �N�u�� 1 �q�A���W�Y�i
        N = len(word)   ## �r�ꪺ���סA�|�M�w�j�� i �n�q���}�l
        M = N - (numFriends - 1)
        ## �u�̪��v�i�઺�r�ꪺ����: N - (n-1) ��L (n-1) ���O 1 �Ӧr��
        ans = word[0:M] ## �̪��䪺�̱`���Ӧr��
        for i in range(N):  ## �C�ӥi�઺�}�l����l i
            ans = max(ans, word[i:i+M]) ## �q i �}�l�A�̪����r��A�O�_��j
        return ans
