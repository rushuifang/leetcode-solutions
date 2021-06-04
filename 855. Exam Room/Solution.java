class ExamRoom {
    TreeSet<int[]> pq;
    HashMap<Integer, int[]> startMap;
    HashMap<Integer, int[]> endMap;
    private int n;
    
    public ExamRoom(int n) {
        this.n = n;
        startMap = new HashMap<>();
        endMap = new HashMap<>();
        pq = new TreeSet<>((a, b) -> {
            int distA = distance(a);
            int distB = distance(b);
            if (distA == distB) {
                return b[0] - a[0];
            }
            return distA - distB;
        });
        addInterval(new int[] {-1, n});
    }
    
    public int seat() {
        int[] longest = pq.last();
        int x = longest[0];
        int y = longest[1];
        int seat;
        if (x == -1) {
            seat = 0;
        } else if (y == n) {
            seat = n - 1;
        } else {
            seat = (y + x) / 2;
        }
        int[] left = new int[] {x, seat};
        int[] right = new int[] {seat, y};
        deleteInterval(longest);
        addInterval(left);
        addInterval(right);
        return seat;
    }
    
    public void leave(int p) {
        int[] left = endMap.get(p);
        int[] right = startMap.get(p);
        int[] merge = new int[] {left[0],right[1]};
        deleteInterval(left);
        deleteInterval(right);
        addInterval(merge);
    }
    
    public int distance(int[] interv) {
        int x = interv[0];
        int y = interv[1];
        if (x == -1) {
            return y;
        } else if (y == n) {
            return y - 1 - x;
        }
        return (y - x) / 2;
    }
    
    public void addInterval(int[] interv) {
        pq.add(interv);
        startMap.put(interv[0], interv);
        endMap.put(interv[1], interv);
    }
    
    public void deleteInterval(int[] interv) {
        pq.remove(interv);
        startMap.remove(interv[0]);
        endMap.remove(interv[1]);
    }
}

/**
 * Your ExamRoom object will be instantiated and called as such:
 * ExamRoom obj = new ExamRoom(n);
 * int param_1 = obj.seat();
 * obj.leave(p);
 */