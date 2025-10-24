import pytest
from Pages.login_page import LoginPage
from Pages.tables_page import TablesPage

@pytest.mark.smoke
def test_table_data(driver):
    # Step 1️: Login
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login("tomsmith", "SuperSecretPassword!")

    #  Validation 1: Verify login success
    success_message = login_page.get_success_message()
    assert "You logged into a secure area!" in success_message, " Login failed!"

    # Step 2️: Go to tables page
    tables_page = TablesPage(driver)
    tables_page.open()

    # Step 3️: Fetch and validate table data
    table_data = tables_page.get_table_data()

    # Validation 2: Table is not empty
    assert len(table_data) > 0, "Table data is empty!"

    #  Validation 3: Check column names
    expected_columns = ['Last Name', 'First Name', 'Email', 'Due', 'Web Site', 'Action']
    for col in expected_columns:
        assert col in table_data[0], f" Missing column: {col}"

    #  Validation 4: Verify specific user data (Smith)
    smith_record = next((r for r in table_data if r["Last Name"] == "Smith"), None)
    assert smith_record is not None, " Smith record not found!"
    assert smith_record["Email"] == "jsmith@gmail.com", " Smith email mismatch!"

    #  Optional: Print for debug
    print("\n All validations passed successfully!")
    for record in table_data:
        print(record)
