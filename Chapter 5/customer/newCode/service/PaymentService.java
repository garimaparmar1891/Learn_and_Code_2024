import customer.newCode.model.Customer;

public class PaymentService {

    public boolean processPayment(Customer customer, float amount) {
        return customer.makePayment(amount);
    }
}
