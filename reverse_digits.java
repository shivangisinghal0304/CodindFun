import java.util.*;

class Reverse {
    String x = new String("");
    int n;
    void getdata() {
        System.out.println("Enter a number to reverse");
        Scanner s = new Scanner(System.in);
        n = s.nextInt();
    }

    void compute() {
        int copy_n = n;
        while(n != 0) {
            int rem = n % 10;
            x += rem;
            n /= 10;
        }
    }
    void printdata() {
        System.out.println("The number in reverse is: " + (x));
    }

    public static void main(String args[]) {
        Reverse n = new Reverse();
        n.getdata();
        n.compute();
        n.printdata();
    }
}