import pandas as pd

# Step 1: Load dataset
def load_dataset(filepath):
    try:
        df = pd.read_csv(filepath, encoding='utf-8')
        print("✅ Dataset loaded successfully using UTF-8 encoding.\n")
    except UnicodeDecodeError:
        df = pd.read_csv(filepath, encoding='latin-1')
        print("⚠️ UTF-8 failed, loaded using Latin-1 encoding.\n")
    return df


# Step 2: Country + Currency Mapping
country_currency_map = {
    1: ("India", "Indian Rupees (₹)"),
    14: ("Australia", "Australian Dollar (A$)"),
    30: ("Brazil", "Brazilian Real (R$)"),
    37: ("Canada", "Canadian Dollar (C$)"),
    94: ("Indonesia", "Indonesian Rupiah (IDR)"),
    148: ("New Zealand", "New Zealand Dollar (NZ$)"),
    162: ("Philippines", "Philippine Peso (₱)"),
    166: ("Qatar", "Qatari Riyal (QAR)"),
    184: ("Singapore", "Singapore Dollar (SGD)"),
    189: ("South Africa", "South African Rand (R)"),
    191: ("Sri Lanka", "Sri Lankan Rupee (LKR)"),
    208: ("Turkey", "Turkish Lira (₺)"),
    214: ("UAE", "Emirati Dirham (AED)"),
    215: ("UK", "British Pound (£)"),
    216: ("USA", "US Dollar ($)")
}


# Step 3: Display Intro
def show_intro():
    print("************************************************************")
    print("** WELCOME TO THE RESTAURANT RECOMMENDATION SYSTEM **")
    print("************************************************************\n")


# Step 4: Show Countries
def show_countries():
    print("1. Country - Please choose a country from the options below:\n")
    for code, (name, currency) in country_currency_map.items():
        print(f"{code}. {name} (Currency: {currency})")


# Step 5: Show Cities
def show_cities(df, selected_country):
    if selected_country not in df['Country Code'].unique():
        print("\n⚠️ Invalid country code or no data available for this country.")
        return None
    cities = sorted(df[df['Country Code'] == selected_country]['City'].dropna().unique())
    if not cities:
        print("\n⚠️ No cities available for this country in the dataset.")
        return None
    print(f"\n2. City - Choose from {len(cities)} available cities:\n")
    for i, city in enumerate(cities, 1):
        print(f"{i}. {city}")
    try:
        choice = int(input("\nEnter city number: "))
        if 1 <= choice <= len(cities):
            selected_city = cities[choice - 1]
            print(f"\nYou selected city: {selected_city}")
            return selected_city
    except ValueError:
        pass
    print("\n⚠️ Invalid input.")
    return None


# Step 6: Show Localities
def show_localities(df, selected_city):
    localities = sorted(df[df['City'] == selected_city]['Locality'].dropna().unique())
    if not localities:
        print("\n⚠️ No localities found.")
        return None
    print(f"\n3. Locality - Choose from {len(localities)} available localities:\n")
    for i, loc in enumerate(localities, 1):
        print(f"{i}. {loc}")
    try:
        choice = int(input("\nEnter locality number: "))
        if 1 <= choice <= len(localities):
            selected_locality = localities[choice - 1]
            print(f"\nYou selected locality: {selected_locality}")
            return selected_locality
    except ValueError:
        pass
    print("\n⚠️ Invalid input.")
    return None


# Step 7: Show Addresses
def show_addresses(df, selected_city, selected_locality):
    addresses = df[(df['City'] == selected_city) & (df['Locality'] == selected_locality)]['Address'].dropna().unique()
    if len(addresses) == 0:
        print("\n⚠️ No addresses found.")
        return None
    print(f"\n4. Addresses in {selected_locality} ({len(addresses)} total):\n")
    for i, addr in enumerate(addresses, 1):
        print(f"{i}. {addr}")
    try:
        choice = int(input("\nEnter address number: "))
        if 1 <= choice <= len(addresses):
            selected_address = addresses[choice - 1]
            print(f"\nYou selected address: {selected_address}")
            return selected_address
    except ValueError:
        pass
    print("\n⚠️ Invalid input.")
    return None


# Step 8: Show Restaurants and Recommend
def recommend_restaurants(df, selected_address):
    restaurants = df[df['Address'] == selected_address]
    if restaurants.empty:
        print("\n⚠️ No restaurants found at this address.")
        return None

    print("\n🍽️ Here are the restaurant recommendations for you based on your preferences:\n")
    for i, row in restaurants.iterrows():
        name = row['Restaurant Name'] if pd.notna(row['Restaurant Name']) else "Unnamed"
        cuisines = row['Cuisines'] if pd.notna(row['Cuisines']) else "Not available"
        print(f"➡️ {name}")
        print(f"   🍴 Cuisines: {cuisines}")
        print()
    return restaurants


# Step 9: Show Features + Price Range + Votes
def show_features(df, selected_address):
    selected_rows = df[df['Address'] == selected_address]

    print("--------------------------------------------------------------")
    print("📋 Restaurant Feature Summary:")
    print("--------------------------------------------------------------")

    features = {
        "Has Table booking": "🪑 Table Booking Availability",
        "Has Online delivery": "📦 Online Delivery Available",
        "Is delivering now": "🚚 Currently Delivering",
        "Switch to order menu": "🍴 Switch to Order Menu Available"
    }

    for col, label in features.items():
        if col in selected_rows.columns:
            unique_vals = selected_rows[col].dropna().unique()
            readable = ["Yes" if val == 1 else "No" for val in unique_vals]
            print(f"{label}: {', '.join(readable)}")
        else:
            print(f"{label}: Information not available.")

    if 'Price range' in selected_rows.columns:
        price_ranges = selected_rows['Price range'].dropna().unique()
        if len(price_ranges) > 0:
            print(f"\n💵 Price Range: {', '.join(map(str, price_ranges))}")

    if 'Votes' in selected_rows.columns:
        votes = selected_rows['Votes'].dropna().unique()
        if len(votes) > 0:
            print(f"⭐ Votes: {', '.join(map(str, votes[:10]))}")  # Show up to 10 votes


# Step 10: Main
def main():
    filepath = r"C:\Users\Sree Kirthana\Documents\random\Dataset_binary_fixed.csv"
    df = load_dataset(filepath)
    show_intro()
    show_countries()

    try:
        selected_country = int(input("\nEnter Country Code: "))
        if selected_country in country_currency_map:
            selected_city = show_cities(df, selected_country)
            if selected_city:
                selected_locality = show_localities(df, selected_city)
                if selected_locality:
                    selected_address = show_addresses(df, selected_city, selected_locality)
                    if selected_address:
                        recommend_restaurants(df, selected_address)
                        show_features(df, selected_address)
    except ValueError:
        print("\n⚠️ Invalid input.")


if __name__ == "__main__":
    main()


