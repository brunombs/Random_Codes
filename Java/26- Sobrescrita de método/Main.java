class Linguagem{
    public void mostrarInformacao(){
        System.out.println("Lingua portuguesa");
    }
}

class Java extends Linguagem {
    public void mostrarInformacao(){
        System.out.println("Linguagem de programação Java");
    }
}

class R extends  Linguagem {
    public void mostrarInformacao(){
        System.out.println("Linguagem de programação R");
    }
}

class Main{
    public static void main(String[] args){
        Linguagem linguagem1 = new Linguagem();
        linguagem1.mostrarInformacao();

        Java java1 = new Java();
        java1.mostrarInformacao();

        R r1 = new R();
        r1.mostrarInformacao();
    }
}