// Last updated: 2/23/2026, 6:47:21 PM
class Solution {
    public int compress(char[] chars) {
        if(chars.length == 1)
            return 1;
        int write = 0;
        int count = 1;
        for(int read=1; read<chars.length; read++) {
            if(chars[read] != chars[read-1]) {
                chars[write++] = chars[read-1];
                write = writeCount(chars, count, write);
                count = 1;
            }
            else
                count++;
        }
        chars[write++] = chars[chars.length-1];
        if(count != 1)
            write = writeCount(chars, count, write);
        return write;
    }
    
    public int writeCount(char[] chars, int count, int write) {
        if(count>1 && count<10)
            chars[write++] = (char)('0'+ count);
        if(count >= 10) {
            char[] countArray = String.valueOf(count).toCharArray();
            for(int i=0; i<countArray.length; i++)
                chars[write++] = countArray[i];
        }
        return write;    
    }
}