public class Wallet {
    private float balance;

    public Wallet(float initialValue) {
        this.balance = initialValue;
    }

    public float getBalance() { return balance; }
    public void setBalance(float newValue) { this.balance = newValue; }
    public void deposit(float amount) { this.balance += amount; }
    public void withdraw(float amount) { this.balance -= amount; }

    public boolean hasSufficientBalance(float amount) {
        return this.balance >= amount;
    }
}
