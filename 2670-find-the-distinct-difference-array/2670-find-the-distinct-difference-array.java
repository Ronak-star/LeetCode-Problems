class Solution {
    public int[] distinctDifferenceArray(int[] nums) {
        int [] diff = new int[nums.length];
        for(int i=0; i<nums.length; i++){
            Set<Integer> prefix = new HashSet<>();
            for(int j =0; j<=i; j++){
                prefix.add(nums[j]);
            }
            Set<Integer> suffix = new HashSet<>();
            for(int j=i+1; j<nums.length; j++){
                suffix.add(nums[j]);
            }
            diff[i] = prefix.size() - suffix.size();
        }
        return diff;
    }
}