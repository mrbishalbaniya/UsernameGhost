import requests
import json
import sys
import time
from tqdm import tqdm  # Import tqdm for the progress bar

def load_sites(filename):
    """Load the list of sites from a JSON file."""
    with open(filename, "r") as file:
        return json.load(file)

def search_username(username):
    # Load sites from JSON file
    sites = load_sites("sites.json")

    results = {}
    
    print("Searching usernames...")
    
    # Initialize tqdm for progress bar
    sites_list = list(sites.items())
    with tqdm(total=len(sites_list), desc="Checking sites", ncols=100) as pbar:
        for site, url_template in sites_list:
            url = url_template.format(username=username)
            print(f"Checking {site}...", end="\r")
            try:
                response = requests.get(url)
                if response.status_code == 200:
                    results[site] = url
                else:
                    results[site] = "Not Available"
            except Exception as e:
                results[site] = f"Error: {str(e)}"
            
            # Update progress bar
            pbar.update(1)
            time.sleep(0.1)  # Adjust the delay as needed

    # Separate results into available and not available
    available_urls = {site: url for site, url in results.items() if url != "Not Available" and not url.startswith("Error")}
    not_available_urls = {site: url for site, url in results.items() if url == "Not Available"}
    errors = {site: url for site, url in results.items() if url.startswith("Error")}

    # Save results to JSON file
    with open(f"{username}.json", "w") as outfile:
        json.dump({
            "Available URLs": available_urls,
            "Not Available": not_available_urls,
            "Errors": errors
        }, outfile, indent=4)
    
    # Print results
    if available_urls:
        print("\nAvailable URLs:\n")
        for site, url in available_urls.items():
            print(f"{site}: {url}")
    else:
        print("\nNo URLs available for username '{username}'.")

    if not_available_urls:
        print("\nNot Available URLs:\n")
        for site in not_available_urls.keys():
            print(f"{site}: Not Available")

    if errors:
        print("\nErrors:\n")
        for site, error in errors.items():
            print(f"{site}: {error}")

    print(f"\nSearch complete. Results saved to {username}.json")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 UsernameGhost.py <username>")
        sys.exit(1)
    
    username = sys.argv[1]
    search_username(username)
