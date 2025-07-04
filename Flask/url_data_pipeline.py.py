import json
import requests
import socket
import pandas as pd

json_file = "D:/Flask/response.json"

try:
    with open(json_file, 'r', encoding='utf-8') as f:
        json_content = f.read()
except FileNotFoundError:
    raise Exception("File does not exist.")

data = json.loads(json_content)

all_infringing_urls = []
all_infringing_ips = []

def get_ip_address(url):
    try:
        hostname = requests.utils.urlparse(url).hostname
        # print(hostname)
        ip_address = socket.gethostbyname(hostname)
        return ip_address
    except Exception as e:
        return None

for notice in data.get('notices', []):
    for work in notice.get('works', []):
        urls = [url_obj['url'] for url_obj in work.get('infringing_urls', [])]
        
        for url in urls:
            ip = get_ip_address(url)
            if ip:  
                all_infringing_urls.append(url)
                all_infringing_ips.append(ip)

df = pd.DataFrame({
    'URL': all_infringing_urls[:10],
    'IP_Address': all_infringing_ips[:10]
})
print(df)

if len(all_infringing_urls) == len(all_infringing_ips):
    df = pd.DataFrame({
        'URL': all_infringing_urls,
        'IP_Address': all_infringing_ips
    })
    # Writing data frame to a CSV file
    df.to_csv("python_output.csv", index=False)
    print("CSV file 'python_output.csv' has been created successfully.")
else:
    print("Mismatch in lengths of URLs and IPs. Check the IP resolution process.")
