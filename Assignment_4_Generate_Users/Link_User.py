import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# Initialize browser
driver = webdriver.Firefox()

# Navigate to your website 
# driver.get("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRMz_aCPaCfCUAlzB6HlBZEmb3GzNzgDRfKJzIaBn52Sg&s")
driver.get("https://github.com/khangwen")

# Track presence time 
start_time = time.time()
presence_time = start_time

# Print title
print(driver.title)

# Counter to stop recursion
counter = 0

def get_Elements():
    # Global variables
    global counter

    # Find links
    links = driver.find_elements(by=By.TAG_NAME, value="a")
    link_name = ""

    # Click on link
    for link in links:
        link_name = link.get_attribute("href")
        print(link_name)
        if "#" not in link_name and counter <= 1:
            print("Found clickable link. Redirecting...")
            counter += 1
            link.click()
            time.sleep(10)

            # Find image
            images = driver.find_elements(by=By.TAG_NAME, value="img")

            # Print number of elements
            if len(images) == 0:
                print("No images found")
            else:
                print(f"Found {len(images)} images")
                time.sleep(10 * len(images))

            # Find keywords
            keywords = driver.find_elements(by=By.ID, value="food")

            if len(keywords) == 0:
                print("No food id found")
            else:
                print(f"Found food id")
                time.sleep(10)
            break
    
    # Recursion if link exists
    if len(links) > 0 and counter <= 1:
        get_Elements()
    else:
        print("No links found or recursion limit reached. Exiting...")

# Get elements
get_Elements()

# Output presence time
current_time = time.time()
presence_time = current_time - start_time
print(f"Presence time: {presence_time} seconds")
        
driver.quit()