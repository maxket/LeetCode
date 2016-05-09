public class Solution {
    public int[] twoSum(int[] nums, int target) {
        int[] result = new int[2];
        
        if (nums == null || nums.length < 2) {
            return result;
        }
        
        HashMap<Integer, Integer> numMap = new HashMap<Integer, Integer>();
        
        for (int i = 0; i < nums.length; i++) {
            int left = target - nums[i];
            if (numMap.containsKey(left)) {
                result[0] = numMap.get(left);
                result[1] = i;
                return result;
            } else {
                numMap.put(nums[i], i);
            }
        }
        
        return result;
    }
}
