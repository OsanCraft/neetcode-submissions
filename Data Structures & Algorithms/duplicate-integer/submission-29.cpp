class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        // loop through the array
        // if that specific item isnt in the hashmap,
        // add it to the hashmap
        // check if that item is in the hashmap
        // if not in hashmap after looping though array
        //return False
        // else, we return true
        
        unordered_set<int> seen;

        for (int num: nums){
            if(seen.count(num)){
                return true;
            }
            
            seen.insert(num);
        }
        return false;
    }
        
};