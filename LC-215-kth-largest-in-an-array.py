# Time:  O(n)
# Space: O(1)
#
# Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.
#
# For example,
# Given [3,2,1,5,6,4] and k = 2, return 5.

import random


class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int

        Notes:
        1. outmost while i<=j
        2. inner while predicate check i<=j then access value.
        3. Need to memorieze quick sort

        """

        # print("\nnew  nums={} k={}".format(nums,k))
        pivot_idx = random.randint(0, len(nums) - 1)
        nums[0], nums[pivot_idx] = nums[pivot_idx], nums[0]
        i, j = 1, len(nums) - 1
        while i <= j:
            while i <= j and nums[i] <= nums[0] : i += 1 # order matters!
            while i <= j and nums[j] >= nums[0] : j -= 1 # order matters!
            if i < j: nums[i], nums[j] = nums[j], nums[i]

        nums[j], nums[0] = nums[0], nums[j]
        if k == len(nums)  - j:
            return nums[j]
        elif k < len(nums) - j:
            return self.findKthLargest(nums[j + 1:], k)
        else:
            return self.findKthLargest(nums[:j], k- (len(nums)- j) )


if __name__ == '__main__':
    pass
    s = Solution()
    # ans = s.findKthLargest(nums=[0], k=1)
    # print(ans)
    #
    # ans = s.findKthLargest(nums=[-1,2,0], k=3)
    # print(ans)
    #
    # ans = s.findKthLargest(nums=[random.randint(-10,10) for _ in range(50)], k=3)
    # print(ans)

    # ans = s.findKthLargest(
    #     nums=[2,2,2,2,2,2,2,2,2,2,2,2], k=6)
    # print(ans)
    print("#"*80)
    ans = s.findKthLargest(
        nums=[2,1], k=1)
    print(ans)

    print("#" * 80)
    ans = s.findKthLargest(
        nums=[2,1], k=2)
    print(ans)

    print("#" * 80)
    ans = s.findKthLargest(
        nums=[7, 6, 5, 4, 3, 2, 1], k=5)
    print(ans)

    print("#" * 80)
    ans = s.findKthLargest(nums=[10, 2, -8, 6, 8, -6, -10, 9, 9, 9, 5, 1, -6, -3, 3, 10, 4, 5, 3, 4, -7, -5, 4, -3, -5, -9, 2, 7, -2, 4, -8, 9, -8, 5, 3, 3, -10, -10, -1, -2, -2, -7, -10, 3, -4, -8, -10, -4, 6, -5], k=3)
    print(ans)
