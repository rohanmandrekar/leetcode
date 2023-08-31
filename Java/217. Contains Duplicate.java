class Solution {
    public boolean containsDuplicate(int[] nums) {
        Set<Integer> dist = new HashSet<>();

        for(int i=0; i<nums.length; i++){
            if(dist.contains(nums[i])) return true;

            dist.add(nums[i]);
        }

        return false;

    }
}