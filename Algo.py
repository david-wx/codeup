import random
import sys


def strictly_increasing(L):
    return all(x < y for x, y in zip(L, L[1:]))


def strictly_decreasing(L):
    return all(x > y for x, y in zip(L, L[1:]))


def non_increasing(L):
    return all(x >= y for x, y in zip(L, L[1:]))


def non_decreasing(L):
    return all(x <= y for x, y in zip(L, L[1:]))


class algo_sort:
    @staticmethod
    def qsort(S, a, b):
        """Quick sort in-place.

        Ref: Data structure and algorithm in Java by Michael Goodrich and Roberto Tamassia (3rd)"""
        if a >= b: return a
        pivot_idx = random.randint(a, b)
        S[pivot_idx], S[b] = S[b], S[pivot_idx]
        p = S[b]
        l, r = a, b - 1
        while l <= r:
            while l <= r and S[l] <= p: l += 1
            while r >= l and S[r] >= p: r -= 1
            if l < r: S[l], S[r] = S[r], S[l]
        S[l], S[b] = S[b], S[l]
        algo_sort.qsort(S, a, l - 1)
        algo_sort.qsort(S, l + 1, b)
        return S

    @staticmethod
    def qsort2(a, l, r):
        """Quick sort in-place.

        Alternative implementation. Random pivot selection. Pivot first
        """
        if l >= r: return a
        pivot_idx = random.randint(l, r)
        a[l], a[pivot_idx] = a[pivot_idx], a[l]
        p = a[l]
        i, j = l + 1, r
        while i < j:
            while i <= j and a[i] <= p: i = i + 1
            while i <= j and a[j] >= p: j = j - 1
            if i < j: a[i], a[j] = a[j], a[i]
        a[j], a[l] = a[l], a[j]
        algo_sort.qsort2(a, l, j - 1)
        algo_sort.qsort2(a, j + 1, r)
        return a

    @staticmethod
    def msort(a, l, r, tmp=None):

        if l >= r: return a
        if tmp is None: tmp = [None] * len(a)

        mid = (l + r) // 2
        algo_sort.msort(a, l, mid, tmp)
        algo_sort.msort(a, mid + 1, r, tmp)

        # merge the two halves
        left_start, left_end = l, mid
        right_start, right_end = mid + 1, r
        merged_idx = l
        i, j = left_start, right_start

        while i <= left_end and j <= right_end:
            if a[i] <= a[j]:
                tmp[merged_idx] = a[i]
                i += 1
            else:
                tmp[merged_idx] = a[j]
                j += 1
            merged_idx += 1

        if i < left_end + 1:
            tmp[merged_idx:right_end + 1] = a[i:left_end + 1].copy()
        if j < right_end + 1:
            tmp[merged_idx:right_end + 1] = a[j:right_end + 1].copy()
        a[l:r + 1] = tmp[l:r + 1]
        return a


if __name__ == '__main__':
    a = [random.randint(1, 99) for x in range(800)]
    print(a)
    b = algo_sort.qsort(a.copy(), 0, len(a) - 1)
    print(b)
    print(non_decreasing(b))

    print("\n" * 3)
    # a = [69, 53]
    print(a)
    b2 = algo_sort.msort(a.copy(), 0, len(a) - 1)
    print(b2)
    print(non_decreasing(b2))
