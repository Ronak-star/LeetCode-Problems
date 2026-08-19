class Solution {
    public int vowelStrings(String[] words, int left, int right) {
        int count = 0;
        for(int i=left; i<=right; i++){
            if(checkVowel(words[i])){
                count++;
            }
        }
        return count;
    }
    private static boolean checkVowel(String str){
        if(str.charAt(0) == 'a' || str.charAt(0) == 'e' || str.charAt(0) == 'i' || str.charAt(0) == 'o' || str.charAt(0) == 'u' ){

if(str.charAt(str.length() - 1) == 'a' || str.charAt(str.length() - 1) == 'e' || str.charAt(str.length() - 1) == 'i' || str.charAt(str.length() - 1) == 'o' || str.charAt(str.length() - 1) == 'u' ){

    return true;
}

         
        }
        return false;
    }
}