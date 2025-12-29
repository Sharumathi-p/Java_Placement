import java.io.*;
class DAY8{
    public static void main(String[] args)throws IOException {
        File f=new File("C:\\Sharaa\\Buttaa");
        f.mkdir();
        File f2 = new File("C:\\Sharaa\\Buttaa\\Kuttie");
        f2.mkdirs();
        File f3 = new File("C:\\Sharaa\\Buttaa\\Kuttie\\s2k.txt");
        f3.createNewFile();
    }
}
