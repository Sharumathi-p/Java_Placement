import java.util.*;
public class Pattern {
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        int s=sc.nextInt();
        for (int i=0;i<=s;i++) {
            System.out.print("*");
        }
        for (int j=0;j<=s;j++) {
            System.out.print("*");
        }
        System.out.println(" ");
        sc.close();
    }
}
