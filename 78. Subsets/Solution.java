class Solution {
    List<List<Integer>> res = new ArrayList();
    public List<List<Integer>> subsets(int[] nums) {
        ArrayList<Integer> track = new ArrayList();
        backTrack(nums, 0, track);
        return res;
    }
    
    public void backTrack(int[] nums, int start, ArrayList<Integer> track) {
        res.add(new ArrayList(track));
        
        for (int i = start; i < nums.length; i++) {
            track.add(nums[i]);
            backTrack(nums, i + 1, track);
            track.remove(track.size() - 1);
        }
    }
}