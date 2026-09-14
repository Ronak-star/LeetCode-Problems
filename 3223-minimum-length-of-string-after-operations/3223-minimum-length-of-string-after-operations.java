class Solution {
    public int minimumLength(String s) {
        Map<Character, Integer> map = new HashMap<>();
        for(int i=0; i<s.length(); i++){
            map.put(s.charAt(i), map.getOrDefault(s.charAt(i), 0) + 1);

        }
        int count = 0;
        for(Map.Entry<Character, Integer> entry : map.entrySet()){
            int val = entry.getValue();
            count += (val % 2 == 1) ? val - 1 : val - 2;
        }
        return s.length() - count;
    }
}