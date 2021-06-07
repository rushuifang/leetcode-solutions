class Solution {
    int count;
    int[] charFreq = new int[26];
    
    public int countCharacters(String[] words, String chars) {
        for (char c : chars.toCharArray()) {++charFreq[c - 'a'];}
        for (String word : words) {
            if (isGood(word)) count += word.length();
        }
        
        return count;
    }
    
    public boolean isGood(String word) {
        int[] localFreq = new int[26];
        for (char c : word.toCharArray()) {++localFreq[c - 'a'];}
        for (int i = 0; i < 26; i++) {
            if (localFreq[i] > charFreq[i]) {return false;}
        }
        
        return true;
    }
}