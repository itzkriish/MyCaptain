# web scraping done for educational purposes
import requests
from bs4 import BeautifulSoup
import argparse
import sqlite3

def connect(dbname):
    conn = sqlite3.connect(dbname)
    conn.execute("CREATE TABLE IF NOT EXISTS OYO_HOTELS (NAME TEXT, ADDRESS TEXT, PRICE INT, AMENITIES TEXT, RATING TEXT)")
    conn.close()

def insert_data(dbname, data):
    conn = sqlite3.connect(dbname)
    insert_to_db = "INSERT INTO OYO_HOTELS (NAME, ADDRESS, PRICE, AMENITIES, RATING) VALUES (?, ?, ?, ?, ?)"
    conn.execute(insert_to_db, data)
    conn.commit()
    conn.close()

def hotel_info(dbname):
    conn = sqlite3.connect(dbname)
    cur = conn.cursor()
    cur.execute("SELECT * FROM OYO_HOTELS")

    data = cur.fetchall()
    for record in data:
        print(record)

    conn.close()

parser = argparse.ArgumentParser()
parser.add_argument("--page_max", help="Enter the number of pages to parse", type=int)
parser.add_argument("--dbname", help="Enter the name of the database", type=str)
args = parser.parse_args()

headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1.1 Safari/605.1.15"}
url = "https://www.oyorooms.com/hotels-in-delhi/?page="
page_max = args.page_max

connect(args.dbname)
scraped_info = []
for page in range(page_max):
    req = requests.get(url + str(page), headers=headers)
    data = req.content
    soup = BeautifulSoup(data, "html.parser")

    hotels = soup.find_all("div", {"class": "hotelCardListing"})
    for hotel in hotels:
        hotel_dict = {}
        hotel_dict["name"] = hotel.find("h3", {"class": "listingHotelDescription__hotelName"}).text
        hotel_dict["address"] = hotel.find("span", {"itemprop": "streetAddress"}).text
        hotel_dict["price"] = hotel.find("span", {"class": "listingPrice__finalPrice"}).text

        # if there are no available ratings for the hotel
        try:
            hotel_dict["rating"] = hotel.find("span", {"class": "hotelRating__ratingSummary"}).text
        except AttributeError:
            hotel_dict["rating"] = None

        parent_ameneties_element = hotel.find("div", {"class": "amenityWrapper"})

        amenities = []
        for amenity in parent_ameneties_element.find_all("div", {"class": "amenityWrapper__amenity"}):
            amenities.append(amenity.find("span", {"class": "d-body-sm"}).text.strip())
        hotel_dict["amenities"] = ', '.join(amenities[:-1])

        scraped_info.append(hotel_dict)
        insert_data(args.dbname, tuple(hotel_dict.values()))

hotel_info(args.dbname)
