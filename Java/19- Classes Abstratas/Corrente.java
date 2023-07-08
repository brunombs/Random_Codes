public class Corrente extends Conta {

    public void imprimeExtrato(){
        System.out.println("Saldo na conta corrente: " + this.getSaldo());
        System.out.println("Crédito na conta corrente: " + this.getCredito());
    }
}
