class Solution {
    public int findSpecialInteger(int[] arr) {
        int limit = arr.length / 4;
        for(int i=0; i<arr.length - limit; i++){
            if(arr[i] == arr[i + limit]){
                return arr[i];
            }
        }
        return -1;
    }
}