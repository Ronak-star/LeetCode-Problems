class Solution {
    public int[][] mergeArrays(int[][] nums1, int[][] nums2) {
        Map<Integer, Integer> map = new TreeMap<>();
        for(int [] num : nums1){
            map.put(num[0], num[1]);
        }
        for(int [] num : nums2){
            if(map.containsKey(num[0])){
               
                 map.put(num[0], map.get(num[0]) + num[1]);

            }
                else{
                    map.put(num[0], num[1]);
                }
            }
            int[] [] res = new int[map.size()][2];
            int i = 0;
            for(Map.Entry<Integer, Integer> entry : map.entrySet()){
                res[i] [0]  = entry.getKey();
                res[i]  [1] = entry.getValue();
                i++;
            }
            return res;
        }
    }
