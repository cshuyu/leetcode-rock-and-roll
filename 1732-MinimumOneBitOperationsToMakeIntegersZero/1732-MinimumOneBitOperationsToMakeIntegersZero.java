// Last updated: 2/23/2026, 6:44:30 PM
class Solution {
    public int minimumOneBitOperations(int n) {
        // First, for numbers of format 10000, we need 2^b -1 operations to 
        // convert it to zero, where b is the number of bits. ---------- Theory 1
        //   Details: 10000 -> 11000 (build the ladder) + 1 + 01000 -> 0 
        //          According to math introduction: minimumOneBitOperations(b) = 2^b - 1
        
        // Second, for transformation of 1XXXX -> 0, we must follow the following steps
        //    (1): 1XXXX -> 11000 (This is the only way we can remove the highest bit)
        //    (2): 11000 -> 01000 (1 operation)
        //    (3): 01000 -> 0 (2^(b-1)-1 according to Theory 1)
        
        // So we know the operations for step (2) and (3), we want to reduce this step 1
        // to a smaller problem. 
        // Observe transformation: 1XXXX -> 11000 (assuming the number of bits to be b)
        // 1XXXX -> 11000  <==> XXXX -> 1000 (Make it a function toOne(XXXX)  )
        // Case 1: the higest X is 1: 
        //         1XXXX -> 11000  <==> XXXX -> 1000 <==>  1XXX -> 1000 <==> XXX -> 0 <==> minimumOneBitOperations(XXX)
        // Case 2: the highest x is 0:
        //         1XXXX -> 11000  <==> XXXX -> 1000 <==>  0XXX -> 1000, following the next steps:
        //         (1): 0XXX -> 0100 <==> XXX -> 100 (It's a reduced problem toOne(XXX))
        //         (2): 0100 -> 1100  (1 operation)
        //         (3): 1100 -> 1000 <==> 100 -> 0: (needs operations 2^(b-2) -1 )
        List<Character> lst = new ArrayList<>();
        while(n != 0) {
            if ((n & 1) == 0) lst.add('0');
            else lst.add('1');
            n = n >> 1;
        }
        Collections.reverse(lst);

        
        return toZero(lst);
    }
    
    /** The number of steps to convert lst to the format of 100..0 where they have the same length */
    private int toOne(List<Character> lst) {
        if (lst.isEmpty()) return 0;
        // System.out.println("toOne: "+lst.size() +" "+lst.get(0));
        if (lst.size() == 1 && lst.get(0) == '1') return 0;
        if (lst.size() == 1) return 1;
        
        
        if (lst.get(0) == '1') {
            // Highest bit is 1 (1XXX).
            // 1XXX -> 1000 <==> XXX -> 0
            return toZero(lst.subList(1, lst.size()));
        }
        else {
            // Highest bit is 0 (0XXX).
            // 0XXX -> 1000 <==> 
            //  (1) 0XXX -> 0100 <==> XXX -> 100 (It's a reduced problem toOne(XXX))
            //  (2): 0100 -> 1100  (1 operation)
            //  (3): 1100 -> 1000
            int b = lst.size();
            return toOne(lst.subList(1, lst.size())) + 1 + (int)(Math.pow(2, b-1) - 1);
        }
         
    }
    
    private int toZero(List<Character> lst) {
        if (lst.isEmpty()) return 0;
        // System.out.println("toZero: "+lst.size() +" "+lst.get(0));
        if (lst.size() == 1 && lst.get(0) == '1') return 1;
        if (lst.size() == 1) return 0;
        
        // Highest bit index
        int i = 0;
        for(; i<lst.size(); i++) {
            if (lst.get(i) == '1') {
                break;
            }
        }
        // The lst has all zeros.
        if (i == lst.size()) return 0;
        
        // The lst is "0XXXX", to convert to "00000", it's basically "XXXX" -> 0
        if (i > 0) return toZero(lst.subList(1, lst.size()));
        
        // Now lst is "1XXXX" to conver it to "0", we need ladders
        //   (1): 1XXXX -> 11000 (toOne(XXXX))
        //.  (2): 11000 -> 01000
        //   (3): 01000 -> 0 (2^(b-1) -1)
        int b = lst.size();
        return toOne(lst.subList(1, lst.size())) + 1 + (int)(Math.pow(2, b-1) - 1);
        
    }
}