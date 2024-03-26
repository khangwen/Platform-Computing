import time
import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
import pymongo

# Set up MongoDB
myclient = pymongo.MongoClient("mongodb+srv://khangwen197:password@cluster0.pqitser.mongodb.net/")
mydb = myclient["CSE4200"]

mycol = mydb["Metrics"]

# Initialize browser
driver = webdriver.Firefox()

# Navigate to your website 
driver.get("http://localhost:3000/")

metrics = []
# Track presence time 
start_time = time.time()
presence_time = start_time

# Initialize number of clicks
num_clicks = 0

# Initialize title
title = driver.title

while True:#presence_time < 50: # seconds
    now = datetime.datetime.now().strftime("%H:%M:%S")

    current_time = time.time()
    presence_time = current_time - start_time
    print(f"Presence time: {presence_time} seconds")
    
    # Track scrolling
    scroll_height = driver.execute_script("return document.body.scrollHeight")  
    current_scroll = driver.execute_script("return window.pageYOffset")
    print(f"Scrolled {current_scroll}/{scroll_height} pixels")
    
    # Insert data into MongoDB
    new_entry = {"TIMESTAMP (HH/MM/SS)": now, "PRESENCE_TIME (SEC.)": presence_time, "SCROLLING (PIXELS)": current_scroll}
    mycol.insert_one(new_entry)

    time.sleep(2) 
        
driver.quit()