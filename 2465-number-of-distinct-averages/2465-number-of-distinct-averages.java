class Solution {
    public int distinctAverages(int[] nums) {
        Arrays.sort(nums);
        int left = 0, right = nums.length - 1;
        Set<Integer> set = new HashSet<>();
        while(left<right){
            int avg = nums[left] + nums[right];
            set.add(avg);
            left++;
            right--;
        }
        return set.size();
    }
}