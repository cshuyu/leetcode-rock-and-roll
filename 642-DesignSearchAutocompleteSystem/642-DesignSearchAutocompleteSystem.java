// Last updated: 2/23/2026, 6:46:14 PM
class AutocompleteSystem {
    static class Node {
        public int cnt = 0;
        public String word ="";
        public boolean isTerminal = false;
        public Node[] children = new Node[27]; // space + letters
    }
    
    Node root;
    Node cur;
    
    public AutocompleteSystem(String[] sentences, int[] times) {
        root = new Node();
        cur = root;
        for(int i=0; i<times.length; i++) {
            String s = sentences[i];
            int t = times[i];
            StringBuilder sb = new StringBuilder();
            Node node = root;
            for(int j=0; j<s.length(); j++) {
                sb.append(s.charAt(j));
                int id = idx(s.charAt(j));
                if (node.children[id] == null)
                    node.children[id] = new Node();
                node = node.children[id];
                node.word = sb.toString();
            }
            node.isTerminal = true;
            node.cnt = t;
        }
    }
    
    public List<String> input(char c) {
        List<Node> nodes = new ArrayList<>();
        List<String> rs = new ArrayList<>();
        if (c == '#') {
            cur.isTerminal = true;
            cur.cnt++;
            cur = root;
            return rs;
        } else{
            int id = idx(c);
            if (cur.children[id] == null){
                cur.children[id] = new Node();
                cur.children[id].word = cur.word + c;
            }
            cur = cur.children[id];
            findAllWords(cur, nodes);//need to sort based on count.
        }
        
        Collections.sort(nodes, new Comparator<Node>(){
            @Override
            public int compare(Node n1, Node n2) {
                if (n2.cnt != n1.cnt)
                    return n2.cnt - n1.cnt;
                else
                    return n1.word.compareTo(n2.word);
            }
        });
        
        for(Node node : nodes) {
            rs.add(node.word);
            if (rs.size() == 3)
                break;
        }
        return rs;
    }
    
    public void findAllWords(Node node, List<Node> rs){
        if (node.isTerminal)
            rs.add(node);
        for(Node child : node.children){
            if (child != null)
                findAllWords(child, rs);
        }
    }
    
    
    public int idx(char c){
        int rs = c - 'a';
        //space is smaller than ;a;
        return rs < 0 ? 26 : rs;
    }
}

/**
 * Your AutocompleteSystem object will be instantiated and called as such:
 * AutocompleteSystem obj = new AutocompleteSystem(sentences, times);
 * List<String> param_1 = obj.input(c);
 */