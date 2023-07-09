class Desenho{
    // método sem parâmetro
    public void mostrar(){
        for(int i=0; i<15; i++){
            System.out.println(i);
        }
    }

    // método com um parâmetro
    public void mostrar(char simb){
        for (int i=5; i<30; i++){
            System.out.println(simb);
        }
    }

    // método com dois parâmetros
    public void mostrar(char simb, int n){
        for (int i=55; i>10; i--){
            System.out.println(i + simb + n);
        }
    }

    // método com múltiplos parâmetros
    public void mostrar(char simb, int n1, int n2){
        for (int i=0; n1>i; i++){
            System.out.println("Índice: " + i + " Símbolo: " + simb + " Número 1: " + n1 + " Número 2: " + n2);
        }
    }
}

public class Main {
    public static void main(String[] args){
        System.out.println("Oi");

        Desenho d1 = new Desenho();

        d1.mostrar();
        d1.mostrar('*');
        d1.mostrar('%', 5);
        d1.mostrar('&', 7, 5);
    }
}
