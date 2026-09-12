class Solution {
    public int countConsistentStrings(String allowed, String[] words) {
        Set<Character> set = new HashSet<>();
        for(char ch : allowed.toCharArray()){
            set.add(ch);
        }
        int count = 0;
        for(String word : words){
          boolean isConsistent = true;
          for(int i=0; i<word.length(); i++){
            char currentChar = word.charAt(i);
            if(!set.contains(currentChar)){
                isConsistent = false;
                break;
            }
          }
          if(isConsistent){
            count++;
          }
        }
        return count;
    }
}