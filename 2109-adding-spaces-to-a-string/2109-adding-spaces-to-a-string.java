class Solution {
    public String addSpaces(String s, int[] spaces) {
        StringBuilder sb = new StringBuilder();
        int spacesIndex = 0;
        for(int i=0; i<s.length(); i++){
            if(spacesIndex < spaces.length && i == spaces[spacesIndex]){
                sb.append(' ');
                spacesIndex++;
            }
            sb.append(s.charAt(i));

        }
        return sb.toString();
    }
}