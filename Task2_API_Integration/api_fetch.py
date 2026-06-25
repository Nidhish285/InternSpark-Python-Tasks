import requests

def main():

    cities = ["London", "New York", "Tokyo", "Paris", "Berlin", "Sydney", "Mumbai", "Cairo"]
    data_list = []
    
    print("=== InternSpark Task 2: API Data Fetching Using Requests ===")
    print("[LOG] Initiating concurrent connections to weather endpoints...")
    
    try:
        for city in cities:
            url = f"https://wttr.in/{city}?format=j1"
            response = requests.get(url, timeout=10)
            response.raise_for_status() 
            
            weather_json = response.json()
            current = weather_json['current_condition'][0]
            

            data_list.append({
                "city": city,
                "temp": int(current['temp_C']),
                "condition": current['weatherDesc'][0]['value'],
                "humidity": current['humidity']
            })
        print("[LOG] Weather records successfully fetched and processed.\n")
        

        print("GLOBAL WEATHER SUMMARY")
        print("=================================================================")
        print(f"{'City Location':<15} | {'Temperature':<12} | {'Condition':<20} | {'Humidity':<10}")
        print("-----------------------------------------------------------------")
        for record in data_list:
            print(f"{record['city']:<15} | {record['temp']:>3}C       | {record['condition']:<20} | {record['humidity']}%")
        print("=================================================================")
        

        print("\n--- Search Location Functionality ---")
        search_name = input("Enter city name to search: ").strip()
        if search_name:
            found = False
            for record in data_list:
                if search_name.lower() in record["city"].lower():
                    print("\nLocation Record Found!")
                    print(f"City:      {record['city']}")
                    print(f"Temp:      {record['temp']}C")
                    print(f"Outlook:   {record['condition']}")
                    print(f"Humidity:  {record['humidity']}%")
                    found = True
            if not found:
                print(f"No weather records match the location: '{search_name}'")
        else:
            print("[SKIP] Blank input provided. Skipping search.")


        print("\n--- Filter Locations by Heat Threshold ---")
        try:
            min_temp = float(input("Enter minimum temperature filter (C): "))
            print(f"\nResults for locations currently at or above {min_temp}C:")
            print("-----------------------------------------------------------------")
            found_filter = False
            for record in data_list:
                if record['temp'] >= min_temp:
                    print(f"Match: {record['city']} is experiencing hot weather at {record['temp']}C ({record['condition']})")
                    found_filter = True
            if not found_filter:
                print(f"No tracked locations are currently at or above {min_temp}C")
            print("-----------------------------------------------------------------")
        except ValueError:
            print("[ERROR] Invalid numeric input. Skipping filter.")

    except requests.exceptions.RequestException as e:
        print(f"[ERROR] Network operation failed: {e}")
    except Exception as e:
        print(f"[ERROR] An unexpected data parsing error occurred: {e}")
    finally:
        print("\nAPI data process sequence finalized.")

if __name__ == "__main__":
    main()
