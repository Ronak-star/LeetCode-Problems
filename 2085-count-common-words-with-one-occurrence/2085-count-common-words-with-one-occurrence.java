class Solution {
    public int countWords(String[] words1, String[] words2) {
        Map<String,Integer> map = new HashMap<String,Integer>();
        for(int i=0; i<words1.length; i++){
            if(map.containsKey(words1[i])){
                map.put(words1[i], map.get(words1[i] )+ 1);

            }
            else{
                map.put(words1[i], 1);
            }
        }
        for(String word : words2){
            if(map.containsKey(word)){
                if(map.get(word) <= 1){
                    map.put(word, map.get(word) - 1);
                }
            }
        }
        int count = 0;
        for(String word : words1){
            if(map.get(word) == 0){
                count++;
            }
        }
        return count;
    }
}