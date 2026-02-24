// Last updated: 2/23/2026, 6:47:00 PM
public class Solution {
    public int findComplement(int num) {
       return ~num & (Integer.highestOneBit(num) - 1);
    }
}