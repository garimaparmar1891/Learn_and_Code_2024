import customer.newCode.model.Customer;
import customer.newCode.service.PaymentService;

public class Main {
    public static void main(String[] args) {
        //dummy data
        Customer myCustomer = new Customer("garima", "parmar", 10.00);
        PaymentService paymentService = new PaymentService();

        float payment = 2.00;

        if (paymentService.processPayment(myCustomer, payment)) {
            System.out.println("Thanks for the payment!");
        } else {
            System.out.println("Come back later and get my money.");
        }
    }
}

// The code follows SOLID principles by separating responsibilities between Customer, Wallet, and PaymentService.
// Improving clarity and maintainability.
// Restricts direct wallet access to ensure better data protection.
