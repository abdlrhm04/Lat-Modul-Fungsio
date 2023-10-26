package modul;
import java.util.Scanner;

public class main {

    public static void main(String[] args) {
        Scanner inp = new Scanner(System.in);
        balok balok = new balok();
        System.out.print("Masukkan Panjang : ");
        balok.setPanjang(inp.nextInt());
        System.out.print("Masukkan Lebar : " );
        balok.setLebar(inp.nextInt());
        System.out.print("Masukkan Tinggi : ");
        balok.setTinggi(inp.nextInt());
        balok.hasil();
    }
}
