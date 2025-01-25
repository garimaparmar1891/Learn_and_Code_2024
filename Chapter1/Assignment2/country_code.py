country_names = {
    "IN": "India",
    "US": "United States",
    "NZ": "New Zealand",
    "UK": "United Kingdom",
    "CA": "Canada",
    "AU": "Australia",
    "FR": "France",
    "DE": "Germany",
    "JP": "Japan",
    "CN": "China",
    "BR": "Brazil",
    "ZA": "South Africa",
    "IT": "Italy",
    "RU": "Russia",
    "MX": "Mexico"
}

def get_country_name(country_code):
    country_code = country_code.upper()  
    return country_names.get(country_code, "Invalid country code. Please try again.")

def main():
    print("Welcome to the Country Name Finder!")
    while True:
        country_code = input("Enter a country code (e.g., IN, US, NZ) or type 'exit' to quit: ")
       
        if country_code.lower() == "exit":
            print("Exiting the application!")
            break
        
        country_name = get_country_name(country_code)
        print(f"Country: {country_name}\n")

if __name__ == "__main__":
    main()