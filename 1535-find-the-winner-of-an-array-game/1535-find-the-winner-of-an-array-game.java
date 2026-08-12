class Solution {
    public int getWinner(int[] arr, int k) {
        Queue<Integer> queue = new LinkedList<>();
        int maxElement = arr[0];
        for(int i=1; i<arr.length; i++){
            maxElement = Math.max(maxElement, arr[i]);
            queue.offer(arr[i]);
        }
        int curr = arr[0];
        int winStreak = 0;
        while(!queue.isEmpty()){
            int opponent = queue.poll();
            if(curr> opponent){
                queue.offer(opponent);
                winStreak++;
            }
            else{
                queue.offer(curr);
                curr = opponent;
                winStreak = 1;
            }
            if(winStreak == k || curr == maxElement){
                return curr;
            }
        }
        return -1;
    }
}