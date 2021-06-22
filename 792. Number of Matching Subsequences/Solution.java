class Solution {
    public int numMatchingSubseq(String s, String[] words) {
        ArrayList<Integer>[] index = new ArrayList[256];
        int lenS = s.length();
        int count = 0;
        
        for (int i = 0; i < lenS; i++) {
            char c = s.charAt(i);
            if (index[c] == null) {
                index[c] = new ArrayList<Integer>();
            }
            index[c].add(i);
        }
        
        for (String word : words) {
            if (isSub(word, s, index)) {count++;}
        }
        return count;
    }
    
    public boolean isSub(String word, String s, ArrayList<Integer>[] index) {
        int lenWord = word.length();
        int j = 0;
            
        for (int i = 0; i < lenWord; i++) {
            char c = word.charAt(i);
            if (index[c] == null) return false;
            int pos = getLeftBound(index[c], j);
            if (pos == index[c].size()) return false;
            j = index[c].get(pos) + 1;
        }
        
        return true;
    }
    
    
    public int getLeftBound(ArrayList<Integer> al, int target) {
        int low = 0;
        int high = al.size();
        
        while (low < high) {
            int mid = (low + high) / 2;
            if (al.get(mid) >= target) {
                high = mid;   
            } else {
                low = mid + 1;
            }
        }
        return low;
    }
}