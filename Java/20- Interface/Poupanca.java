public class Poupanca implements Conta {
    private double saldo;

    public void depositar(double valor) {
        this.saldo += valor;
        System.out.println("Valor depositado: " + valor);
    }

    public double getSaldo() {
        System.out.println("Saldo: " + this.saldo);
        return this.saldo;
    }

    public void sacar(double valor) {
        this.saldo -= valor;
        System.out.println("Valor sacado: " + valor);
    }
}
