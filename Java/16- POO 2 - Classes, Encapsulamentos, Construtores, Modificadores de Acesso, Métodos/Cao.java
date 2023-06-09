public class Cao{
    private int idade;
    private String cor;

    public void setCor(String c){
        cor = c;
    }

    public String getCor(){
        return cor;
    }

    public void setIdade(int i){
        idade = i;
    }

    public int getIdade(){
        return idade;
    }

    public boolean VerificarIdade(){
        if (idade>10){
            return true;
        }
        else{
            return false;
        }
    }
}