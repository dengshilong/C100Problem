package chapter1;

/**
 * Created on 16/5/8.
 * author: robinjia
 * email: dengshilong1988@gmail.com
 */

/*
可以用变量prefix来表示前置和，用suffix来表示后置和，
用i表示前置和累加元素的位置，i从前往后加，用j表示后置和累加元素的位置, j从后往前加。
当prefix > suffix时，累加后置和，也就是j向前走；
当prefix < suffix时，累加前置和，也就是i往后走；
当prefix == suffix时，同时累加前置和与后置和，也就是i往后走，j往前走
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
