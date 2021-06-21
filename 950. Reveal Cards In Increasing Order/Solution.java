class Solution {
   
    public int[] deckRevealedIncreasing(int[] deck) {
        Queue<Integer> index = new LinkedList<>();
        int N = deck.length;
        int[] ans = new int[N];
        Arrays.sort(deck);
        for (int i = 0; i < N; i++) {index.add(i);}
        
        for (int i = 0; i < N; i++) {
            ans[index.poll()] = deck[i];
            if (!index.isEmpty()) {
                index.add(index.poll());
            }         
        }
        
        return ans;
    }
    
}

