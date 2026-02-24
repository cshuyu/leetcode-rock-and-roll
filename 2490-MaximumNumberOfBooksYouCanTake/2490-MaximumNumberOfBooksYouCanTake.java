// Last updated: 2/23/2026, 6:44:18 PM
class Solution {
    public long maximumBooks(int[] books) {
        if (books.length == 0) return 0;
        long[] dp = new long[books.length + 1];
        dp[0] = 0;
        dp[1] = books[0];

        Stack<Integer> stack = new Stack<>();
        stack.push(0);

        for(int i=1; i<books.length; i++) {
            // Now try with the case when we need to pick
            // from 0 to i, inclusive, and books at i needs
            // all be picked up.

            // Find the sub-problem we can resue
            while(!stack.empty() && books[stack.peek()] > books[i] - (i-stack.peek())) {
                stack.pop();
            }
            // 0,  1, 2
            // 10, 8, 5
            if (stack.empty()) {
                // we cannot reuse any sub problem, compute directly.
                // [... books[i]-2, books[i]-1, books[i]]
                if (books[i] <= i) {
                    dp[i+1] = sum(1, books[i], books[i]);
                } else {
                    dp[i+1] = sum(books[i]-i, books[i], i+1);
                }
                stack.push(i);
                continue;
            }

            // We found a subproblem we can reuse.
            int j = stack.peek();
            // i = 5, j = 2
            int middleCnt = i - j - 1;
            dp[i+1] = dp[j+1] + books[i] + sum(books[i]-middleCnt, books[i]-1, middleCnt);
            stack.push(i);
        }

        long max = 0;
        for(int i=1; i<dp.length; i++) {
            max = Math.max(max, dp[i]);
        }
        return max;
    }

    long sum(int first, int last, int n) {
        return ((long)first + last) * n / 2;
    }


}