// Last updated: 2/23/2026, 6:44:54 PM
class Solution {
    public String shortestSuperstring(String[] A) {
        int totalSubsetNumber = 1 << A.length; // 2^length
        // System.out.println(totalSubsetNumber);
        int[][] d= new int[totalSubsetNumber][A.length];
        int[][] steps= new int[totalSubsetNumber][A.length];
        
        for (int i=0; i<totalSubsetNumber; i++) {
            for(int j=0; j<A.length; j++) {
                d[i][j] = Integer.MAX_VALUE;
            }
        }
        
        // Update the subset of size 1.
        for (int i=0; i<A.length; i++) {
            // d[{i}][i]  = 0
            d[1<<i][i] = A[i].length();
        }
        
        Integer[] subsets = new Integer[totalSubsetNumber];
        for(int i=0; i<totalSubsetNumber; i++) {
            subsets[i] = i;    
        }
        Arrays.sort(subsets, new Comparator<Integer>(){
            @Override
            public int compare(Integer a, Integer b) {
                // System.out.println(a+", "+b);
                return Integer.bitCount(a) - Integer.bitCount(b);
            }
        });
        
        int k = 0;
        while (k < subsets.length){
            int s = subsets[k++];
            for(int j=0; j<A.length; j++) {
                int label = 1 << j;
                if ((label | s) != s) {
                    // Node j is not at S.
                    continue;
                }
                // handle d[s][j]
                // System.out.println("Handle "+s+", "+j);
                int s2 = s & (~label);
                if (s2 == 0) {
                    continue;
                }
                int val = Integer.MAX_VALUE;
                for(int i=0; i<A.length; i++) { 
                    // System.out.println();
                    int label2 = 1 << i;
                    if ((label2 | s2) != s2 || i==j) {
                        // Node i is not at S - {j}.
                        continue;
                    }
                    // System.out.println("  I: "+i+", "+j + "] distance: "+ distance(A[i], A[j]));
                    if (d[s2][i] == Integer.MAX_VALUE) {
                        System.out.println("Trying to read: ["+s2+","+label2+"] to reach "+label);
                    }
                    int curVal = d[s2][i] + distance(A[i], A[j]);
                    if (curVal < val) {
                        val = curVal;
                        steps[s][j] = i;
                    }
                }
                // System.out.println("Update "+s+", "+j+" "+val);
                d[s][j] = val;
            }
        };
        
        Stack<String> stack = new Stack<String>();
        
        int next = 0;
        int last = 0;
        int subset = d.length - 1; 
        int min = Integer.MAX_VALUE;
        for(int i=0; i<A.length; i++) {
            if (d[subset][i] < min) {
                min = d[subset][i];
                last = i;
                next = steps[subset][i];
            }
        }
        int lastLabel = 1 << last;
        int nextLabel = 1 << next;
        stack.push(A[last]);
        subset = subset & (~lastLabel);
        
        while(subset >0) {   
            min = Integer.MAX_VALUE;
            last = next;
            next = steps[subset][last];
            stack.push(A[last]);
            lastLabel = 1 << last;
            nextLabel = 1 << next;
            subset = subset & (~lastLabel);
            // System.out.println("MIN:" + min+" Last: "+ last +" ,Next: "+next+", "+Integer.toBinaryString(subset));
            // System.out.println(Integer.toBinaryString(subset));
        }
        
        StringBuilder sb = new StringBuilder();
        while(!stack.isEmpty()) {
            String val = stack.pop();
            // System.out.println(val);
            boolean changed = false;
            for(int i=0; i<sb.length(); i++) {
                if(val.startsWith(sb.substring(i))) {
                    sb.append(val.substring(sb.length() - i));
                    changed = true;
                    break;
                }
            }
            if(!changed) {
                sb.append(val);
            }
            
        }
        return sb.toString();
    }
    
    private int distance(String from, String to) {
        for(int i=0; i<from.length(); i++) {
            if(to.startsWith(from.substring(i))) {
                return to.length() - (from.length() - i);
            }
        }
        return to.length();
    }
}