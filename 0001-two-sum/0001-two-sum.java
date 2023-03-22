class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> found = new HashMap<>();
        int[] ans = new int[2];
        for(int i=0; i<nums.length; i++){
            if(null == found.get(nums[i])){
                found.put(target - nums[i], i);
            }else{
                ans[0] = found.get(nums[i]);
                ans[1] = i;
            }
        }
        return ans;
    }
}