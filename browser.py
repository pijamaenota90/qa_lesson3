from selene import browser, be, have

def test_search():
    browser.open('/')
    browser.element('#text').should(be.blank).type('qa.guru').press_enter()
    browser.element('#search-result').should(have.text('QA.GURU'))


def test_search_no_results():

    browser.open('https://google.com/')
    search_box = browser.element('[name="q"]')
    search_box.should(be.visible).should(be.blank)
    search_box.type('qlkjdlk')
    search_box.should(have.value('qlkjdlk'))

    assert True
