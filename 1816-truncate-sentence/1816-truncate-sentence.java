class Solution {
    public String truncateSentence(String s, int k) {
        int len = s.length();
        String words[] = s.split(" ");
        StringBuilder sb = new StringBuilder();
        int index = 0;
        while(k != 0){
            sb.append(words[index] + " ");
            index++;
            k--;
        }
        return sb.toString().trim();
    }
}