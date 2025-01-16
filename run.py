from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import streamlit as st

st.write("Hello and welcome to the food helper!")
new_recipe = st.text_area("Enter new recipe!")
st.write(new_recipe)

# driver = webdriver.Chrome()
# try:
#     driver.get("https://www.fairprice.com.sg/")
#     time.sleep(3)  # Wait for page load
#
#     search_bar = driver.find_element(By.ID, "search-input-bar")
#     search_bar.send_keys("carrots")
#     search_bar.send_keys(Keys.ENTER)
#     time.sleep(5)
#
#     filter_container = driver.find_element(By.XPATH, ".//div[@data-testid='filterList-desktop-price']")
#     filter_container.find_element(By.XPATH, ".//div[@data-testid='filter-item-0']").click()
#
#     time.sleep(10)
#
#     product_containers = driver.find_elements(By.XPATH, "//div[@data-refid]")  # Products have data-refid attribute
#
#     time.sleep(5)
#
#     # Extract product details
#     product_data = []
#     for container in product_containers:
#         # Extract product name
#         try:
#             name = container.find_element(By.XPATH, ".//span[@class='sc-aa673588-1 iCYFVg']").text
#         except:
#             name = "N/A"
#
#         # Extract price
#         try:
#             price = container.find_element(By.XPATH, ".//span[contains(@class, 'sc-65bf849-1')]").text
#         except:
#             price = "N/A"
#
#         # Extract discount or savings
#         try:
#             discount = container.find_element(By.XPATH, ".//span[@data-testid='promo-label']//div").text
#         except:
#             discount = "N/A"
#
#         # Extract rating
#         try:
#             rating = container.find_element(By.XPATH, ".//span[contains(@class, 'sc-6fe931dc-4')]").text
#         except:
#             rating = "N/A"
#
#         # Append extracted data to the list
#         product_data.append({
#             "Name": name,
#             "Price": price,
#             "Discount": discount,
#             "Rating": rating
#         })
#
#     # Convert to a DataFrame
#     df = pd.DataFrame(product_data)
#
#     # Save to Parquet file
#     df.to_parquet("product_data.parquet", index=False)
#
#     print("Scraping completed. Data saved to product_data.parquet.")
#
#
# finally:
#     driver.quit()
