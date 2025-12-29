import java.util.*;
public class CountVoewlsAndConsonants {
    public static void main(String[] args) {
        Scanner sc=new Scanner (System.in);
        String s =sc.nextLine();
        int vcount = 0;
        int ccount = 0;

        for (int i=0;i<s.length();i++){
            char ch = s.charAt(i);
            if(ch=='a' || ch=='e' || ch=='i' || ch=='o' || ch=='u' || ch=='A' || ch=='E' || ch=='I' || ch=='O' || ch=='U') {
                vcount++;
            }else if (Character.isLetter(ch)) {
                ccount++;
            }
        }
        System.out.println("Vowels: " + vcount);
            System.out.println("Consonants: " + ccount);
        }
    }
