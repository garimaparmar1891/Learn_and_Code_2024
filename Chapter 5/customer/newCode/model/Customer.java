public class Customer {
    private String firstName;
    private String lastName;
    private Wallet wallet;

    public Customer(String firstName, String lastName, float initialBalance) {
        this.firstName = firstName;
        this.lastName = lastName;
        this.wallet = new Wallet(initialBalance);
    }

    public String getFirstName() { return firstName; }
    public String getLastName() { return lastName; }

    public boolean makePayment(float amount) {
        if (wallet.hasSufficientBalance(amount)) {
            wallet.withdraw(amount);
            return true;
        }
        return false;
    }
}
