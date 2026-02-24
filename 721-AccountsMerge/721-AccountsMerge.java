// Last updated: 2/23/2026, 6:45:53 PM
class Solution {
    HashSet<String> visited = new HashSet<>();
    Map<String, List<String>> adjacent = new HashMap<String, List<String>>();
    
    private void dfs(List<String> mergedAccount, String email) {
        visited.add(email);
        mergedAccount.add(email);
        
        if(!adjacent.containsKey(email)) {
            return;
        }
        
        for(String neighbor: adjacent.get(email)) {
            if(!visited.contains(neighbor)) {
                dfs(mergedAccount, neighbor);
            }
        }
    }
    
    public List<List<String>> accountsMerge(List<List<String>> accountList) {
        int accountListSize = accountList.size();
        for(List<String> account : accountList) {
            int accountSize = account.size();
            String accountFirstEmail = account.get(1);
            for(int j=2; j<accountSize; j++) {
                String accountEmail = account.get(j);
                if(!adjacent.containsKey(accountFirstEmail)) {
                    adjacent.put(accountFirstEmail, new ArrayList<String>());
                }
                adjacent.get(accountFirstEmail).add(accountEmail);
                
                if(!adjacent.containsKey(accountEmail)) {
                    adjacent.put(accountEmail, new ArrayList<String>());
                }
                adjacent.get(accountEmail).add(accountFirstEmail);
            }
        }
        
        // Traverse over all the accounts to store components
        List<List<String>> mergedAccounts = new ArrayList<>();
        for(List<String> account: accountList) {
            String accountName = account.get(0);
            String accountFirstEmail = account.get(1);
            
            if(!visited.contains(accountFirstEmail)) {
                List<String> mergedAccount = new ArrayList<>();
                mergedAccount.add(accountName);
                dfs(mergedAccount, accountFirstEmail);
                Collections.sort(mergedAccount.subList(1, mergedAccount.size()));
                mergedAccounts.add(mergedAccount);             
            }
        }
        return mergedAccounts;
    }
}