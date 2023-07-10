import java.util.ArrayList;
import java.util.Iterator;

public class Main {
    public static void main(String[] args) {
        ArrayList<Integer> numeros = new ArrayList<>();
        numeros.add(1);
        numeros.add(3);
        numeros.add(7);

        System.out.println("Array List: " + numeros);

        // Criando uma instância de Iterator
        Iterator<Integer> it = numeros.iterator();

        int numero = it.next();
        System.out.println(numero);

        while(it.hasNext()){
            it.forEachRemaining((value) -> System.out.println(value));
        }
    }
}