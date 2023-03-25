class Solution {
    public void moveZeroes(int[] nums) {
        int zp = 0;
        for(int i = 0; i<nums.length;i++){
            if(nums[i] != 0){
            nums[zp++] = nums[i];    
            }
            
        }
        while(zp<nums.length){
            nums[zp++]=0;
        }
        
    }
}