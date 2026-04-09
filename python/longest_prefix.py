#!/bin/python3

class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        n = 0
        while n <= 200:
            if not self.check_all_words_for_nth_caracter(strs, n): break
            else: n +=  1

        return strs[0][:n]

    def check_all_words_for_nth_caracter(self, strs: list[str], n:int) -> bool:
        c = None
        for str_item in strs:
            if not self.list_get(str_item, n):
                return False
            elif not c:
                c = str_item[n]
            elif str_item[n] != c:
                return False
        else:
            return True

    def list_get(self, lst: list, index: int, default=None):
        return lst[index] if 0 <= index < len(lst) else default

solution = Solution()

print(solution.longestCommonPrefix(
    ["flower","flow","flight"]
))

print(solution.longestCommonPrefix(
    ["dog","racecar","car"]
))

print(solution.longestCommonPrefix(
    ["dog","dog","dog"]
))

print(solution.longestCommonPrefix(
    ["dog","","dog"]
))

print(solution.longestCommonPrefix(
    ["animaldog","animalcat","animalbear","animalmouse"]
))
