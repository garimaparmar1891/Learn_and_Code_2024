package model;

public class Wallet {
    private float balance;

    public Wallet(float initialAmount) {
        this.balance = initialAmount;
    }

    public float getBalance() {
        return balance;
    }

    public boolean debit(float amount) {
        if (balance >= amount) {
            balance -= amount;
            return true;
        }
        return false;
    }

    public void credit(float amount) {
        balance += amount;
    }
}
