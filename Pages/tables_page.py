from selenium.webdriver.common.by import By

class TablesPage:
    def __init__(self, driver):
        self.driver = driver
        self.table_id = "table1"

    def open(self):
        self.driver.get("https://the-internet.herokuapp.com/tables")

    def get_table_data(self):
        headers = [
            header.text for header in self.driver.find_elements(
                By.XPATH, f"//table[@id='{self.table_id}']//thead//th"
            )
        ]
        rows = self.driver.find_elements(By.XPATH, f"//table[@id='{self.table_id}']//tbody/tr")

        table_data = []
        for row in rows:
            cols = [col.text for col in row.find_elements(By.XPATH, ".//td")]
            row_dict = dict(zip(headers, cols))
            table_data.append(row_dict)
        return table_data
