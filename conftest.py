import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None,
                     help="Choose language: es, ru...")



@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption("language")
    browser = None
    if language is not None:
        print(f"\nstart chrome browser for test. selected language is {language}")
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': language})
        browser = webdriver.Chrome(options=options)
    else:
        raise pytest.UsageError("--language should be selected")
    yield browser
    print("\nquit browser..")
    browser.quit()