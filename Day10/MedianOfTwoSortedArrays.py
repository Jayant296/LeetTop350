'''
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).
'''
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)
        total = m+n
        half = total//2

        st, end = 0, m

        while True:
            cut1 = (st+end)//2
            cut2 = half - cut1

            l1 = nums1[cut1-1] if cut1 > 0 else float('-inf')
            r1 = nums1[cut1] if cut1 < m else float('inf')

            l2 = nums2[cut2-1] if cut2 > 0 else float('-inf')
            r2 = nums2[cut2] if cut2 < n else float('inf')

            # correct partition
            if l1 <= r2 and l2 <= r1:

                if total % 2:
                    return min(r1,r2)
                
                return (max(l1,l2) + min(r1,r2))/2
            
            elif l1 > r2:
                end = cut1-1
            
            else:
                st = cut1+1
            
        