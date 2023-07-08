abstract class Conta {
    private double saldo;
    private double credito;

    public void setSaldo(double saldo){
        this.saldo = saldo;
    }

    public void setCredito(double credito){
        this.credito = credito;
    }

    public double getSaldo(){
        return saldo;
    }

    public double getCredito(){
        return credito;
    }

    public abstract void imprimeExtrato();

}