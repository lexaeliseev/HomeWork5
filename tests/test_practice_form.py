import time

from selene import browser, have, be, command


def test_practice_form():
    browser.open("https://demoqa.com/automation-practice-form")

    browser.element('[id="firstName"]').should(be.blank).type("Алексей")
    browser.element('[id="firstName"]').should(have.value("Алексей"))

    browser.element('[id="lastName"]').should(be.blank).set_value("Елисеев")
    browser.element('[id="lastName"]').should(have.value("Елисеев"))

    browser.element('[id="userEmail"]').should(be.blank).type("qaguru@test.com")
    browser.element('[id="userEmail"]').should(have.value("qaguru@test.com"))

    browser.element('//label[contains(text(),"Male")]').click()
    # нет проверки, что выбран Male

    browser.element('[id="userNumber"]').should(be.blank).set_value("9999999999")
    browser.element('[id="userNumber"]').should(have.value("9999999999"))

    browser.element('[id="dateOfBirthInput"]').click()
    browser.element(".react-datepicker__year-select").click().element('[value="1992"]').click()
    browser.element(".react-datepicker__month-select").click().element('//option[contains(text(),"April")]').click()
    browser.element(".react-datepicker__day--014").click()




    # # browser.element('id="subjectsContainer"').click()
    #
    # browser.element('[subjects-auto-complete__control css-yk16xz-control]').click()
    # browser.element('[class="subjects-auto-complete__value-container subjects-auto-complete__value-container--is-multi css-1hwfws3"]').click()
    #
    # browser.element('[id="react-select-2-option-0"]').click()

    time.sleep(3)