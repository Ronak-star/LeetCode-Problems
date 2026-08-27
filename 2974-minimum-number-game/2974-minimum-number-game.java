class Solution {
    public int[] numberGame(int[] nums) {
        int[] arr = new int[nums.length];
        Arrays.sort(nums);
        int bob = 0, alice = 1;
        for(int i=1; i<nums.length; i = i +2){
            arr[bob] = nums[i];
            bob += 2;
        }
        for(int i=0; i<nums.length; i= i + 2){
            arr[alice] = nums[i];
            alice += 2;
        }
        return arr;
    }
}