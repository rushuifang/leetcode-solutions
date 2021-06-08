class Solution {
    private int counts;
    public int balancedStringSplit(String s) {
        Stack<Character> stack = new Stack<>();
        for (char letter : s.toCharArray()) {
            if (!stack.empty()) {
                if (stack.peek() != letter) {
                    stack.pop();
                } else {
                    stack.push(letter);
                }
            } else {
                stack.push(letter);
            }
            if (stack.empty()) {counts++;}
        }
        return counts;
    }
}

// Easier solution
class Solution {
    public int balancedStringSplit(String s) {
        int res = 0;
        int counts = 0;
        for (char letter : s.toCharArray()) {
            counts += letter == 'R' ? 1 : -1;
            if (counts == 0) res++; 
        }
        return res;
    }
}
