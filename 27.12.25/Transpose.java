import java.util.*;
public class Transpose {
    public static void main(String[] args) {
        Scanner  sc = new Scanner (System.in);
        int s=sc.nextInt();
        int a=sc.nextInt();
        int[][] mat=new int[s][a];
        for (int i=0;i<s;i++){
            for (int j=0;j<a;j++) {
                mat[i][j] = sc.nextInt();
            }
        }
        for (int j=0;j<a;j++) {
            for (int i=0;i<s;i++) {
                System.out.print(mat[i][j] + " ");
            }
            System.out.println();
        }
    }
}
