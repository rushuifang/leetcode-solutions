// Only works for positive numbers

class Solution {
    public boolean canReorderDoubled(int[] arr) {
        Queue<Integer> queue = new PriorityQueue<>();
        Arrays.sort(arr);
        
        for (int x : arr) {
            if (!queue.isEmpty()) {
                if (queue.peek() * 2 > x) {
                    queue.add(x);
                } else if (queue.peek() * 2 == x) {
                    queue.poll();
                } else {
                    return false;
                }
            }
            else {
                queue.add(x);
            }
        }
        return queue.isEmpty();
    }
}


class Solution {
    public boolean canReorderDoubled(int[] arr) {
        Map<Integer, Integer> count = new HashMap<>();
        Integer[] B = new Integer[arr.length];
        for (int i = 0; i < arr.length; i++) {
            B[i] = arr[i];
            count.put(arr[i], count.getOrDefault(arr[i], 0) + 1);
        }
        Arrays.sort(B, Comparator.comparingInt(Math::abs));
        
        for (int x : B) {
            if (count.get(x) == 0) {
               continue;
            }
            if (count.getOrDefault(x * 2, 0) <= 0) {
                return false;
            }
            
            count.put(x, count.get(x) - 1);
            count.put(2 * x, count.get(2 * x) - 1);
        
        }
        return true;
    }
}