import os
import time
import urllib.request
from selenium import webdriver
from selenium.webdriver.common.by import By

# Initialize browser
driver = webdriver.Firefox()

# Install extensions
ublock_PATH = "C:\\Users\\lenovo\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\8w1j97j1.default-release\\extensions\\uBlock0@raymondhill.net.xpi"
driver.install_addon(ublock_PATH, temporary=True)

# Navigate to your website
website_URL = "https://www.prydwen.gg/star-rail/characters" 
driver.get(website_URL)

# Track presence time 
start_time = time.time()
presence_time = start_time

# Print title
print(driver.title)

def get_Elements():

    # Find rarity class
    rarity_class_5 = driver.find_elements(By.XPATH, "//*[contains(@class, 'rarity-5 true')]")

    # Print number of rarity 5 elements
    if len(rarity_class_5) == 0:
        print("No rarity-5 elements found")
    else:
        print(f"Found {len(rarity_class_5)} rarity-5 elements...")
        time.sleep(2)

    # Find link
    link = driver.find_element(By.XPATH,"//a[@href='/star-rail/characters/acheron']")
    link_name = ""

    # Click on link
    link_name = link.get_attribute("href")
    print(link_name)

    print("Found link. Redirecting...")
    driver.execute_script("arguments[0].click();", link)
    time.sleep(2)

    # Show all tabs
    driver.execute_script("document.getElementsByClassName('tab-inside')[2].style.display='block';")
    print("Showing third tab...")
    time.sleep(2)

    # Find images
    images = driver.find_elements(by=By.TAG_NAME, value="img")

    # Print number of images  
    if len(images) == 0:
        print("No images found")
    else:
        print(f"Found {len(images)} images...")
        time.sleep(2)

        # Download all images
        print("Downloading images...")
        image_PATH = 'scraped_images/'
        if not os.path.exists(image_PATH):
            os.makedirs(image_PATH)

        counter = 0
        for image in images:
            counter += 1
            new_url = image_PATH + "test" + str(counter) + ".png"
            src = image.get_attribute("src")
            urllib.request.urlretrieve(src, new_url)

    # Find keywords
    keywords = driver.find_elements(By.XPATH, "//*[contains(@class, 'build-stats')]")

    if len(keywords) == 0:
        print("No keyword found")
    else:
        print(f"Found {len(keywords)} keywords...")
        time.sleep(2)

        # Find keyword info
        for keyword in keywords:
            best_stat = keyword.find_element(By.XPATH, ".//*[contains(@class, 'Lightning')]")
            print(best_stat.text)
            if best_stat.text == "BEST STATS":
                print("Found element with best stats...")
                time.sleep(2)
                break
            else:
                print("Not working as intended")
    
# Get elements
get_Elements()

# Output presence time
current_time = time.time()
presence_time = current_time - start_time
print(f"Presence time: {presence_time} seconds")
        
driver.quit()