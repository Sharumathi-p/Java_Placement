import java.util.*;
public class BubbleShort {
    public static void main(String[] args) {
        Scanner sc = new Scanner (System.in);
        arr n = sc.nextInt();
        int [] arr = new int[n];
        int c =0;
        for(int i=0;i<n;i++) {
            arr[i] = sc.nextInt();
        }
        for(int i=0;i<n;i++){
            for(int j=0;j<n-i-1;j++){
                if(arr[j]>arr[j+1]) {
                    int temp = arr[j];
                    arr[j] = arr[j+1];
                    arr[j+1] = temp;
                }
            }c++;
        }        System.out.println("Number of passes: " + c);
        for(int i=0;i<n;i++) {
            System.out.print(arr[i]+" ");
        }

    }
}

