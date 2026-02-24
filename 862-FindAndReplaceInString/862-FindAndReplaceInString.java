// Last updated: 2/23/2026, 6:45:04 PM
class Solution {
    public String findReplaceString(String s, int[] indices, String[] sources, String[] targets) {
        Map<Integer, Integer> myMap = new HashMap<>();
        for(int i=0; i<indices.length; i++) {
            if(s.startsWith(sources[i],indices[i])) {
                myMap.put(indices[i], i);
            }
        }
        StringBuilder sb = new StringBuilder();
        for(int j=0; j<s.length(); j++) {
            if(myMap.containsKey(j)) {
                int index = myMap.get(j);
                sb.append(targets[index]);
                j += sources[index].length()-1;
            }
            else {
                sb.append(s.charAt(j));
            }
        }
        return sb.toString();
    }
}