// Last updated: 2/23/2026, 6:46:25 PM
class Solution {
    public int subarraySum(int[] nums, int k) {
        if(nums==null || nums.length==0)
            return 0;
        int currSum = 0;
        int count = 0;
        Map<Integer, Integer> sumCountMap = new HashMap<>();
        sumCountMap.put(0, 1);
        for(int i=0; i<nums.length; i++) {
            currSum += nums[i];
            if(sumCountMap.containsKey(currSum-k)) {
                count += sumCountMap.get(currSum-k);
            }
            if(sumCountMap.containsKey(currSum)) {
                sumCountMap.put(currSum, sumCountMap.get(currSum)+1);
            }
            else {
                sumCountMap.put(currSum, 1);
            }
        }
        // if(count==0 && currSum<k)
        //     throw Exception("no subset equals to k");
        return count;
    }
}



// HashMap<sum, count>

// allSum<k, throw Exception()
// noAnswer, 
// sum-k


// 1,1,1    k=3   currSum=3    currSum-k=0  count=1
    
// 1,1,1    k=-7

    
// 1,2,3  k=3   (0, 1) count:0
// index1: currSum: 1, currSum-k: -2,  count:0,  (0,1), (1,1)
// index2: currSum: 3, currSum-k: 0, count: 0+1=1, (0,1), (1,1), (3, 1) --->[1,2]
// index3; currSum: 6, currSum-k: 3, count: 1+1=2, (0,1), (1,1), (3,1), (6, 1)---> [3]
    
// return count 2