class Solution {
    public boolean checkIfExist(int[] arr) {
        Map<Integer, Integer> map = new HashMap<>();
        for(int i=0; i<arr.length; i++){
            int doub = 2 * arr[i];
            int half = arr[i] / 2;
            if(map.containsKey(doub) || (arr[i] % 2 == 0 && map.containsKey(half))){
                return true;
            }
            else{
                map.put(arr[i], 1);
            }
        }
        return false;
    }
}