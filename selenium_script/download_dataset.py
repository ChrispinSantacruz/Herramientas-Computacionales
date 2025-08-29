
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

# Set download directory
DOWNLOAD_DIR = os.path.abspath("../datasets")

options = webdriver.ChromeOptions()
options.add_experimental_option('prefs', {
    "download.default_directory": DOWNLOAD_DIR,
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
    "safebrowsing.enabled": True
})

driver = webdriver.Chrome(options=options)
driver.get("https://www.datos.gov.co/")
time.sleep(3)

# Click on the 'DESCUBRE' button
descubre_btn = driver.find_element(By.XPATH, "//div[contains(@class,'dataset-fact-tile') and .//p[contains(text(),'DESCUBRE')]]")
descubre_btn.click()
time.sleep(3)

# Click on the dataset link
dataset_link = driver.find_element(By.XPATH, "//a[contains(@data-testid,'view-card-entry-link') and contains(text(),'Inventario de activos de información de la Subred Sur Occidente 2025')]")
dataset_link.click()
time.sleep(5)

# Switch to new tab if opened
driver.switch_to.window(driver.window_handles[-1])

# Click on the download link for Excel
download_link = driver.find_element(By.XPATH, "//a[contains(@class,'download-file-link') and contains(@href,'inventario_activos_de_informacion_todos_los_procesos_2025.xlsx')]")
download_link.click()
print("Excel download started.")

# Wait for download to complete
time.sleep(10)
driver.quit()
