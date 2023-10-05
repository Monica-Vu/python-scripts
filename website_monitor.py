import time
import hashlib
from urllib.request import urlopen, Request

SECONDS_IN_A_MINUTE = 60
SECONDS_IN_A_DAY = 86400

urls = ['https://www.clio.com/about/careers/search/?teams=engineering&locations=vancouver',
        'https://edel.fa.us2.oraclecloud.com/hcmUI/CandidateExperience/en/sites/CX/requisitions?location=Vancouver%2C+BC%2C+Canada&locationId=100000000379548&locationLevel=city&mode=location&radius=25&radiusUnit=MI'
        
        ]
hashes = {}

def get_page_hash(url):
    try:
        req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        response = urlopen(req).read()
        page_hash = hashlib.sha224(response).hexdigest()
        return page_hash
    
    except Exception as e:
        print(f"Error fetching {url}: {e}")
        return None 
    
def main():
    for url in urls:
        initial_hash = get_page_hash(url)
        
        if initial_hash: 
            hashes[url] = initial_hash

    print("Monitoring websites for changes: ")

    while True: 
        for url in urls: 
            new_hash = get_page_hash(url)

            if new_hash:
                if new_hash != hashes[url]: 
                    print(f"Change detected in {url}!")
                    hashes[url] = new_hash
                    print("hashes =>", hashes, "\n")
        
        time.sleep(SECONDS_IN_A_DAY)

if __name__ == "__main__":
    main()