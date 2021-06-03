class Solution {
    List<List<Integer>> res = new ArrayList<>();
    
    public List<List<Integer>> combine(int n, int k) {
        ArrayList<Integer> track = new ArrayList();
        backTrack(n, k, 1, track);
        return res;
    }
    
    public void backTrack(int n, int k, int start, ArrayList<Integer> track) {
        if (track.size() == k) {
            res.add(new ArrayList(track));
            return;
        }
        
        for (int i = start; i <= n; i++) {
            track.add(i);
            backTrack(n, k, i + 1, track);
            track.remove(track.size() - 1);
        }
    }
}