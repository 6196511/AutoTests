from selenium.webdriver.common.by import By
from webium import BasePage, Find, Finds


class NavigationBar(BasePage):

    url = 'https://ci004.godo.io/dashboard.aspx'

    page_loader_wrapper = Find(by=By.XPATH, value="//div[@class='page-loader-wrapper']")
    godo_lodo = Find(by=By.XPATH, value="//a[@class = 'logo']")
    navigation_bar = Finds(by=By.XPATH, value="//ul[@class='nav navbar-nav navbar-right']")
    time_tracker = Find(by=By.XPATH, value="//div[@class = 'switch-button-background']")
    time_tracker_checked = Find(by=By.XPATH, value="//div[@class = 'switch-button-background checked']")
    menu_drop_down = Find(by=By.XPATH, value="//a[contains(@class, 'user-name')]")

    main_tab = Find(by=By.XPATH, value="//a[@href='#menu']")
    sell_tickets = Find(by=By.XPATH, value="//a//span[text()='Sell Tickets']")
    add_booking = Find(by=By.XPATH, value="//a[@href='/add_booking.aspx']")
    sell_gift_certificate = Find(by=By.XPATH, value="//a[@href = 'giftcertificate.aspx']")

    products = Find(by=By.XPATH, value="//a//span[text()='Products']")
    product_hub = Find(by=By.XPATH, value="//a[text()='Product Hub']")
    gift_certificates = Find(by=By.CSS_SELECTOR, value="[href = 'giftcertificate.aspx']")


    calendar = Find(by=By.XPATH, value="//li/a[@href='event_calendar.aspx']")

    profile_pic = Find(by=By.XPATH, value="//div[contains(@class, 'user-account')]/img")
    profile_pics = Finds(by=By.XPATH, value="//div[contains(@class, 'user-account')]/img")

    # Your Hubs navigation bar.

    sitemap = Find(by=By.XPATH, value="//i[@class='fa fa-sitemap']")
    activities = Find(by=By.XPATH, value="//a//span[text()='Activities']")
    activity_hub = Find(by=By.XPATH, value="//a[text()='Activity Hub']")
    addons = Find(by=By.XPATH, value="//a[text()='Add-Ons']")
    marketing_hub = Find(by=By.XPATH, value="//a//span[text()='Marketing and Sales']")
    expanded_list = Find(by=By.XPATH, value="//ul[@aria-expanded='true']")
    groupon = Find(by=By.XPATH, value="//a[text()='Groupon']")

    people = Find(by=By.XPATH, value="//a//span[text()='People']")
    people_hub = Find(by=By.XPATH, value="//li//a[text()='People Hub']")
    add_guide = Find(by=By.XPATH, value="//li//a[text()='Add a Guide/Leader']")

    logout = Find(by=By.XPATH, value="//ul/li/a[text()='Logout']")

    def scrollIntoView(self, element):
        self._driver.execute_script("arguments[0].scrollIntoView(true);", element)
