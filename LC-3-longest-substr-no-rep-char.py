
# Time:  O(n)
# Space: O(1)
#
# Given a string, find the length of the longest substring without repeating characters.
# For example, the longest substring without repeating letters for "abcabcbb" is "abc", which the length is 3.
# For "bbbbb" the longest substring is "b", with the length of 1.


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        max_len, curr_nrcs_start = 0, 0
        visited = {}

        for idx, char in enumerate(s):
            if char not in visited:
                visited[char] = idx
            else:
                # check it prev idx of the same char
                # if yes, move the nrcs position by 1, excluding the same char first in nrcs
                if visited[char] >= curr_nrcs_start:
                    curr_nrcs_start = visited[char]+ 1
                visited[char]=idx
            # current len = idx - curr_nrcs_start+1, from beginning of nrcs
            # always include the last char
            max_len = max(max_len, idx - curr_nrcs_start+1)
        return max_len

    def lengthOfLongestSubstring1(self, s):
        """
        :type s: str
        :rtype: int
        Too slow
        """
        if not s:
            return 0
        longest_len = [1 for x in s]
        curr_lengest_len = 1
        longest_set = [set(x) for x in s]
        for idx, it in enumerate(s):
            if idx + curr_lengest_len > len(s):
                break
            for idx2, it2 in enumerate(s[idx + 1:]):
                if it2 in longest_set[idx]:
                    break
                else:
                    longest_set[idx].add(it2)
                    longest_len[idx] += 1
                    if longest_len[idx] > curr_lengest_len:
                        curr_lengest_len = longest_len[idx]
        return curr_lengest_len


if __name__ == '__main__':
    pass
    print(Solution().lengthOfLongestSubstring('c'))
    print(Solution().lengthOfLongestSubstring('abcabcbb'))
    assert Solution().lengthOfLongestSubstring('abcabcbb')==3
    print(Solution().lengthOfLongestSubstring('bbbbb'))
    print(Solution().lengthOfLongestSubstring('pwwkew'))
    assert Solution().lengthOfLongestSubstring('pwwkew') == 3
    print(Solution().lengthOfLongestSubstring(''))
