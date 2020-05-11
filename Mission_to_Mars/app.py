#import dependencies
from flask import Flask, render_template, redirect
import pymongo
import requests
import scrape_mars

#create connection variable
conn = "mongodb://localhost:27017"
#pass variable to pymongo instance
client = pymongo.MongoClient(conn)

#create and connect to database
db = client.mars_db
#create collection in database
mars_collection = db.mars_db

#create Flask app instance
app = Flask(__name__)

@app.route("/")
def home():
    #retrieve dictionary of mars data from database
    mars_dictionary = db.mars_collection.find_one()
    #display database information in webpage using html template
    return render_template("index.html", dict=mars_dictionary)

#run scraper code
@app.route("/scrape")
def scraper():
    #assign returned data from scraper to variable
    scraped_data = scrape_mars.scrape()
    #store scraped data into database
    db.mars_collection.update({}, scraped_data, upsert=True)
    #navigate back to home
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
    