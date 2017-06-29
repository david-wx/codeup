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
        """

        pivot_idx = random.randint(0, len(nums) - 1)
        nums[0], nums[pivot_idx] = nums[pivot_idx], nums[0]
        i, j = 1, len(nums) - 1
        while i < j:
            print(f"start i={i}, j={j}, nums={nums}")
            while nums[i] <= nums[0] and i <= j: i += 1
            while nums[j] >= nums[0] and i <= j: j -= 1
            print(f"stop  i={i}, j={j}, nums={nums}")
            if i < j:
                nums[i], nums[j] = nums[j], nums[i]

        print(f"pivot i={i}, j={j}, nums={nums}")
        nums[j], nums[0] = nums[0], nums[j]
        print(f"final i={i}, j={j}, nums={nums}")


        # return 0
        if k == len(nums)  - j:
            return nums[j]
        elif k < len(nums) + 1 - i:
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

    ans = s.findKthLargest(
        nums=[2,1], k=1)
    print(ans)

    ans = s.findKthLargest(nums=[10, 2, -8, 6, 8, -6, -10, 9, 9, 9, 5, 1, -6, -3, 3, 10, 4, 5, 3, 4, -7, -5, 4, -3, -5, -9, 2, 7, -2, 4, -8, 9, -8, 5, 3, 3, -10, -10, -1, -2, -2, -7, -10, 3, -4, -8, -10, -4, 6, -5], k=3)
    print(ans)
