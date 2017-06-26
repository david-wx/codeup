class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = {}
        for idx, it in enumerate(nums):
            if it in d:
                return idx, d[it]
            else:
                d[target - it] = idx

if __name__ == '__main__':
    print(Solution().twoSum((2, 7, 11, 15), 9))
