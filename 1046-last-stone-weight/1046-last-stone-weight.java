class Solution {
    public int lastStoneWeight(int[] stones) {
        // max priority queue
        PriorityQueue<Integer> pq = new PriorityQueue<>(Collections.reverseOrder());

        for(int ele : stones){ // adding the elements of array to pq
            pq.add(ele);
        }
        while(pq.size()>1){
            int max = pq.remove();
            int smax = pq.remove();

            int nstone = max - smax;

            if(nstone!=0){
                pq.add(nstone);
            }
        }
        if(pq.size()==0){
            return 0;
        }else{
            return pq.remove();
        }
    }
}