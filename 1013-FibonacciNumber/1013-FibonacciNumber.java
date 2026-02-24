// Last updated: 2/23/2026, 6:44:52 PM
class Solution {
    public int fib(int n) {
        if (n == 0) return 0;
        if (n == 1) return 1;
        long prev0 = 0;
        long prev1 = 1;
        long v = 0;
        for(int i=2; i<=n; i++) {
            v = prev0 + prev1;
            prev0 = prev1;
            prev1 = v;
        }
        return (int)v;
    }
}