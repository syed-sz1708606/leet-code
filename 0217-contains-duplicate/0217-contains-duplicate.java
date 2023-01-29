class Solution {
      public boolean containsDuplicate(int[] nums) {
	       final Set<Integer> numbers = new HashSet<Integer>();
            for(int num: nums){
                if(numbers.contains(num)){
                    return true; 
                }
                else{
                    numbers.add(num);
                }
            }
          return false; 
	    }
}