package chapter1;

/**
 * Created on 16/5/8.
 * author: robinjia
 * email: dengshilong1988@gmail.com
 */
public class Pleateau {
    public static int pleateau(int[] nums) {
        int length = 1;
        for (int i = 1; i < nums.length; i++) {
            if (nums[i] == nums[i - length]) {
                length++;
            }
        }
        return length;
    }

    public static int pleateaub(int[] nums) {
        int length = 1;
        int i = 0;
        while (i + length < nums.length) {
            if (nums[i] == nums[i + length]) {
                length++;
            } else {
                i += length;
                while (i < nums.length && i > 0 &&  nums[i] == nums[i - 1]) {
                    i--;
                }
            }
        }
        return length;
    }
    public static void main(String[] args) {
        int[] nums = {1, 2, 2, 3, 3, 3, 4, 5, 5, 5, 5, 6};
        System.out.println(pleateau(nums));
        System.out.println(pleateaub(nums));
    }
}
