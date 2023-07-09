public class Main {
    public static void main(String[] args) {
        Pessoa p = new Pessoa();
        p.nome = "Bruno";
        Vendedor v = new Vendedor();
        v.comissao = 11.50;
        v.nome = "Estevan";
        System.out.println(p.nome);
        System.out.println("A comissão de " + v.nome + " é: " + v.comissao);
    }
}
