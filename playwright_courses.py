from playwright.sync_api import sync_playwright, expect
from config import CHROMIUM_EXECUTABLE

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(executable_path=CHROMIUM_EXECUTABLE, headless=False)
    context = browser.new_context()
    page = context.new_page()

    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

    email_input = page.get_by_test_id('registration-form-email-input').locator('input')
    expect(email_input).to_be_visible()
    email_input.fill("user.name@gmail.com")

    username_input = page.get_by_test_id('registration-form-username-input').locator('input')
    expect(username_input).to_be_visible()
    username_input.fill("username")

    password_input = page.get_by_test_id('registration-form-password-input').locator('input')
    expect(password_input).to_be_visible()
    password_input.fill("password")

    registration_button = page.get_by_test_id('registration-page-registration-button')
    expect(registration_button).to_be_enabled()
    registration_button.click()

    context.storage_state(path="browser-state.json")

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False, executable_path=CHROMIUM_EXECUTABLE)
    context = browser.new_context(storage_state="browser-state.json")
    page = context.new_page()

    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")

    courses_h6 = page.get_by_test_id('courses-list-toolbar-title-text')
    expect(courses_h6).to_be_visible()
    expect(courses_h6).to_have_text("Courses")

    courses_empty_icon_svg = page.get_by_test_id('courses-list-empty-view-icon')
    expect(courses_empty_icon_svg).to_be_visible()

    courses_empty_title_h6 = page.get_by_test_id('courses-list-empty-view-title-text')
    expect(courses_empty_title_h6).to_be_visible()
    expect(courses_empty_title_h6).to_have_text("There is no results")

    courses_empty_description_h6 = page.get_by_test_id('courses-list-empty-view-description-text')
    expect(courses_empty_description_h6).to_be_visible()
    expect(courses_empty_description_h6).to_have_text("Results from the load test pipeline will be displayed here")
