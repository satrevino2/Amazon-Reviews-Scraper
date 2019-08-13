# Amazon-Reviews-Scraper

This code is written to scrape O.R.S amazon reviews content from both United States and United Kingdom platforms and writes it into a csv file.

## Prerequisites

This code runs off of Python 3, asssuming you already have that installed, the things you need to install and how to install them:

```
pip install selenium
```
```
pip install beautifulsoup4
```
```
pip install requests
```

### Usage
1. It is important to install ChromeDriver, otherwise selenium will not be able to operate.

   * Once ChromeDriver is installed, be sure to identify its executable path on your device and add it into ```driver = webdriver.Chrome(executable_path = "/Users/stephanie/Downloads/chromedriver")```

2. The url is set by default for O.R.S Hydration tablets, but if necessary, the url can be adjusted accordingly. 

3. The number of page(s) that are scrapped can be adjusted accordingly within the for loop: ```for i in range(1,2):```

### Running
1. Open your terminal.

2. Change directory into the folder the python code is located in.

3. Finally, enter in your terminal: ```python3 amazon_scraper.py```
