import pytest
from selene import browser


@pytest.fixture(params=[('1920', '1080'), ('1680', '1050')], scope='function',
                ids=['1920', '1680'])
def browser_config_desktop(request):
    width, height = request.param
    browser.config.window_width = width
    browser.config.window_height = height


@pytest.fixture(params=[('360', '640'), ('412', '740')], scope='function',
                ids=['360', '412'])
def browser_config_mobile(request):
    width, height = request.param
    browser.config.window_width = width
    browser.config.window_height = height


@pytest.fixture(params=[('1920', '1080'), ('412', '740')], scope='function',
                ids=['Desktop', 'Mobile'])
def browser_config(request):
    width, height = request.param
    browser.config.window_width = width
    browser.config.window_height = height
    if int(width) > 800:
        yield "desktop"
    else:
        yield "mobile"
