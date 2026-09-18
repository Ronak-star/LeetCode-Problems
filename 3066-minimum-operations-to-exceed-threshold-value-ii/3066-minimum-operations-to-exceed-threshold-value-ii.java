class Solution {
    public int minOperations(int[] nums, int k) {
        PriorityQueue<Long> pq = new PriorityQueue<>();
        for(int i=0; i<nums.length; i++){
            pq.offer((long)nums[i]);
        }
        int count = 0;
        while(!pq.isEmpty() && pq.size() > 1){
            long x = pq.poll();
            long y = pq.poll();
            if(x < k || y < k){
                long newVal = Math.min(x,y) * 2 + (long) Math.max(x, y);
                pq.offer(newVal);
                count++;
            }
            else{
                break;
            }

        }
        return count;
    }
}