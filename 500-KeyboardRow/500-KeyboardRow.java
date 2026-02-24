// Last updated: 2/23/2026, 6:46:48 PM
public class Solution {
    public String[] findWords(String[] words) {
        ArrayList<HashSet<Character>> keys = new ArrayList<HashSet<Character>>();
        keys.add(new HashSet<Character>(Arrays.asList('q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p')));
        keys.add(new HashSet<Character>(Arrays.asList('a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l')));
        keys.add(new HashSet<Character>(Arrays.asList('z', 'x', 'c', 'v', 'b', 'n', 'm')));
        
        ArrayList<String> ret = new ArrayList<String>();
        
        for(String word : words){
            String low = word.toLowerCase();
            
            
            for(HashSet<Character> set : keys){
                if(set.contains(low.charAt(0))){
                    boolean matched = true;
                    for(int i = 0; i < low.length(); i++){
                        if(!set.contains(low.charAt(i))){
                            matched = false;
                            break;
                        }
                    }
                    
                    if(matched){
                        ret.add(word);
                    }
                }
            }
        }
        
        String[] result = new String[ret.size()];
        int index = 0;
        
        for(String str: ret){
            result[index++] = str;
        }
        
        return result;
        
    }
}