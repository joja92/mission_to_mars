from flask import Flask, render_template, redirect
import pymongo
import requests
import scrape_mars


conn = "mongodb://localhost:27017"
client = pymongo.MongoClient(conn)

db = client.mars_db
mars_collection = db.mars_db

app = Flask(__name__)

@app.route("/")
def home():
    mars_dictionary = db.mars_collection.find_one()
    return render_template("index.html", dict=mars_dictionary)

@app.route("/scrape")
def scraper():
    scraped_data = scrape_mars.scrape()
    db.mars_collection.update({}, scraped_data, upsert=True)
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
    