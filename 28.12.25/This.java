
class A{
    String name;
    int num;
    A() {
        this.name=name;
        this.num=num;
    }
    void display(){
        System.out.println(name + " " + num);
    }
}
public class This {
    public static void main(String[] args) {
        A obj = new A("Sharaa", 19);
        obj.display();
        obj.display();
    }
}
