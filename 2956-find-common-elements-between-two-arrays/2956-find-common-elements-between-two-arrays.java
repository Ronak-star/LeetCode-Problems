class Solution {
    public int[] findIntersectionValues(int[] nums1, int[] nums2) {
        int [] answer = new int[2];
        int count1[] = new int[101];
        int count2[] = new int[101];
        for(int i=0; i<nums1.length; i++){
            count1[nums1[i]]++;
        }
        for(int i=0; i<nums2.length; i++){
            count2[nums2[i]]++;
        }
        int result1 = 0, result2 = 0;
        for(int i=1; i<=100; i++){
            if(count2[i] >= 1){
                result1 += count1[i];
            }
            if(count1[i] >= 1){
                result2 += count2[i];
            }
        }
        answer[0] = result1;
        answer[1] = result2;
        return answer;
    }
}