class Solution {
    public int minEatingSpeed(int[] piles, int h) {
        int m = getMax(piles);
        int right = m;
        int left = 1;
        while (left < right) {
            int mid = (left + right) / 2;
            if (canFinish(mid, piles, h)) {
                right = mid;
            } else {
                left = mid + 1;
            }
        }
        return left;
    }
    
    public int getMax(int[] piles) {
        int m = 0;
        for (int n : piles) {
            if (n > m) {
                m = n;
            }
        }
        return m;
    }
    
    public boolean canFinish(int speed, int[] piles, int h) {
        int time = 0;
        for (int n : piles) {
            time += n / speed + ((n % speed == 0) ? 0 : 1);
        }
        return time <= h;
    }
}