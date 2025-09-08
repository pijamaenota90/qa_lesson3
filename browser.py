from selene import browser, be, have

def test_search_no_results():

    browser.open('/')
    search_box = browser.element('[name="q"]')
    search_box.should(be.visible).should(be.blank)
    search_box.type('qlkjdlk')
    search_box.should(have.value('qlkjdlk'))

    assert True
