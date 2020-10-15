class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        count = 0 
        for s in range(len(A) - 2):
            d = A[s + 1] - A[s]
            for e in range(s + 2, len(A)):
                if A[e] - A[e - 1] == d:
                    count += 1
                else:
                    break
        return count
        
# Remember there's always brutal force when you can't think of a dynamic
# programming algorithm

public class Solution {
    public int numberOfArithmeticSlices(int[] A) {
        int[] dp = new int[A.length];
        int sum = 0;
        for (int i = 2; i < dp.length; i++) {
            if (A[i] - A[i - 1] == A[i - 1] - A[i - 2]) {
                dp[i] = 1 + dp[i - 1];
                sum += dp[i];
            }
        }
        return sum;
    }
}