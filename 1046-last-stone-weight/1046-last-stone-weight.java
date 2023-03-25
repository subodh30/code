class Solution {
    public int lastStoneWeight(int[] stones) {
        PriorityQueue<Integer> pq = new PriorityQueue<>(Collections.reverseOrder());
        for(int x: stones){
            pq.add(x);
        }
        System.out.println(pq);
        while(pq.size() > 1){
            int a = pq.poll();
            int b = pq.poll();
            System.out.println(pq);
            if(a-b != 0){
                pq.add(Math.abs(a-b));
            }
        }
        return pq.isEmpty() ? 0 : pq.poll();
    }
}