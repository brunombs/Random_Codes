class Main {
    public static void main(String[] args) {
        Conta cp = new Poupanca();
        cp.setSaldo(5000);

        Conta cc = new Corrente();
        cc.setSaldo(3000);
        cc.setCredito(7520);

        cp.imprimeExtrato();
        cc.imprimeExtrato();

    }
}