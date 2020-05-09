# -*- coding:utf-8 -*-
class Solution:

    def GetLeastNumbers_Solution(self, tinput, k):
        # write code here
        def mink(tinput, k):
            current = tinput[0]
            i = 1
            j = len(tinput) - 1
            while i < j:
                while i <= len(tinput) - 1 and tinput[i] <= current:
                    i += 1
                while j > 0 and tinput[j] > current:
                    j -= 1
                if j > i:
                    tinput[i], tinput[j] = tinput[j], tinput[i]
                    i += 1
                    j -= 1
                pass
            tinput[0], tinput[i-1] = tinput[i-1], tinput[0]

            if i == k:
                return sorted(tinput[:i])
            if i > k:
                return mink(tinput[:i], k)
            if i < k:
                return sorted(tinput[:i] + mink(tinput[i:], k - i))

        if k > len(tinput) or k <= 0:
            return []
        result = mink(tinput, k)
        return result

    pass

print Solution().GetLeastNumbers_Solution([8, 7, 6, 5, 4, 3, 2, 1], 4)
