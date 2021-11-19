"""
<input>
abcd
xLLLyRnRB

<output>
abycnx


<input>
cubfwkrgtrvfpjmdcidudgqiidmplycpsduonnxjhsqwbdcfnfbsnsawxpljnpaguxwjmtstojqrouxdbywpqynonazbpbjjyhsl
LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLRRRRRywioqRRRnjRRBBBBRRRRRprlapcyhjfzvyhpabpRRLLRRRRieBBBBBBBBBLBBBBBtnvtLLLLLBBBBRlfRRwjnkLLLLRRRRRRRRRRlRRRRRRfowdzjhmwrxnswqBBRRRRRLLLLRRRRRRBcetnuubBBBBLuzwcpLRRRRRLLkvhmbRBBBRajabLLLLRRRRRRLLLLgbqicoBBBBmyesLLLLLRRBBBBBBwsdxfshRRRRLBBBBBfcfmaBBBBBBBBBBBBcrnimBBRRRRRRRRRRowiutRRRuahBBBRRRnLLLvzBBBRRRagfgLLLLLLLkmrBBLLLLRRLLLBBBBBnrfxLLLoxmougmmaLLLBBBBttkreRRRRLdodBBBBkpRRRRRRRBLLLLLdLLRRzgRRRRlsjbljwsBBBBRRLLLLLglnsvjmakrcRRRRkvfzBBRRRRRRRRRBBBBBBLLLLLRRRRRBBBBBBBBBRRRRBBdcRRBBccifcRRRRqfRRRRRRRRRRRRRRRRLLLLBBjowsRRRBRBRRRRLfipvplrjBRRRRRRRRRBRRRRRRRRRRskddBBBRBBBBBhygecszzaqlkLLRRRRRRLLLBBRRRRBBRRRRBBBBBBBBLLLLLRRRBBBLLLLLRRRyBBLLLRLLLLLLLLLLLLLBLBBBBBLLLLyzezmxiuaovuwlxeudauRRRRRgRRRRBBBBBLLLLLLLBBBpwvdcLsdwvRRRLLLepBBBBRRLLLRRRRBLLLLLBowRRRRLLLLLRRRRBBBBtBzuRRRmhdblkRbRRRRRRRRRwqhfnRRRRyfBBBBRRRRLLLLLRRRvzbLBRRRjjlwLLLLBBBmRRRRRRRRRRLodfntLLLRRRRRjsaRRRLLLLLxBecwrLLLLLBBRRRLLLLLLj

<output>
cubfwkywioqrgtfpjmdprlajlftnwjnkvtpdgqliidmplfowdzjhmwrxnsycpsduceuzwcptnkcrnabjhsqwbdnoxttkremmkprdzgfxtflglnsvjmakrcawdcccifcnpagqfuxwjyzezmxiuaovuwlxpwozucammhdblktbstsfipvplwqhfnrpnnvmjjjlwonecwrtjjsa
"""
from collections import deque
input_val = input()
command = list(input())

left = list(input_val)
right = deque()

for cmd in command:
    if cmd == 'L':
        if left:
            right.appendleft(left.pop())
    elif cmd == 'R':
        if right:
            left.append(right.popleft())
    elif cmd == 'B':
        if left:
            left.pop()
    else:
        left.append(cmd)

# answer question
print ("".join(left), end="")
print("".join(right))