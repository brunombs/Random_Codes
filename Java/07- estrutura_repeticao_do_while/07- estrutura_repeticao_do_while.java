import java.util.Scanner;

class Main {
    public static void main(String[] args) {
        int option;

        do{
            System.out.println("Digite um valor ou 999 para sair");
            Scanner n1 = new Scanner(System.in);
            option = n1.nextInt();
        }while (option != 999);
    }
}