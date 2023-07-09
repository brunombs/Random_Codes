public class Animal {
    String nome;
    String cor;

    public void setNome(String nome){
        this.nome = nome;
    }

    public String getNome(){
        return nome;
    }

    public void Comer(){
        System.out.println("Eu gosto de comer.");
    }

    public void setCor(String cor){
        this.cor = cor;
    }

    public String getCor(){
        return cor;
    }

}
