import requests
from bs4 import BeautifulSoup

HEADERS = {"User-Agent": "Mozilla/5.0"}

def scrape_headlines(url):
    response = requests.get(url, headers=HEADERS)
    soup = BeautifulSoup(response.text, "html.parser")

    headlines = set()

    for tag in soup.find_all(["h2", "h3"]):
        a = tag.find("a")
        if a:
            title = a.get_text(strip=True)
            if title and len(title) > 30:
                headlines.add(title.upper())  # CAPITAL LETTERS

    if not headlines:
        print("\n⚠️ NO HEADLINES FOUND.")
        return

    print("\n📰 HEADLINES:\n")
    for i, h in enumerate(headlines, start=1):
        print(f"{i}. {h}")

    print("\n🔗 EXPLORE MORE:")
    print(url)


# ---------------- MAIN MENU ---------------- #

print("\nCHOOSE NEWS WEBSITE:")
print("1. INDIA TODAY")
print("2. THE HINDU")

site_choice = input("\nENTER CHOICE (1/2): ").strip()

# -------- INDIA TODAY -------- #
if site_choice == "1":
    print("\nCHOOSE INDIA TODAY SECTION:")
    print("i. IPO")
    print("ii. MARKET")

    section = input("\nENTER CHOICE (i/ii): ").strip().lower()

    if section == "i":
        scrape_headlines("https://www.indiatoday.in/business/ipo")
    elif section == "ii":
        scrape_headlines("https://www.indiatoday.in/business/market")
    else:
        print("❌ INVALID INDIA TODAY OPTION")

# -------- THE HINDU -------- #
elif site_choice == "2":
    print("\nCHOOSE THE HINDU SECTION:")
    print("i. BUSINESS")
    print("ii. MARKETS")
    print("iii. ECONOMY")

    section = input("\nENTER CHOICE (i/ii/iii): ").strip().lower()

    if section == "i":
        scrape_headlines("https://www.thehindu.com/business/")
    elif section == "ii":
        scrape_headlines("https://www.thehindu.com/business/markets/")
    elif section == "iii":
        scrape_headlines("https://www.thehindu.com/business/Economy/")
    else:
        print("❌ INVALID THE HINDU OPTION")

else:
    print("❌ INVALID WEBSITE CHOICE")
