class Solution {
public:
    int majorityElement(vector<int>& nums){
        // 1. using Brute force algo
 // int n = nums.size(); 

   //    for(int val : nums){
  //        int freq = 0;

  //        for(int el : nums){
  //            if(el == val){
  //                freq++;
  //            }
  //        }
  //        if(freq > n/2){
  //            return val;
  //        }
  //    }
  //return -1;
  //}


// 2.using shorting

  // sort
 // sort(nums.begin(), nums.end());


  //freq count
 // int freq = 1, ans = nums[0];
 // for(int i=1; i<n; i++){
 //   if(nums[i] == nums [i-1]){
 //       freq++;
 //   }else{
 //       freq = 1;
 //       ans = nums[i];
 //   }
 //   if(freq > n/2){
 //       return ans;
 //   }
//
 // }
 //   
 // return ans;
 //   }
//

// using moores voting algo

    int freq = 0 , ans = 0;

    for(int i=0; i<nums.size(); i++){
        if(freq == 0){
            ans = nums[i];
        }
        if(ans == nums[i]){
            freq++;

        }
        else{
            freq--;
        }
    }
    return ans;
    }
};