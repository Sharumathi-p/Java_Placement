import java.util.*;
public class MaximunNumberOfTwo {
    public static void main(String[] args) {
        Scanner sc = new Scanner (System.in);
        int s = sc.nextInt();
        int b = sc.nextInt();
        display(s, b);
    }
    public static void display(int s, int b) {
        if (s>b) {
            System.out.println("Maximum Number: " +  s);
        } else {
            System.out.println("Maximum Number: " + b);
        }
    }
}
