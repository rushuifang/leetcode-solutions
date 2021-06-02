class Solution {
    List<List<Integer>> res = new LinkedList();
    
    public List<List<Integer>> permute(int[] nums) {
        LinkedList<Integer> track = new LinkedList();
        backTrack(nums, track);
        return res;
    }
    
    void backTrack(int[] nums, LinkedList<Integer> track) {
        if (track.size() == nums.length) {
//             what if I don't use new
            res.add(new LinkedList(track));
            return;
        }
        
        for (int i = 0; i < nums.length; i++) {
            if (track.contains(nums[i])) continue;
            track.add(nums[i]);
            backTrack(nums, track);
            track.removeLast();

        }
    }
}