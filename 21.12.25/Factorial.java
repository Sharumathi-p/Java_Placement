import java.util.*;
public class Factorial {
    public static void main(String[] args) {
        Scanner sc = new Scanner (System.in);
        int s = sc.nextInt();
        int fact = 1;
        for(int i=1;i<=s;i++) {
            fact *= i;
            
        }
        System.out.println(fact); 
    }
}
