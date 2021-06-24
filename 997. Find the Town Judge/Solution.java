class Solution {
    public int findJudge(int n, int[][] trust) {
        Set<Integer> noJudge = new HashSet<>();
        Map<Integer, Integer> trustVotes = new HashMap<>();
        if (trust.length == 0) {
            if (n == 1) {
                return 1;
            } else {
                return -1;
            }
        }
        
        for (int[] arr : trust) {
            noJudge.add(arr[0]);
            trustVotes.put(arr[1], trustVotes.getOrDefault(arr[1], 0) + 1);
        }
        
        Queue<Integer> heap = new PriorityQueue<>((n1, n2) -> trustVotes.get(n2) - trustVotes.get(n1));
        
        for (int candidate: trustVotes.keySet()) {
            heap.add(candidate);
        }
        
        int judge = heap.poll();
        if (!noJudge.contains(judge) && trustVotes.get(judge) == n - 1) return judge;
        return -1;
    }
}

// 
class Solution {
    public int findJudge(int N, int[][] trust) {
		// base case
        if(N==1) return 1;
        int cand = -1;
		// create an array to store the indegree of every node
        int[] tj = new int[N+1];
        for(int i=1;i<=trust.length;i++) {
            tj[trust[i-1][1]]+=1; 
            if(tj[trust[i-1][1]]==(N-1)) cand = trust[i-1][1]; // checking if condition 2 is satisfied
        }
		// verfying step 2
        for(int i=1;i<=trust.length;i++) {
            if(trust[i-1][0] == cand ) return -1;
        }
        return cand;
    }
}