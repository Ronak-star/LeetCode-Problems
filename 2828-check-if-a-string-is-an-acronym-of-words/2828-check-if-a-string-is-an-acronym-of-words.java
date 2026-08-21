class Solution {
    public boolean isAcronym(List<String> words, String s) {
        StringBuilder acronym = new StringBuilder();
        for(String word : words){
            char  ch  = word.charAt(0);
            acronym.append(ch);
        }
        if(acronym.toString().equals(s)){
            return true;
        }
        return false;
    }
}