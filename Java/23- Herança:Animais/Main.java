class Main {
    public static void main(String[] args){
        Cachorro druid = new Cachorro();
        druid.setNome("Druid");

        Cachorro nino = new Cachorro();
        nino.setNome("Nino");

        Gato g = new Gato();
        g.setNome("Lola");

        Hamster h = new Hamster();
        h.setCor("preto");

        System.out.println("Cachorros: ");
        druid.mostrar();
        nino.mostrar();
        System.out.println();
        System.out.println("Gatos ");
        g.mostrar();
        System.out.println();
        System.out.println("Hamster: ");
        h.mostrar();
    }
}
