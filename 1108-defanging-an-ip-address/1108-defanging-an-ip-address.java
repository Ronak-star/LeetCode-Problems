class Solution {
    public String defangIPaddr(String address) {
        StringBuilder sb = new StringBuilder();
        char chars[] = address.toCharArray();
        for(char ch : chars){
            if(ch == '.'){
                sb.append("[.]");
            }
            else{
                sb.append(ch);
            }
        }
        return sb.toString();
    }
}