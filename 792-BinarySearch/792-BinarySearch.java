// Last updated: 2/23/2026, 6:45:15 PM
class Solution {
    public int search(int[] nums, int target) {
        if (nums == null) return -1;
        return helper(nums, target, 0, nums.length);
    }

    /** 
     *  Search the target from the nums and returns the index.
     *  The beg is the first index to search, and the end is the
     *  last + 1 index of the search range.
     */
    private int helper(int[] nums, int target, int beg, int end) {
        if (end <= beg) return -1;
        if (end == beg + 1) {
            return nums[beg] == target ? beg : -1;
        }
        int mid = (end - beg)/2  + beg;
        if (nums[mid] == target) return mid;
        else if (nums[mid] > target) {
            return helper(nums, target, beg, mid);
        } else {
            return helper(nums, target, mid + 1, end); 
        }
    }
}