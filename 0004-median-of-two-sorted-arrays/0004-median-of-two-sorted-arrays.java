class Solution {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        
        int[] nums3 = new int[nums1.length + nums2.length];
        int i = 0, j = 0, k = 0;
        double median = 0.0;

        while (i < nums1.length && j < nums2.length) {
            if (nums1[i] < nums2[j])
                nums3[k++] = nums1[i++];
            else
                nums3[k++] = nums2[j++];
        }
        while (i < nums1.length)
            nums3[k++] = nums1[i++];

        while (j < nums2.length) {
            nums3[k++] = nums2[j++];

        }

        if (nums3.length % 2 != 0) {
            median = nums3[Math.floorDiv(nums3.length, 2)];
        } else {
            int mid_index = nums3.length / 2;
            median = (nums3[mid_index] + nums3[mid_index - 1]) / 2.0;
        }
        return median;
    }
    
}
