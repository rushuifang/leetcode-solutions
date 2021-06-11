class Solution {
    public int minSteps(String s, String t) {
        int[] letter1 = new int[26];
        int[] letter2 = new int[26];
        getLetters(s, letter1);
        getLetters(t, letter2);
        int res = 0;
        
        for (int i = 0; i < 26; i++) {
            if (letter1[i] > 0) {
                if (letter1[i] > letter2[i]) {
                    letter1[i] -= letter2[i];
                } else {
                    letter1[i] = 0;
                }
            }
            res += letter1[i];
        }
        
        return res;
    }
    
    public void getLetters(String str, int[] arr) {
        for (char letter : str.toCharArray()) {
            arr[letter - 'a'] += 1;
        }
    }
}