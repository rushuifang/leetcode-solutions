class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        map<int, int> index;
        
        for (int i=0; i<nums.size(); i++)
        {
            int compensate = target - nums[i];
            if (index.find(compensate) != index.end())
            {
                return {i, index.find(compensate)->second};
            }
            index.insert(pair<int,int>(nums[i],i));
        }
        return {};
    }
};