class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2

        if len(A) > len(B):
            A, B = B, A

        l, r = 0, len(A) - 1
        leftPartSize = (len(A) + len(B)) // 2

        while True:
            i = (l + r) // 2
            j = leftPartSize - i - 2

            aleft = A[i] if i >= 0 else float('-inf')
            bleft = B[j] if j >= 0 else float('-inf')
            aright = A[i + 1] if (i+1) < len(A) else float('inf') 
            bright = B[j + 1] if (j+1) < len(B) else float('inf') 

            if aleft <= bright and bleft <= aright:
                res = 0
                if (len(A) + len(B)) % 2 == 0:
                    res = (max(aleft, bleft) + min(bright, aright)) / 2
                else:
                    res = min(bright, aright)
                return res
            elif aright > bright:
                r = i - 1
            else:
                l = i + 1

        return -1
        