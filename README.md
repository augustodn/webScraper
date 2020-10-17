# WebScraper installation/setup instructions
In order to use the scraper script properly you have to:

# Install the dependencies
### Linux:
``$ pip install selenium``
``$ pip install parsel``

# Download the driver
You will have to download the correct driver for your **exact** browser version. Please refer to https://www.selenium.dev/downloads/.
Note that the driver version has to match **exactly** with your browser version and has to be placed in the same path as the browser executable.
## Chrome:
1. Get version from
Help/About Chrome
2. Go to https://chromedriver.storage.googleapis.com/index.html
3. Download the correspondent OS version
4. Extract and move it to the folder where chrome is installed
### Linux:

``$ cd ~/Downloads``

``$ unzip chromedriver_linux64.zip``

``$ which google-chrome-stable``

``/usr/bin/google-chrome-stable``

``$ sudo mv chromedriver /usr/bin``
