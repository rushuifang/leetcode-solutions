class Solution {
    int idx = 0;
    
    public int calculate(String s) {
        Stack<Integer> stack = new Stack<>();
        char sign = '+';
        int num = 0;
        int pre = 0;
        int sum = 0;

        while (idx < s.length()) {
            char c = s.charAt(idx);

            if (Character.isDigit(c)) {
                num = num * 10 + (c - '0');
            }
            if (c == '(') {
                idx++;
                num = calculate(s);
            }

            if ((!Character.isDigit(c) && c != ' ') || idx == s.length() - 1) {
                if (sign == '+') {
                    stack.push(num);
                } else if (sign == '-') {
                    stack.push(-1 * num);
                } else if (sign == '*') {
                    pre = stack.pop();
                    stack.push(pre * num);
                } else if (sign == '/') {
                    pre = stack.pop();
                    stack.push(pre / num);
                }
                sign = c;
                num = 0;
            }
            if (c == ')') {
                break;
            }
            idx++;
        }

        for (int x : stack) {sum += x;}
        return sum;
    }
}