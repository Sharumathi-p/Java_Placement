
import java.util.*;
public class numbers {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int temp = n;
        int rev = 0;
        int count = 0;
        int check = n;
        while (check != 0) {
            count++;
            check = check / 10;
        }
        if (count != 4) {
            System.out.println("Enter the number: ");
        } else {
            while (temp != 0) {
                rev = rev * 10 + temp % 10;
                temp = temp / 10;
            }
            System.out.println(rev);
        }
        sc.close();
    }
}
    