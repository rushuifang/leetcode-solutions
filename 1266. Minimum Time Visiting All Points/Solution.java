class Solution {
    public int minTimeToVisitAllPoints(int[][] points) {
        int distance = 0;
        int i = 0;
        int j = 1;
        
        while (j < points.length) {
            distance += Math.max(Math.abs(points[j][0] - points[i][0]), Math.abs(points[j][1] - points[i][1]));
            i = j;
            j++;
        }
        
        return distance;
    }
}