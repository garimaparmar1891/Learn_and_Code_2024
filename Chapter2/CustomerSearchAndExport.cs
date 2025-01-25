public class CustomerSearch
{
    public List < Customer > SearchByCountry(string country)
    {
        var searchByCountryQuery = from customer in db.customers
        where customer.Country.Contains(country) 
        orderby c.CustomerID ascending 
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

public class CustomerDataExporter
{
    public string ExportToCSV(List<Customer> data)
    {
        StringBuilder csvStringBuilder = new StringBuilder();
        foreach (var item in data)
        {
            csvStringBuilder.AppendFormat("{0},{1}, {2}, {3}", item.CustomerID, item.CompanyName, item.ContactName, item.Country);
            csvStringBuilder.AppendLine();
        }
        return sb.ToString();
    }
}
