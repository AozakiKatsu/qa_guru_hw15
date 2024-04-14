from selene import browser, have


def test_github_login_desktop(browser_config_desktop):
    browser.open('https://github.com/')
    browser.all('[href="/login"]').element_by(have.text('Sign in')).click()


def test_github_login_mobile(browser_config_mobile):
    browser.open('https://github.com/')
    browser.all('[href="/login"]').element_by(have.text('Sign in')).click()
