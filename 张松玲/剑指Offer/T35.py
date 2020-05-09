
# -*- coding:utf-8 -*-
class Solution:
    def GetNumberOfK(self, data, k):
        # write code here
        def getfirst(data,k):
            if len(data)<=0:
                return -1
            mid = len(data)//2
            if data[mid-1]<k and data[mid]==k:
                return mid
            if data[mid]<k:
                return mid + getfirst(data[mid+1:],k)
            else:
                return getfirst(data[:mid],k)

        def getlast(data,k):
            if len(data) == 1:
                return 0

            mid = len(data)//2
            if data[mid+1] > k and data[mid]==k:
                return mid
            if data[mid]<=k:
                return mid + 1 + getlast(data[mid+1:], k)
            else:
                return getlast(data[:mid],k)

        first = getfirst(data,k) if data[0] <= k else
        last = getlast(data,k)
        return last-first+1
a = Solution()
print a.GetNumberOfK([1,2,3,3,3,3,4,5],3)
print a.GetNumberOfK([3,3,3,3,3,3,4,5],3)