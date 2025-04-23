package service;

import model.Customer;
import model.Wallet;

public class CustomerWalletService {
    private Customer customer;
    private Wallet wallet;

    public CustomerWalletService(Customer customer, float initialAmount) {
        this.customer = customer;
        this.wallet = new Wallet(initialAmount);
    }

    public boolean makePayment(float amount) {
        return wallet.debit(amount);
    }

    public void addMoney(float amount) {
        wallet.credit(amount);
    }

    public float checkBalance() {
        return wallet.getBalance();
    }

}
