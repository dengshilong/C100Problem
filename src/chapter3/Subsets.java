package chapter3;

/**
 * Created on 16/5/21.
 * author: robinjia
 * email: dengshilong1988@gmail.com
 */
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;


public class Subsets {
    public static List<List<Integer>> subsets(int[] nums) {
        List<List<Integer>> res = new ArrayList<List<Integer>>();
        if (nums.length == 0)
            return res;
        int[] temp = Arrays.copyOf(nums, nums.length);
        Arrays.sort(temp);
        res = subsets(temp, 0, temp.length - 1);
        return res;
    }
    private static List<List<Integer>>subsets(int[] nums, int start, int end) {
        List<List<Integer>> result = new ArrayList<List<Integer>>();
        if (start > end) {
            result.add(new ArrayList<Integer>());
            return result;
        } else {
            List<List<Integer>> temp = subsets(nums, start + 1, end);
            for (List<Integer> t: temp) {
                List<Integer> s = new ArrayList<Integer>(t);
                result.add(s);
                t.add(0, nums[start]);
                result.add(t);
            }
        }
        return result;
    }
    public static void main(String[] args) {
        int[] nums = {1, 2, 3, 4};
        List<List<Integer>> result = subsets(nums);
        System.out.println(result.size());
        for (List<Integer> t: result) {
            for (Integer i: t) {
                System.out.print(i + " ");
            }
            System.out.println("");
        }
    }
}
