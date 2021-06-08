class Solution {
    public int maxNumberOfBalloons(String text) {
        int[] counts = new int[5];
        for (char letter : text.toCharArray()) {
            switch (letter) {
                case 'b':
                    counts[0]++;
                    break;
                case 'a':
                    counts[1]++;
                    break;
                case 'l':
                    counts[2]++;
                    break;
                case 'o':
                    counts[3]++;
                    break;
                case 'n':
                    counts[4]++;
                    break;
            }
        }
        counts[2] /= 2;
        counts[3] /= 2;
        Arrays.sort(counts);
        return counts[0];
    }
}