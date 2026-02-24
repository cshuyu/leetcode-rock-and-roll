// Last updated: 2/23/2026, 6:45:09 PM
class MyHashMap {
    private int keySpace;
    private List<Bucket> hashTable;
    public MyHashMap() {
        this.keySpace = 3000;
        this.hashTable = new ArrayList<Bucket>();
        for(int i=0; i<keySpace; i++) {
            hashTable.add(new Bucket());
        }
    }
    
    public void put(int key, int value) {
        int hashVal = key % keySpace;
        hashTable.get(hashVal).put(key, value);
    }
    
    public int get(int key) {
        int hashVal = key % keySpace;
        return hashTable.get(hashVal).get(key);
    }
    
    public void remove(int key) {
        int hashVal = key % keySpace;
        hashTable.get(hashVal).remove(key);
    }
    
    static class Bucket {
        private List<Pair> bucket;
        public Bucket() {
            bucket = new ArrayList<Pair>(); 
        }
        
        public void put(int key, int value) {
            boolean hasKey = false;
            for(int i=0; i<bucket.size(); i++) {
                Pair pair = bucket.get(i);
                if(key==pair.key) {
                    pair.value = value;
                    hasKey = true;
                }
            }
            if(!hasKey) {
                bucket.add(new Pair(key, value));
            }
            
        }
        
        public int get(int key) {
            for(int i=0; i<bucket.size(); i++) {
                Pair pair = bucket.get(i);
                if(key==pair.key) {
                    return pair.value;
                }
            }
            return -1;
        }
        
        public void remove(int key) {
            for(int i=0; i<bucket.size(); i++) {
                Pair pair = bucket.get(i);
                if(key==pair.key) {
                    bucket.remove(i);
                }
            }
            //throw exception
        }
    }
    
    static class Pair {
        private int key;
        private int value;
        public Pair(int key, int value) {
            this.key = key;
            this.value = value;
        }
    }
}

/**
 * Your MyHashMap object will be instantiated and called as such:
 * MyHashMap obj = new MyHashMap();
 * obj.put(key,value);
 * int param_2 = obj.get(key);
 * obj.remove(key);
 */



// List<Bucket>
// [(<key, value>, <key, value>, <key, value>), (<key, value>, <key, value>, <key, value>), ....,(<key, value>, <key, value>, <key, value>))
 
// Bucket List<Pair>
// (<key, value>, <key, value>, <key, value>) ---> hashVal

// Pair ->key, value


// hashVal = keyVal%keySpace
// keySpace = 3000

// if hashMap has n values, and it has m hashvals, put operation O(time): O(n/m)
// get operation: O(time): O(n/m)
// remove operation: o(n/m)
 
// space: o(n)