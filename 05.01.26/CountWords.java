import java.util.*;

public class CountWords {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter a string: ");
        String str = sc.nextLine();
        
        String[] words = str.trim().split("\\s+");
        int wordCount = words.length;
        
        System.out.println("Number of words: " + wordCount);
        sc.close();
    }
}
