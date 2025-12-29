import java.util.*;
public class AmstrongNumber {
    public static void main(String[] args) {
        Scanner sc = new Scanner (System.in);
        int a = sc.nextInt();
        int temp = 0;
        int s = a;
        while(a>0) {
            int rem = a % 10;
            temp = temp + (rem * rem * rem);
            a = a / 10;
        } if (temp == s) {
            System.out.println("Amstrong Number");
        }else {
            System.out.println("Is not an Amstrong Number");
        }
    }
}