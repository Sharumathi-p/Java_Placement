import java.util.*;
class Train {
    static void TrainSeat(int a) {
        switch(a%8) {
            case 1:
            case 4:
                System.out.println("Lower Berth");
                break;
            case 2:
            case 5:
                System.out.println("Middle Berth");
                break;
            case 3:
            case 6:
                System.out.println("Upper Berth");
                break;
            case 7:
                System.out.println("Side Lower Berth");
                break;
            case 0:
                System.out.println("Side Upper Berth");
                break;
            default:
                System.out.println("Invaid Number");
        } 
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        TrainSeat(n);
    }}

