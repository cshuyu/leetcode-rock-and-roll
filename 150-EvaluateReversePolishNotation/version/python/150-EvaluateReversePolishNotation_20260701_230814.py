# Last updated: 7/1/2026, 11:08:14 PM
# Stack
1Time: O(n)
2Space: O(n)
3class Solution:
4    def evalRPN(self, tokens: List[str]) -> int:
5        cal_stack = []
6        operators = ["+", "-", "*", "/"]
7        for curr_str in tokens:
8            if curr_str not in operators:
9                try:
10                    curr_int = int(curr_str)
11                except ValueError:
12                    raise ValueError(f"Not valid string {curr_str} for operator")
13                cal_stack.append(curr_int)
14            else:
15                try:
16                    second_int = cal_stack.pop()
17                    first_int = cal_stack.pop()
18                except IndexError:
19                    raise IndexError(f"Not enough number for operator, cal_stack size is {len(stack)}")
20                if curr_str == "+":
21                    res_int = first_int + second_int
22                elif curr_str == "-":
23                    res_int = first_int - second_int
24                elif curr_str == "*":
25                    res_int = first_int * second_int
26                elif curr_str == "/":
27                    try:
28                        res_int = int(first_int / second_int)
29                    except ZeroDivisionError:
30                        raise ZeroDivisionError(f"Runtime Error: invalid Division {first_int}/{second_int}")
31                cal_stack.append(res_int)
32        
33        if not cal_stack or len(cal_stack)>1:
34            raise ValueError(f"there are {len(cal_stack)} numbers left without operators")
35
36        return cal_stack[0]
37