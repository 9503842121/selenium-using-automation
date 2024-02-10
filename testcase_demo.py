
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#from selenium.webdriver.support.select import Select
import chromedriver_autoinstaller

# Automatically install chromedriver
chromedriver_autoinstaller.install()

@pytest.fixture
def browser():
    # Initialize Chrome WebDriver
    driver = webdriver.Chrome()


    yield driver
    # Teardown - close the browser window
    driver.quit()

def test_page_title(browser):
    # Open website
    browser.get("https://www.entrata.com/")
    browser.maximize_window()

    # Check if the title contains "Entrata"
    assert "Entrata" in browser.title

def test_watch_demo_button(browser):
    # Open website
    browser.get("https://www.entrata.com/")
    browser.maximize_window()

    # Click on "Watch Demo" button
    Solutions = browser.find_element(By.XPATH, "//body/div[@id='___gatsby']/div[@id='gatsby-focus-wrapper']/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]")
    Solutions.click()

    # Wait until the URL changes
    #WebDriverWait(browser, 10).until(EC.url_changes("https://www.entrata.com/"))

    # Verify the actual URL after the click
    print("Actual URL after click:", browser.current_url)

    # Check if the correct URL is navigated after clicking the button
    assert browser.current_url == "https://www.entrata.com/"

def test_form_submission(browser):
    # Open website
    browser.get("https://www.entrata.com/")
    browser.maximize_window()

    # Click on "Watch Demo" button
    search_result = browser.find_element(By.XPATH,
                                         "//body/div[@id='___gatsby']/div[@id='gatsby-focus-wrapper']/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]")
    search_result.click()

    search_result = browser.find_element(By.XPATH,
                                         "//div[@class='header-desktop-buttons hide-on-mobile']//a[@class='button-default solid-dark-button'][normalize-space()='Watch Demo']")
    search_result.click()

    # Explicit wait for the form fields to be clickable
    wait = WebDriverWait(browser, 10)
    first_name = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='FirstName']")))
    last_name = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='LastName']")))
    email = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='Email']")))
    company = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='Company']")))
    phone = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='Phone']")))
    unit_dropdown = wait.until(EC.element_to_be_clickable((By.XPATH, "//select[@id='Unit_Count__c']")))
    job_title = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='Title']")))

    # Fill out the form
    first_name.send_keys("Rahul")
    last_name.send_keys("Thakare")
    email.send_keys("rdthakare95@gmail.com")
    company.send_keys("abc")
    phone.send_keys("9503842121")
    job_title.send_keys("selenium")

    assert first_name.get_attribute('value') == "Rahul"
    assert last_name.get_attribute('value') == "Thakare"
    assert email.get_attribute('value') == "rdthakare95@gmail.com"
    assert company.get_attribute('value') == "abc"
    assert phone.get_attribute('value') == "9503842121"
    assert job_title.get_attribute('value') == "selenium"

def test_links_navigation(browser):
    # Open website
    browser.get("https://www.entrata.com/")
    browser.maximize_window()

    # Store the initial URL
    initial_url = browser.current_url

    # Navigate to another page (for demonstration)
    browser.get("https://www.entrata.com/solutions/")

    # Clicking on some links to generate navigation history
    # For demonstration, you can replace these clicks with actual interactions on the page
    # For example, if there are clickable elements on the page, you can click on them
    # Here, we are just navigating back and forth to generate history
    #browser.back()  # Navigate back to the initial page
    browser.forward()  # Navigate forward again

    # Now, verify if the back and forward buttons are visible
    #assert browser.back()  # Check if the back button is visible
    #assert browser.forward()  # Check if the forward button is visible

    # Perform forward navigation
    browser.forward()

    # Verify that forward navigation has happened by comparing URLs
    assert browser.current_url != initial_url

    # Perform backward navigation
    browser.back()

    # Verify that backward navigation has happened by comparing URLs
    assert browser.current_url == initial_url

if __name__ == "__main__":
        pytest.main()