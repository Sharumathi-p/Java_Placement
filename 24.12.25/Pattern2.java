import java.util.*;
public class Pattern2 {
    public static void main(String[] args) {
        Scanner sc=new Scanner (System.in);
        int s =sc.nextInt();
        for (int i=0;i<=s;i++) {
            for (int j=0;j<=s-i;j++) {
            System.out.print(" ");
        }
        for (int k=0;k<=s;k++) {
            System.out.print("*");
        }
        System.out.println();
        sc.close();
    }
}
}
