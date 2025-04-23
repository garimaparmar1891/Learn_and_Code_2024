import model.Customer;
import service.CustomerWalletService;

public class Main {
    public static void main(String[] args) {
        Customer customer = new Customer("garima", "parmar");
        CustomerWalletService walletService = new CustomerWalletService(customer, 100.0f);

        walletService.addMoney(50.0f);
        System.out.println("Balance after adding money : " + walletService.checkBalance());

        boolean success = walletService.makePayment(120.0f);
        System.out.println("Final Balance : " + walletService.checkBalance());
    }
}

// The code follows SOLID principles by separating responsibilities between Customer, Wallet, and CustomerWalletService.
// Improving clarity and maintainability.
// Restricts direct wallet access to ensure better data protection.
