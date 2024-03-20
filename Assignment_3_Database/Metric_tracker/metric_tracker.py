import time
from selenium import webdriver
from selenium.webdriver.common.by import By

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
    # Print title
    # print(f"Title: {title}")

    current_time = time.time()
    presence_time = current_time - start_time
    print(f"Presence time: {presence_time} seconds")
    
    # Track scrolling
    scroll_height = driver.execute_script("return document.body.scrollHeight")  
    current_scroll = driver.execute_script("return window.pageYOffset")
    print(f"Scrolled {current_scroll}/{scroll_height} pixels")
    
    time.sleep(2) 

    # Track clicks   
    buttons = driver.find_elements(By.TAG_NAME, "button")

    for button in buttons:
        # button.click()
        if button.get_attribute('textContent') == "Clicked!":
            num_clicks += 1
        
    print(f"Number of clicks: {num_clicks}\n")
        
driver.quit()