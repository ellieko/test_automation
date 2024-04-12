# Test Automation for Scaling App

## 1. Setup Requirments
### 1. Install Python, Selenium, and Chrome
- Ensure Python 3.8 or later is installed
- Ensure pip, Python's package installer, is installed (https://pip.pypa.io/en/stable/installation/)
- Install Selenium: In terminal, "pip install selenium" (https://pypi.org/project/selenium/)
- Download and install the appropriate version of Google Chrome from the official page, https://www.google.com/chrome/

### 2. Download and Configure Chrome Web Driver
- MacOS users who have installed "brew", simply run "brew install chromedriver" in terminal.
- Others
  - Check your Chrome version by typing "chrome://version" in your chrome browser
  - Download the corresponding version of chrome web driver from the Chrome Driver download page, https://chromedriver.chromium.org/downloads
  - Place chromedriver.exe (for Windows users) or chromedriver (for Mac or Linux users) in a directory included in your system's PATH

## 2. Run Test Automation Script to Find a Fake Bar

Run the findFakeBar.py to initiate test automation. This will launch a chrome browser and conduct weighings of gold bars until a fake one is detected. You'll able to see the process of finding a fake bar in the opened browser but aslo in your terminal.

Terminal output example)

![image](https://github.com/ellieko/test_automation/assets/70093034/63d868f2-2e27-489e-b0c1-089382dd079b)
