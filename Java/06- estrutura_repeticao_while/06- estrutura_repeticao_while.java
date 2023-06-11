import java.util.Scanner;

class Main {
    public static void main(String[] args) {
        int option = 0;
        while (option != 999){
            System.out.println("Digite um valor qualquer ou 999 para sair");
            Scanner n1 = new Scanner(System.in);
            option = n1.nextInt();
        }
    }
}