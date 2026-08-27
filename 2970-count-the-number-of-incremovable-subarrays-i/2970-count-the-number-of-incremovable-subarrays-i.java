class Solution {
    public int incremovableSubarrayCount(int[] arr) {
        int count = 0;
        int len = arr.length;
        for(int i=0; i<len; i++){
            for(int j=i; j<len; j++){
                if(isIncreasingSubArray(arr, i, j)){
                    count++;
                }
            }
        }
        return count;
    }
    public boolean isIncreasingSubArray(int [] arr, int start, int end){
        int len = arr.length;
        int prev = 0;
        for(int i=0; i<len; i++){
            if(i<=end && i>= start){
                continue;
            }
            if(arr[i] <= prev){
                return false;
            }
            prev = arr[i];
        }
        return true;
    }
}