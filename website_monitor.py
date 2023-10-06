import time
import hashlib
from urllib.request import urlopen, Request

SECONDS_IN_A_MINUTE = 60
SECONDS_IN_A_DAY = 86400

# TODO: see if there's a cleaner way to get a list of arrays. Maybe you can put these links in a text file (seperated) and the program can read the text?
urls = ['https://www.clio.com/about/careers/search/?teams=engineering&locations=vancouver',
        'https://edel.fa.us2.oraclecloud.com/hcmUI/CandidateExperience/en/sites/CX/requisitions?location=Vancouver%2C+BC%2C+Canada&locationId=100000000379548&locationLevel=city&mode=location&radius=25&radiusUnit=MI',
        'https://careers.translink.bc.ca/psc/EXT/EMPLOYEE/HRMS/c/HRS_HRAM_FL.HRS_CG_SEARCH_FL.GBL?Page=HRS_APP_JBPST_FL&Action=U&FOCUS=Applicant&SiteId=2&JobOpeningId=20230763&PostingSeq=1&'
        'https://talent.canada.ca/en/browse/pools',
        'https://bcpublicservice.hua.hrsmart.com/hr/ats/JobSearch/search',
        'https://emploisfp-psjobs.cfp-psc.gc.ca/psrs-srfp/applicant/page2440?search=Search%20jobs&locationsFilter=&officialLanguage=&title=Software%20Developer&referenceNumber=&tab=1&nonProgram=1&selectionProcessNumber=&departments=&log=false'
        'https://emploisfp-psjobs.cfp-psc.gc.ca/psrs-srfp/applicant/page2440?search=Search%20jobs&locationsFilter=&officialLanguage=&title=Software&referenceNumber=&tab=1&nonProgram=1&selectionProcessNumber=&departments=&log=false'
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
            
            if new_hash != hashes[url]: 
                print(f"Change detected in {url}!")
                hashes[url] = new_hash
                print("hashes =>", hashes, "\n")
        
        time.sleep(SECONDS_IN_A_DAY)

if __name__ == "__main__":
    main()