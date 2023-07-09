import java.util.Scanner;
class Linguagem{
    public Linguagem(String linguagem){
        System.out.println("A linguagem de programação é: " + linguagem);
    }
}

class Main{
    public static void main(String[] args){
        Scanner qualLingua = new Scanner(System.in);
        System.out.println("Digite a linguagem de programação:");
        String linguagem = qualLingua.nextLine();
        Linguagem um = new Linguagem(linguagem);

    }
}