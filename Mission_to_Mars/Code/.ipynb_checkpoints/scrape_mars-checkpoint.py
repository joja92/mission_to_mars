    #!/usr/bin/env python
    # coding: utf-8

    # In[7]:


from bs4 import BeautifulSoup
import requests
import time

def scrape():
    # In[26]:


    url = "https://mars.nasa.gov/news/"


    # In[11]:


    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    print(soup.prettify())


    # In[13]:


    results = soup.find_all("div", class_="slide")
    print(results)


    # In[18]:


    news_title = results[0].find("div", class_="content_title").text
    news_p = results[0].find("div", class_="rollover_description_inner").text
            
    if (news_title and news_p):
        print(news_title)
        print(news_p)


    # In[80]:


    from splinter import Browser


    # In[81]:


    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)


    # In[82]:


    url2 = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(url2)
    time.sleep(3)


    # In[59]:


    soup2 = BeautifulSoup(browser.html, "html.parser")
    print(soup2.prettify)


    # In[60]:


    browser.click_link_by_partial_text("FULL IMAGE")
    time.sleep(3)


    # In[61]:


    soup2 = BeautifulSoup(browser.html, "html.parser")
    print(soup2.prettify)


    # In[62]:


    results2 = soup2.find_all("img", class_="fancybox-image")
    results2item = results2[0]
    print(results2item)


    # In[63]:

    featuredLink = "https://www.jpl.nasa.gov"+results2item["src"]
    print(featuredLink)


    # In[64]:


    url3 = "https://twitter.com/marswxreport?lang=en"
    response3 = requests.get(url3)
    soup3 = BeautifulSoup(response3.text, "html.parser")
    print(soup3.prettify())


    # In[65]:


    results3 = soup3.find_all("div", class_="js-tweet-text-container")
    print(results3)


    # In[68]:


    mars_weather = results3[0].find("p", class_="TweetTextSize TweetTextSize--normal js-tweet-text tweet-text").text

    print(mars_weather)


    # In[69]:


    import pandas as pd


    # In[70]:


    url4 = "https://space-facts.com/mars/"
    tables = pd.read_html(url4)
    tables


    # In[72]:


    mars_df = tables[1]
    mars_df


    # In[74]:


    mars_html = mars_df.to_html()


    # In[84]:


    url5 = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(url5)


    # In[85]:


    browser.click_link_by_partial_text("Cerberus")


    # In[86]:


    soup5 = BeautifulSoup(browser.html, "html.parser")
    print(soup5.prettify)


    # In[95]:


    results5 = soup5.find_all("img", class_="wide-image")
    print(results5)


    # In[91]:


    for result in results5:
        cerberusLink = "https://astrogeology.usgs.gov"+result["src"]
        print(cerberusLink)


    # In[92]:


    browser.visit(url5)


    # In[93]:


    browser.click_link_by_partial_text("Schiaparelli")


    # In[94]:


    soup6 = BeautifulSoup(browser.html, "html.parser")
    print(soup6.prettify)


    # In[96]:


    results6 = soup6.find_all("img", class_="wide-image")
    print(results6)


    # In[97]:


    for result in results6:
        schiaparelliLink = "https://astrogeology.usgs.gov"+result["src"]
        print(schiaparelliLink)


    # In[98]:


    browser.visit(url5)


    # In[99]:


    browser.click_link_by_partial_text("Syrtis")


    # In[100]:


    soup7 = BeautifulSoup(browser.html, "html.parser")
    print(soup7.prettify)


    # In[101]:


    results7 = soup7.find_all("img", class_="wide-image")
    print(results7)


    # In[102]:


    for result in results7:
        syrtisLink = "https://astrogeology.usgs.gov"+result["src"]
        print(syrtisLink)


    # In[103]:


    browser.visit(url5)


    # In[104]:


    browser.click_link_by_partial_text("Valles")


    # In[105]:


    soup8 = BeautifulSoup(browser.html, "html.parser")
    print(soup8.prettify)


    # In[106]:


    results8 = soup8.find_all("img", class_="wide-image")
    print(results8)


    # In[107]:


    for result in results8:
        vallesLink = "https://astrogeology.usgs.gov"+result["src"]
        print(vallesLink)


    # In[108]:


    hemisphere_image_urls = [{"title": "Cerberus Hemisphere", "img_url": cerberusLink},
    {"title": "Schiaparelli Hemisphere", "img_url": schiaparelliLink},
    {"title": "Syrtis Major Hemisphere", "img_url": syrtisLink},
    {"title": "Valles Marineris Hemisphere", "img_url": vallesLink}
    ]


    # In[ ]:
    marsdict = {
        "news_title": news_title,
        "news_paragraph": news_p,
        "featured_img_link": featuredLink,
        "weather": mars_weather,
        "facts_table": mars_html,
        "hemispheres": hemisphere_image_urls
    }
    
    return marsdict



