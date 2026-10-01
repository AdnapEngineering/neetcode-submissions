class Solution {
    public boolean hasDuplicate(int[] nums) {
        Set<Integer> seen = new HashSet<>();

        for(int num: nums){ //for each as we don't care about indicies and altering num
            if(!seen.add(num)){
                return true;
            }
        }
        return false;
    }
}