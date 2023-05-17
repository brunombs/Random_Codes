import java.util.ArrayList;

class Main {
    public static void main(String[] args) {
        ArrayList<String> estados = new ArrayList<>();

        estados.add("Bahia");
        estados.add("Rio de Janeiro");
        System.out.println(estados);
        estados.remove("Rio de Janeiro");
        System.out.println(estados);
        estados.contains("Bahia");
    }
}