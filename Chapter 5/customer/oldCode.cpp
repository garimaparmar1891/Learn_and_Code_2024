//Given code
public class Customer {
    private String firstName;
    private String lastName;
    private Wallet myWallet;

    public String getFirstName() { return firstName; }
    public String getLastName() { return lastName; }
    public Wallet getWallet() { return myWallet; }
}

public class Wallet {
    private float value;

    public float getTotalMoney() { return value; }
    public void setTotalMoney(float newValue) { value = newValue; }
    public void addMoney(float deposit) { value += deposit; }
    public void subtractMoney(float debit) { value -= debit; }
}

Wallet theWallet = myCustomer.getWallet();
if (theWallet.getTotalMoney() > payment) {
    theWallet.subtractMoney(payment);
} else {
    // come back later and get my money
}

// The client code is reaching deep into Customer, pulling out its internals Wallets details, and then manipulating it.
// This is a violation of encapsulation and law of demeter.
// We are reaching through one object to access another (customer → wallet → value). This tight coupling makes the code fragile.
