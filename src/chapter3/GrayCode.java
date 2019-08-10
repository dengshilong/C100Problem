package chapter3;

/**
 * Created on 16/5/21.
 * author: robinjia
 * email: dengshilong1988@gmail.com
 */
import java.util.ArrayList;
import java.util.List;


public class GrayCode {
    public static List<Integer> grayCode(int n) {
        List<Integer> result = new ArrayList<Integer>();
        if (n == 0) {
            result.add(0);
        } else {
            List<Integer> temp = grayCode(n-1);
            for (Integer i: temp) {
                result.add(i);
            }
            int front = 1 << (n - 1);
            for (int i = temp.size() - 1; i >= 0; i--) {
                result.add(temp.get(i) + front);
            }
        }
        return result;
    }
    public static void main(String[] args) {
        List<Integer> result = grayCode(4);
        for (Integer i: result) {
            System.out.println(i);
        }
    }
}
