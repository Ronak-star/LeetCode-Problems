class Solution {
    public int isPrefixOfWord(String sentence, String searchWord) {
        int searchWordLength = searchWord.length();
        String[] words = sentence.split(" ");
        for(int i=0; i<words.length; i++){
            if(words[i].length() < searchWordLength){
                continue;
            }
            if(searchWord.equals(words[i].substring(0, searchWordLength))){
                  return i + 1;
            }
           
        }
         return -1;
    }
}