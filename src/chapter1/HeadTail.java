package chapter1;

/**
 * Created on 16/5/8.
 * author: robinjia
 * email: dengshilong1988@gmail.com
 */
public class HeadTail {
    public static int headTail(int[] nums) {
        int i = 0;
        int j = nums.length - 1;
        int prefix = 0;
        int suffix = 0;
        int result = 0;
        while (i < nums.length && j >= 0) {
            System.out.println(prefix + " " + suffix + " " + i + " " + j);
            if (prefix == suffix) {
                prefix += nums[i++];
                suffix += nums[j--];
                result++;
            } else if (prefix > suffix) {
                suffix += nums[j--];
            } else {
                prefix += nums[i++];
            }
        }
        return result;
    }
    public static void main(String[] args) {
        int[] nums = {3, 6, 2, 1, 4, 5, 2};
        System.out.println(headTail(nums));
    }
}
