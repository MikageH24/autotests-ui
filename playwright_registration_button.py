from playwright.sync_api import sync_playwright, expect
from config import CHROMIUM_EXECUTABLE

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(executable_path=CHROMIUM_EXECUTABLE, headless=False)
    page = browser.new_page()

    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")
    registration_button = page.get_by_test_id('registration-page-registration-button')
    expect(registration_button).to_be_disabled()

    email_input = page.get_by_test_id('registration-form-email-input').locator('input')
    expect(email_input).to_be_visible()
    email_input.fill("user.name@gmail.com")

    username_input = page.get_by_test_id('registration-form-username-input').locator('input')
    expect(username_input).to_be_visible()
    username_input.fill("username")

    password_input = page.get_by_test_id('registration-form-password-input').locator('input')
    expect(password_input).to_be_visible()
    password_input.fill("password")

    expect(registration_button).to_be_enabled()
