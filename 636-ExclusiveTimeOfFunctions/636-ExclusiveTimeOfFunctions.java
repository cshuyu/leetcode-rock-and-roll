// Last updated: 2/23/2026, 6:46:15 PM
class Solution {
    public int[] exclusiveTime(int n, List<String> logs) {
        int[] rs = new int[n];
        Deque<Log> stack = new ArrayDeque<>();
        
        for(String logStr: logs) {
            Log log = new Log(logStr);
            if(log.isStart) {
                stack.push(log);
            }
            else {
                if(stack.isEmpty() || stack.peek().id != log.id) {
                    //throw new Exception("invalid input")
                    return null;
                }
                Log beg = stack.pop();
                int duration = log.time - beg.time + 1;
                rs[log.id] += duration;
                
                // if there is a function blocked, we should record
                // that the past duration time is not used by the function
                if(!stack.isEmpty()) {
                    rs[stack.peek().id] -= duration;
                }
            }
        }
        
        if(!stack.isEmpty()) {
            //throw new Exception("invalid input")
            return null;
        }
        return rs;
    }
    
    private static class Log {
        public int id;
        public int time;
        public boolean isStart;
        
        public Log(String log) {
            String[] strs = log.split(":");
            id = Integer.valueOf(strs[0]);
            isStart = strs[1].equals("start");
            time = Integer.valueOf(strs[2]);
        }
    }
}