class Solution {
    public int shipWithinDays(int[] weights, int days) {
        int left = getMax(weights);
        int right = getSum(weights);
        while (left < right) {
            int mid = (left + right) / 2;
            if (work(mid, weights, days)) {
                right = mid;
            } else {
                left = mid + 1;
            }
        }
        return left;
    }
    
    public int getMax(int[] weights) {
        int n = 0;
        for (int weight : weights) {
            if (weight >= n) {
                n = weight;
            }
        }
        return n;
    }
            
    public int getSum(int[] weights) {
        int sum = 0;
        for (int weight : weights) {
            sum += weight;
        }
        return sum;
    }
            
    public boolean work(int cap, int[] weights, int days) {
        int i = 0;
        for (int day = 0; day < days; day++) {
            int maxCap = cap;
            while ((maxCap -= weights[i]) >= 0) {
                i++;
                if (i == weights.length) {
                    return true;
                }
            }
        }
        return false;
    }
}