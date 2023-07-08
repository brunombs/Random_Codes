class Main {
    public static void main(String[] args) {
        Conta cp = new Poupanca();
        cp.depositar(750);
        cp.getSaldo();
        cp.sacar(350);
        cp.getSaldo();
    }
}
