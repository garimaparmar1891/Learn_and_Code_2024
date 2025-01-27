public class CustomerSearch
{
    public List < Customer > SearchByCountry(string country)
    {
        var searchByCountryQuery = from customer in db.customers
        where customer.Country.Contains(country) 
        orderby customer.CustomerID ascending 
        select customer;
        return searchByCountryQuery.ToList();
    }

    public List < Customer > SearchByCompanyName(string company)
    {
        var searchByCompanyQuery = from customer in db.customers
        where customer.Country.Contains(company)
        orderby customer.CustomerID ascending 
        select customer;
        return searchByCompanyQuery.ToList();
    }

    public List < Customer > SearchByContact(string contact)
    {
        var searchByContactQuery = from customer in db.customers
        where customer.Country.Contains(contact)
        orderby customer.CustomerID ascending
        select customer;
        return searchByContactQuery.ToList();
    }
}

public class CustomerFormatter
{
    public string GenerateCSVRowFromCustomer(Customer customer)
    {
        return $"{customer.CustomerID},{customer.CompanyName},{customer.ContactName},{customer.Country}";
    }
}

public class CustomerDataExporter
{
    public string ExportToCSV(List<Customer> customerData, CustomerFormatter customerFormatter)
    {
        StringBuilder csvStringBuilder = new StringBuilder();
        foreach (var customer in customerData)
        {
            csvStringBuilder.AppendLine(customerFormatter.GenerateCSVRowFromCustomer(customer));
        }
        return csvStringBuilder.ToString();
    }
}
