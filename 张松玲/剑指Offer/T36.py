# -*- coding:utf-8 -*-
class Solution:
    def StrToInt(self, s):
        # write code here
        def cheak(s):
            if s is not None and len(s) > 0:
                num = 0
                for i in s:
                    if "0" <= i and i <= "9":
                        num = num * 10 + int(i)
                    else:
                        return 0
            else:
                return 0
            pass

        s = list(s)
        if s is None or len(s) == 0:
            return 0

        f = 1
        if s[0] == "+":
            s = s[1:]
        elif s[0] == "-":
            s = s[1:]
            f = -1
        r = cheak(s)
        return f * r

a = Solution().StrToInt("123")