class Solution {
public:
vector<vector<int>> arr;

void helper(int i,vector<int>& nums,vector<int> ans){
    if(i==nums.size()){
        arr.push_back(ans);
        return; //Base condition
    }

    // include
    ans.push_back(nums[i]);
    helper(i+1, nums, ans);
    //backtraking
    ans.pop_back();
    // exclude
    helper(i+1,nums, ans);
}
    vector<vector<int>> subsets(vector<int>& nums) {
        vector<int>ans;
        helper(0,nums,ans);
        return arr;
        /*
        vector<vector<int>> res = {{}};
        for (int num : nums) {
            int n = res.size();
            for (int i = 0; i < n; i++) {
                vector<int> subset = res[i];
                subset.push_back(num);
                res.push_back(subset);
            }
        }
        return res;
        */


/*
        vector<vector<int>> res;
        vector<int> path;
        solve(nums, 0, path, res);
        return res;
    }
    
private:
    void solve(vector<int>& nums, int index, vector<int>& path, vector<vector<int>>& res) {
        // Base case: processed all elements, record this subset
        if (index == nums.size()) {
            res.push_back(path);
            return;
        }
        
        // Choice 1: exclude nums[index]
        solve(nums, index + 1, path, res);
        
        // Choice 2: include nums[index]
        path.push_back(nums[index]);
        solve(nums, index + 1, path, res);
        path.pop_back(); // backtrack
*/






    }
};