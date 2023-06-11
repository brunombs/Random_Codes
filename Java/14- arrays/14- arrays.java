import java.util.ArrayList;

class Main {
    public static void main(String[] args) {
        ArrayList<String> bandas = new ArrayList<String>();

        bandas.add("Charlie Brown Jr");
        bandas.add("Avenged Sevenfold");
        System.out.println(bandas);
        bandas.add(bandas.indexOf("Avenged Sevenfold"), "RHCP");
        System.out.println(bandas);
        bandas.remove("RHCP");
        System.out.println(bandas);
        bandas.clear();
        System.out.println(bandas);
    }
}