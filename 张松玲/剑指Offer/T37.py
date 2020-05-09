import re
class Solution:
    def isNumeric(self, s):
        # write code here
        return True if re.match(r"^([+-]?[0-9]*)?(\.[0-9]*)?([Ee]([+-]?[0-9]+))?$", s) else False


print Solution().isNumeric("12e")
