class Animal {
    void Eat() {
        System.out.println("Eats");
    }
}

class Dog extends Animal {
    void Bark() {
        System.out.println("Barks");
    }
}

class Cat extends Dog {
    void Sleep() {
        System.out.println("Sleeps");
    }
}

public class MultiLevelInheritance {
    public static void main(String[] args) {
        Cat obj = new Cat();
        obj.Eat();  
        obj.Bark();  
        obj.Sleep();
    }    
}