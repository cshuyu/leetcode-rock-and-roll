// Last updated: 2/23/2026, 6:45:07 PM
class Solution {
    public String mostCommonWord(String paragraph, String[] banned) {
        char[] arr = paragraph.toCharArray();
        int s = 0;
        Set<String> bannedSet = new HashSet<>(Arrays.asList(banned));
        Map<String, Integer> freq = new HashMap<>();
        while(s < arr.length) {
            int e = tokenEndIndex(arr, s);
            if(s != e) {
                // System.out.println(paragraph);
                // System.out.println(paragraph.length()+" Lengh "+s+", "+e);
                String word = paragraph.substring(s, e).toLowerCase();
                if(!bannedSet.contains(word)) {
                    int cnt = freq.containsKey(word) ? freq.get(word) + 1: 1;
                    freq.put(word, cnt);
                }
            }
            s = e+1;
        }
        int max = 0;
        String word = "";
        for(String key : freq.keySet()) {
            if (max < freq.get(key)){
                max = freq.get(key);
                word = key;
            }
        }
        return word;
    }
    
    public int tokenEndIndex(char[] arr, int s) {
        while(s<arr.length && 
              (arr[s]>='a' && arr[s]<='z'|| arr[s]>='A' && arr[s]<='Z'))
            s++;
        return s;
    }
}