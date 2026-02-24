// Last updated: 2/23/2026, 6:45:57 PM
class MaxStack {
    TreeMap<Integer, List<Node>> map;
    DoublyLinkedList dll;
    public MaxStack() {
        map = new TreeMap();
        dll = new DoublyLinkedList();
    }
    
    public void push(int x) {
        Node node = dll.add(x);
        if(!map.containsKey(x))
            map.put(x, new ArrayList<Node>());
        map.get(x).add(node);
    }
    
    public int pop() {
        int val = dll.pop();
        List<Node> lst = map.get(val);
        if(lst.size()==1)
            map.remove(val);
        else
            lst.remove(lst.size()-1);
        return val;
    }
    
    public int top() {
        return dll.peek();
    }
    
    public int peekMax() {
        return map.lastKey();
    }
    
    public int popMax() {
        int max = peekMax();
        List<Node> lst = map.get(max);
        Node node = lst.remove(lst.size()-1);
        dll.unlink(node);
        if(lst.isEmpty())
            map.remove(max);
        return max;
    }
}

class DoublyLinkedList{
    Node head;
    Node tail;
    public DoublyLinkedList() {
        head = new Node(0);
        tail = new Node(0);
        head.next = tail;
        tail.prev = head;
    }
    
    public Node add(int n) {
        Node node = new Node(n);
        node.next = tail;
        node.prev = tail.prev;
        tail.prev.next = node;
        tail.prev = node;
        return node;
    }
    
    public int pop() {
        return unlink(tail.prev).val; 
    }
    
    public int peek() {
        return tail.prev.val;
    }
    
    public Node unlink(Node node) {
        node.prev.next = node.next;
        node.next.prev = node.prev;
        return node;
    }  
}

class Node {
    int val;
    Node prev;
    Node next;
    public Node(int v) {
        val = v;
    }
}

/**
 * Your MaxStack object will be instantiated and called as such:
 * MaxStack obj = new MaxStack();
 * obj.push(x);
 * int param_2 = obj.pop();
 * int param_3 = obj.top();
 * int param_4 = obj.peekMax();
 * int param_5 = obj.popMax();
 */