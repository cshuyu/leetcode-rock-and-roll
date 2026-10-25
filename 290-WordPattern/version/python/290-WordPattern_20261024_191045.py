# Last updated: 10/24/2026, 7:10:45 PM
1class Solution:
2    def wordPattern(self, pattern: str, s: str) -> bool:
3        s_list = s.split(" ")
4        char_word_map = {}
5        word_char_map = {}
6        if len(pattern) != len(s_list):
7            return False
8        for i in range(len(pattern)):
9            char = pattern[i]
10            word = s_list[i]
11            if char not in char_word_map:
12                char_word_map[char] = word
13            else:
14                if word != char_word_map[char]:
15                    return False
16            if word not in word_char_map:
17                word_char_map[word] = char
18            else:
19                if char != word_char_map[word]:
20                    return False
21        return True