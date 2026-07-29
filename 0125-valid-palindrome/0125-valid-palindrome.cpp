class Solution {
public:
 bool isPalindrome(string s){
    /*
   if((ch >= '0' && ch <= '9') || 
    (tolower(ch)  >= 'a' && tolower(ch) <= 'z')){
             return true;
    }
    return false;
 }
    bool isPalindrome(string s) {
        int st = 0, end = s.length()-1;

        while(st < end){
            if(!isAlphaNum(s[st])){
                st++; continue;
            }
            if(!isAlphaNum(s[end])){
                end--; continue;
            }
            if(tolower(s[st]) != tolower(s[end])){
                return false;
            }
            st++; end--;
        }
         return true;
    }
    */
 
 int start=0;
 int end=s.length()-1;
 while(start<=end){
    if(!isalnum(s[start])){
        start++;
        continue;
    }
      if(!isalnum(s[end])){

                end--; 
                continue;
            }
  if(tolower(s[start]) != tolower(s[end])){
                return false;
  }
                else{
                    start++;
                    end--;
                }
            }
            return true;

    }
 
   
};