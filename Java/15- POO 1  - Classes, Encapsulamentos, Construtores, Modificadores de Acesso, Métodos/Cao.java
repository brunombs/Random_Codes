public class Cao{
    String nome;
    String cor;
    int idade;
    double peso;

    public Cao(){
        cor = "caramelo";
    }

    public Cao(String nome, int idade){
        this.nome = nome;
        this.idade = idade;
    }

    public void Anda(){
        System.out.println("Estou andando...");
    }

    public void DadosCao(){
        System.out.println("Hi, my name is: " + nome + " and I am " + idade + " years old");
    }
}