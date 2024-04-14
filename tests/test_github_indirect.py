import pytest
from selene import browser, have, query


@pytest.mark.parametrize("browser_config_desktop", [('1200', '1200')], indirect=True)
def test_github_desktop(browser_config_desktop):
    browser.open('https://github.com/')
    browser.all('[href="/login"]').element_by(have.text('Sign in')).click()


@pytest.mark.parametrize("browser_config_mobile", [('300', '600')], indirect=True)
def test_github_desktop(browser_config_mobile):
    browser.open('https://github.com/')
    browser.all('[href="/login"]').element_by(have.text('Sign in')).click()
