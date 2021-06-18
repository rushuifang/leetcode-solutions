class Solution {
    public int lenLongestFibSubseq(int[] arr) {
        int N = arr.length;
        Map<Integer, Integer> index = new HashMap<>();
        Map<Integer, Integer> longest = new HashMap<>();
        for (int i = 0; i < N; i++) {
            index.put(arr[i], i);
        }
        int ans = 0;
        
        for (int k = 0; k < N; k++) {
            for (int j = 0; j < k; j++) {
                int i = index.getOrDefault(arr[k] - arr[j], -1);
                if (i != -1 && i < j) {
                    int cand = longest.getOrDefault(i * N + j, 2) + 1;
                    longest.put(j * N + k, cand);
                    ans = Math.max(ans, cand);
                }
            }
        }
        
        return ans >= 3 ? ans : 0;
    }
}