from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
import time

# Function to click the chosen fake bar
def clickFakeBar(driver, a):
    print(f"Fake bar should be {a}.")
    button = driver.find_element(By.ID, f"coin_{a}")
    button.click()
    print(Alert(driver).text)


if __name__ == "__main__":

    # Initialize the WebDriver
    driver = webdriver.Chrome()

    # Navigate to a website
    driver.get("http://sdetchallenge.fetch.com/")

    stack = list(range(9))
    weighings = []
    
    while stack:
        
        if len(stack) == 1:
            clickFakeBar(driver, stack.pop())
            break

        # Put two bars on each side
        a, b = stack.pop(), stack.pop()
        input_field = driver.find_element(By.ID, "left_0")
        input_field.send_keys(a)
        input_field = driver.find_element(By.ID, "right_0")
        input_field.send_keys(b)

        # Weigh the scaling
        weigh_button = driver.find_element(By.ID, "weigh")
        weigh_button.click()
        time.sleep(3)

        # Append the weighing result and check if there is a fake bar
        weighing_result = driver.find_elements(By.ID, "reset")[0].text
        weighings.append(f"{len(weighings)}th weighing: {a} {weighing_result} {b}")
        print(weighings[-1])

        if weighing_result == "<":
            clickFakeBar(driver, a)
            break
        elif weighing_result == ">":
            clickFakeBar(driver, b)
            break
        else:
            # Reset the scaling
            reset_element = driver.find_elements(By.ID, "reset")[1]
            reset_element.click()

    print(f"We Found the fake bar within {len(weighings)} times of weighings.")

    # Close the browser window
    driver.quit()