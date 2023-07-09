class Faculdade{
    private double duracao;

    public void setDuracao(double duracao){
        this.duracao = duracao;
    }

    public double getDuracao(){
        return duracao;
    }

    public void mostrarInformacao(){
        System.out.println("Faculdade de Tecnologia, duração média: " + getDuracao() + " anos");
    }
}

class ADS extends Faculdade{
    public void mostrarInformacao(){
        System.out.println("Faculdade de Análise e Desenvolvimento de Sistemas, duração: " + getDuracao() + " anos");
    }
}

class CC extends Faculdade{
    public void mostrarInformacao(){
        System.out.println("Faculdade de Ciências da Computação, duração: " + getDuracao() + " anos");
    }
}

class EC extends Faculdade{
    public void mostrarInformacao(){
        System.out.println("Faculdade de Engenharia da Computação, duração: " + getDuracao() + " anos");
    }
}

public class Main {
    public static void main(String[] args) {
        Faculdade f1 = new Faculdade();
        f1.setDuracao(3.66);
        f1.mostrarInformacao();

        ADS f2 = new ADS();
        f2.setDuracao(2.5);
        f2.mostrarInformacao();

        CC f3 = new CC();
        f3.setDuracao(3.5);
        f3.mostrarInformacao();

        EC f4 = new EC();
        f4.setDuracao(5);
        f4.mostrarInformacao();
    }
}