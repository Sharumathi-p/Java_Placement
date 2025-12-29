public class BankAccountDetails {
    int num ;
    double deposit ;
    BankAccountDetails(){
        num = 12345678;
        deposit = 5000.00;
        System.out.println("Current Balance: " + deposit);
    }
    void add(double a){
        deposit += a;
        System.out.println("New Balance : " +deposit);
    }
    void sub(double b) {
        if (deposit<b) {
            System.out.println("Insufficient Balance : ");
        }
        else {
            deposit -=b;
            System.out.println("New Balance : " + deposit);
        }
    }
    public static void main(String[] args){
        BankAccountDetails account = new BankAccountDetails();
        account.add(2000.00);
        account.sub(3000.00);
        account.sub(5000.00);
    }
    }
