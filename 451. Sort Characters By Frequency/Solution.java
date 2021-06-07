class Solution {
    public String frequencySort(String s) {
        HashMap<Character, Integer> count = new HashMap<>();
        for (char letter : s.toCharArray()) {
            count.put(letter, count.getOrDefault(letter, 0) + 1);
        }
        System.out.println(count);
        Queue<Character> heap = new PriorityQueue<>((a, b) -> count.get(b) - count.get(a));
        for (char letter: count.keySet()) {
            heap.add(letter);
        }
        System.out.println(heap);
        String res = "";
        while (heap.size() != 0) {
            char letter = heap.poll();
            StringBuilder sb = new StringBuilder();
            for (int i = 0; i < count.get(letter); i++) {
                sb.append(letter);
            }
            res += sb;
        }
        return res;
    }
}