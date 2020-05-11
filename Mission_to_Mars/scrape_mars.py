#!/usr/bin/env python
# coding: utf-8

#define scrape function to be used by app
def scrape():

    # In[24]:


    #import BeautifulSoup (BS), time, and requests dependencies
    from bs4 import BeautifulSoup
    import requests
    import time


    # In[2]:


    #website for latest news article
    url = "https://mars.nasa.gov/news/"


    # In[3]:


    #create response object from URL and pass to BS to scrape
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    #display HTML from scrape in readable format
    print(soup.prettify())


    # In[4]:


    #filter for only "slide" class tags in a list
    results = soup.find_all("div", class_="slide")
    print(results)


    # In[5]:


    #assign first result in list to variables
    news_title = results[0].find("div", class_="content_title").text
    news_p = results[0].find("div", class_="rollover_description_inner").text
            
    if (news_title and news_p):
        print(news_title)
        print(news_p)


    # In[6]:


    #import splinter
    from splinter import Browser


    # In[7]:


    #start chromedriver executable
    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)


    # In[8]:


    #navigate to next URL
    url2 = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(url2)


    # In[9]:


    #scrape current page with BS
    #display HTML from scrape in readable format
    soup2 = BeautifulSoup(browser.html, "html.parser")
    print(soup2.prettify)


    # In[10]:


    #click desired link for featured image
    browser.click_link_by_partial_text("FULL IMAGE")
    #allow at least 2 seconds for page to load
    time.sleep(2)


    # In[11]:


    ##scrape current page with BS
    #display HTML from scrape in readable format
    soup2 = BeautifulSoup(browser.html, "html.parser")
    print(soup2.prettify)


    # In[12]:


    #search for image tags and separate first one
    results2 = soup2.find_all("img", class_="fancybox-image")
    results2item = results2[0]
    print(results2item)


    # In[13]:


    #build link to image from scraped results
    featuredLink = "https://www.jpl.nasa.gov"+results2item["src"]
    print(featuredLink)


    # In[14]:


    #scrape twitter page with BS
    #display HTML from scrape in readable format
    url3 = "https://twitter.com/marswxreport?lang=en"
    response3 = requests.get(url3)
    soup3 = BeautifulSoup(response3.text, "html.parser")
    print(soup3.prettify())


    # In[15]:


    #filter out tweets
    results3 = soup3.find_all("div", class_="js-tweet-text-container")
    print(results3)


    # In[16]:


    #assign first tweet's text to variable
    mars_weather = results3[0].find("p", class_="TweetTextSize TweetTextSize--normal js-tweet-text tweet-text").text

    print(mars_weather)


    # In[17]:


    #import pandas
    import pandas as pd


    # In[18]:


    #turn tables from next URL into list of dataframes
    url4 = "https://space-facts.com/mars/"
    tables = pd.read_html(url4)
    tables


    # In[19]:


    #separate desired dataframe
    mars_df = tables[1]
    mars_df


    # In[20]:


    #transform dataframe to html format
    mars_html = mars_df.to_html()
    print(mars_html)


    # In[21]:


    #navigate to next URL for hemisphere images
    url5 = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(url5)


    # In[22]:


    #click on first hemisphere
    browser.click_link_by_partial_text("Cerberus")


    # In[23]:


    ##scrape current page with BS
    #display HTML from scrape in readable format
    soup5 = BeautifulSoup(browser.html, "html.parser")
    print(soup5.prettify)


    # In[95]:


    #find image tag
    results5 = soup5.find_all("img", class_="wide-image")
    print(results5)


    # In[91]:


    #build link to image from scrape
    for result in results5:
        cerberusLink = "astrogeology.usgs.gov"+result["src"]
        print(cerberusLink)


    # In[151]:


    #navigate back to hemisphere images
    browser.visit(url5)


    # In[152]:


    #click on next hemisphere
    browser.click_link_by_partial_text("Schiaparelli")


    # In[153]:


    ##scrape current page with BS
    #display HTML from scrape in readable format
    soup6 = BeautifulSoup(browser.html, "html.parser")
    print(soup6.prettify)


    # In[154]:


    #find image tag
    results6 = soup6.find_all("img", class_="wide-image")
    print(results6)


    # In[155]:


    #build link to image from scrape
    for result in results6:
        schiaparelliLink = "astrogeology.usgs.gov"+result["src"]
        print(schiaparelliLink)


    # In[98]:


    #navigate back to hemisphere images
    browser.visit(url5)


    # In[99]:


    #click on next hemisphere
    browser.click_link_by_partial_text("Syrtis")


    # In[100]:


    ##scrape current page with BS
    #display HTML from scrape in readable format
    soup7 = BeautifulSoup(browser.html, "html.parser")
    print(soup7.prettify)


    # In[101]:


    #find image tag
    results7 = soup7.find_all("img", class_="wide-image")
    print(results7)


    # In[102]:


    #build link to image from scrape
    for result in results7:
        syrtisLink = "astrogeology.usgs.gov"+result["src"]
        print(syrtisLink)


    # In[103]:


    #navigate back to hemisphere images
    browser.visit(url5)


    # In[104]:


    #click on next hemisphere
    browser.click_link_by_partial_text("Valles")


    # In[105]:


    ##scrape current page with BS
    #display HTML from scrape in readable format
    soup8 = BeautifulSoup(browser.html, "html.parser")
    print(soup8.prettify)


    # In[106]:


    #find image tag
    results8 = soup8.find_all("img", class_="wide-image")
    print(results8)


    # In[107]:


    #build link to image from scrape
    for result in results8:
        vallesLink = "astrogeology.usgs.gov"+result["src"]
        print(vallesLink)


    # In[108]:


    #create dictionary with hemisphere titles and respective links
    hemisphere_image_urls = [{"title": "Cerberus Hemisphere", "img_url": cerberusLink},
                            {"title": "Schiaparelli Hemisphere", "img_url": schiaparelliLink},
                            {"title": "Syrtis Major Hemisphere", "img_url": syrtisLink},
                            {"title": "Valles Marineris Hemisphere", "img_url": vallesLink}
                        ]


    # In[ ]:


    #create dictionary with news title and paragraph, link to featured image, weather from twitter, table of Mars facts in HTML, and hemisphere dictionary
    marsdict = {
            "news_title": news_title,
            "news_paragraph": news_p,
            "featured_img_link": featuredLink,
            "weather": mars_weather,
            "facts_table": mars_html,
            "hemispheres": hemisphere_image_urls
        }

    #return dictionary to Flask app
    return marsdict