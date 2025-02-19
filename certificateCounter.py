import requests

def get_certificate_count(domain):
    
    non_expired_url = f"https://crt.sh/?q={domain}&output=json"
    
    
    expired_url = f"https://crt.sh/?q={domain}&exclude=expired&group=none&output=json"
    
    try:
        
        non_expired_response = requests.get(non_expired_url)
        if non_expired_response.status_code == 200:
            non_expired_certs = non_expired_response.json()
            non_expired_count = len(non_expired_certs)
            print(f"Non-expired certificates for {domain}: {non_expired_count}")
        else:
            print(f"Error: {non_expired_response.status_code} - Unable to retrieve non-expired certificates for {domain}")
        
        
        expired_response = requests.get(expired_url)
        if expired_response.status_code == 200:
            expired_certs = expired_response.json()
            expired_count = len(expired_certs)
            print(f"Expired certificates for {domain}: {expired_count}")
        else:
            print(f"Error: {expired_response.status_code} - Unable to retrieve expired certificates for {domain}")
    
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")


domain = "crt.sh"  
get_certificate_count(domain)