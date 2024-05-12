from selenium import webdriver
import pytest
from data import URL


@pytest.fixture
def driver():
    firefox = webdriver.Firefox()
    firefox.get(URL)

    yield firefox

    firefox.quit()
