class Main {
    public static void main(String[] args) {
        Cao cachorro = new Cao();
        cachorro.setIdade(15);
        cachorro.setCor("dourado");
        System.out.println("Cor do cachorro: " + cachorro.getCor());

        if(cachorro.VerificarIdade()){
            System.out.println("Ele é idoso");
        }
        else{
            System.out.println("Ele é novinho");
        }
    }
}