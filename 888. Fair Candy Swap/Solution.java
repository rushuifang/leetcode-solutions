class Solution {
    public int[] fairCandySwap(int[] aliceSizes, int[] bobSizes) {
        int sumA = 0, sumB = 0;
        for (int x : aliceSizes) sumA += x;
        for (int x: bobSizes) sumB += x;
        int delta = (sumA - sumB) / 2;
        
        Set<Integer> set = new HashSet<>();
        for (int a : aliceSizes) set.add(a);
        for (int b: bobSizes) {
            if (set.contains(b + delta)) {
                return new int[] {b + delta, b};
            }
        }
        throw null;
    }
}