package chapter2;

/**
 * Created on 16/5/21.
 * author: robinjia
 * email: dengshilong1988@gmail.com
 */
public class RecursionPower {
    public static long recursionPower(long m, long n) {
        if (n == 0)
            return 1;
        long result = 1;
        if (n % 2 == 1) {
            result = m * recursionPower(m * m, n / 2);
        } else {
            result = recursionPower(m * m, n / 2);
        }
        return result;
    }
    public static void main(String[] args) {
        System.out.println(recursionPower(2, 4));
        System.out.println(recursionPower(3, 9));
        System.out.println(recursionPower(28, 23));
    }
}
