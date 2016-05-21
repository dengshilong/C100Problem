package chapter3;

/**
 * Created on 16/5/21.
 * author: robinjia
 * email: dengshilong1988@gmail.com
 */
public class IntPartition {
    public static int partition(int n) {
        return _partition(n, n);
    }
    private static int _partition(int n, int m) {
        if (n < 0) {
            return 0;
        }
        if (n == 0 || m == 1) {
            return 1;
        }
        return _partition(n - m, m) + _partition(n, m - 1);
    }
    public static void main(String[] args) {
        for (int i = 0; i < 10; i++) {
            System.out.println(i + " " + partition(i));
        }
    }
}
