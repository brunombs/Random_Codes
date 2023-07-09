import java.util.Scanner;


class Main {
    public static void main(String[] args){
    Scanner s = new Scanner(System.in);
    try {
        System.out.println("Digite o primeiro número inteiro: ");
        int numero1 = s.nextInt();
        System.out.println("O valor digitado foi: " + numero1);
        System.out.println("Digite o segundo número inteiro: ");
        int numero2 = s.nextInt();
        System.out.println("O valor digitado foi: " + numero2);
        int soma = numero1 + numero2;
        System.out.println("A soma entre os dois valores é: " + soma);
    } catch (Exception ex){
      System.out.println("ERRO - O número digitado não é um número");
    }
    }
}
