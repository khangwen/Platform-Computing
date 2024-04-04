import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# Initialize browser
driver = webdriver.Firefox()

# Navigate to your website 
# driver.get("https://www.prydwen.gg/star-rail/characters")
driver.get("https://www.starbucks.com/")

# Track presence time 
start_time = time.time()
presence_time = start_time

# Find elements
elements = driver.find_elements(by=By.CLASS_NAME, value="emp-name")

# Print elements
# for e in elements:
#     print(e.text)

# Print title
print(driver.title)

# Print number of elements
if len(elements) == 0:
    print("No characters found")
else:
    print(f"Found {len(elements)} characters")
    time.sleep(10)

# Output presence time
current_time = time.time()
presence_time = current_time - start_time
print(f"Presence time: {presence_time} seconds")
        
driver.quit()