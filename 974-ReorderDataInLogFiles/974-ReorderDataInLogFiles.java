// Last updated: 2/23/2026, 6:44:55 PM
class Solution {
     
    public String[] reorderLogFiles(String[] logs) {
        Comparator<String> comparator = new Comparator<String>(){
            @Override
            public int compare(String log1, String log2) {
                int i=0,j=0;
                while(log1.charAt(i) != ' ')
                    i++;
                while(log2.charAt(j) != ' ')
                    j++;
                return log1.substring(i+1).compareTo(log2.substring(j+1));
            }
        };
        int rep = logs.length-1;
        for(int i=logs.length-1; i>=0; i--) {
            if(isDigitLog(logs[i])) {
                if (i != rep) {
                    String tmp = logs[i];
                    logs[i] = logs[rep];
                    logs[rep] = tmp;
                } 
                rep--;
            }
        }
        
        // case 1: rep < 0
        //   case 1a, the first is letter, nothing changed.
        // . case 1b, the first is digit, nothing changed.
        // case 2 rep >= 0 && rep < length-1: last == rep
        // case 3 rep == length -1: last = rep
        
        Arrays.sort(logs, 0, rep+1, comparator);
        
        return logs;
    }
    
    public boolean isDigitLog(String log) {
        int idx = -1;
        for(int i=0; i<log.length(); i++) {
            if (log.charAt(i) == ' ') {
                idx = i;
                break;
            }
        }
        
        boolean rs= log.charAt(idx+1) >='0' && log.charAt(idx+1)<='9';
        return rs;
    }            
               
}