import requests 
import time

# Change this
mainDomain = "domain.com" 
delay = 0.15

with open("sub.txt", 'r', encoding='utf-16-le') as f:
    words = [word.strip() for word in f]
    output = []
    for word in words:
        url = f"https://{word}.{mainDomain}"
        try:
            r = requests.get(url)
            print(f"{url} - not fail")
        except requests.exceptions.SSLError:
            print(f"{url}") # Means site exists and requests for TLS Cert
            output.append(url)
        except requests.exceptions.ConnectionError:
            # print(f"{url} - conn err")
            pass
        except Exception as e:
            print(e)

        time.sleep(delay)
    
    with open('res.txt', 'w') as file:
        for word in output:
            file.write(word + "\n")
        
    print("All done! :D")
