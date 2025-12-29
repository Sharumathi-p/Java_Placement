class Animal {
    void bark() {
        System.out.println("Barks");
    }
}
class Dog extends Animal {
void eat() {
    System.out.println("Eats");
}
}


public class SingleInheritance {
    public static void main (String[] args) {
        Dog obj = new Dog();
        obj.bark();
        obj.eat();
    }
}