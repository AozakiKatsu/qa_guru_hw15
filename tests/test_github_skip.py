import pytest
from selene import browser, have


def test_github_skip_desktop(browser_config):
    if browser_config == "mobile":
        pytest.skip("Мобильное разрешение")
    browser.open("https://github.com/")
    browser.all('[href="/login"]').element_by(have.text('Sign in')).click()


def test_github_skip_mobile(browser_config):
    if browser_config == "desktop":
        pytest.skip("Десктоп")
    browser.open("https://github.com/")
    browser.all('[href="/login"]').element_by(have.text('Sign in')).click()
