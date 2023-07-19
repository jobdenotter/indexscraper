from selenium import webdriver


def get(url: str) -> str:
    """Get html from url using selenium webdriver"""
    driver = webdriver.Chrome()
    driver.get(url)
    html = driver.page_source
    driver.close()
    return html
