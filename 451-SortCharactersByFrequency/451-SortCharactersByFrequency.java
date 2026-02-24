// Last updated: 2/23/2026, 6:47:13 PM
public class Solution {
    public String frequencySort(String s) {
        if(s == null || s.length() <= 1) return s;
        
        HashMap<Character, Integer> map = new HashMap<Character, Integer>();
        for(int i = 0; i < s.length(); i++){
            char ch = s.charAt(i);
            if(map.containsKey(ch)){
                map.put(ch, map.get(ch) + 1);
            }
            else{
                map.put(ch, 1);
            }
        }
        
        int size = map.size();
        
        PriorityQueue<Node> pq = new PriorityQueue<Node>(size, new Comparator<Node>(){
            public int compare(Node n1, Node n2){
                return n2.count - n1.count;
            }
        });
        
        for(Character ch: map.keySet()){
            Node node = new Node(ch, map.get(ch));
            pq.offer(node);
        }
        
        StringBuilder sb = new StringBuilder("");
        
        while(pq.size() > 0){
            Node node = pq.poll();
            for(int i = 0; i < node.count; i++){
                sb.append(node.ch);
            }
        }
        
        return sb.toString();
        
    }
}

class Node {
    char ch;
    int count;
    
    public Node(char character, int c){
        ch = character;
        count = c;
    }
}