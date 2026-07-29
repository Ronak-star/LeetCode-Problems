class Solution {
public:
    vector<vector<int>> subsets(vector<int>& nums) {
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
    }
};