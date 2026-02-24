// Last updated: 2/23/2026, 6:46:03 PM
class Solution {
    public List<String> topKFrequent(String[] words, int k) {
        Map<String, Integer> count = new HashMap<>();
        for(String word: words) {
            count.put(word, count.getOrDefault(word, 0)+1);
        }
        
        PriorityQueue<String> heap = new PriorityQueue<String>(k, new Comparator<String>(){
            public int compare(String s1, String s2) {
                int comparison = count.get(s1)-count.get(s2);
                if(comparison == 0)
                    return s2.compareTo(s1);
                else
                    return comparison;
            }
        });
        
        for(String key: count.keySet()) {
            heap.offer(key);
            if(heap.size()>k)
                heap.poll();
        }
        
        List<String> ans = new ArrayList();
        while(!heap.isEmpty())
            ans.add(heap.poll());
        Collections.reverse(ans);
        return ans;
    }
}