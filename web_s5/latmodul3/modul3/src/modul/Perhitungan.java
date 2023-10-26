package modul;

public class Perhitungan {

    public int luas(balok balok){
        return balok.getPanjang() * balok.getLebar() * balok.getTinggi();
    }
    public int volume(balok balok){
        return 4*balok.getPanjang() * balok.getLebar() * balok.getTinggi();
    }

    public boolean isCube(int input) {
        return (Math.round(Math.cbrt(input))*Math.round(Math.cbrt(input))) * Math.round(Math.cbrt(input)) == input;
    }
}
