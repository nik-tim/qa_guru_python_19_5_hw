import os
import time
from selene import browser, by, have


def test_fill_form():

    browser.open('/automation-practice-form')

    browser.element(by.id('firstName')).type('Alice')
    browser.element(by.id('lastName')).type('Smith')
    browser.element(by.id('userEmail')).type('alice.smith@mail.com')

    browser.element(by.xpath('//label[text()="Female"]')).click()

    browser.element(by.id('dateOfBirthInput')).click()
    browser.element(by.class_name('react-datepicker__month-select')).click()
    browser.element(by.xpath('//option[text()="November"]')).click()
    browser.element(by.class_name('react-datepicker__year-select')).click()
    browser.element(by.xpath('//option[text()="1992"]')).click()
    browser.element(by.xpath('//div[@class="react-datepicker__day react-datepicker__day--025"]')).click()

    browser.element(by.id('userNumber')).type('9876543210')

    browser.element(by.id('subjectsInput')).type('Computer Science').press_enter()

    browser.element(by.xpath('//label[text()="Sports"]')).click()

    image_path = os.path.abspath('D:\\cat\\cat.jpg')
    browser.element(by.id('uploadPicture')).send_keys(image_path)

    browser.element(by.id('currentAddress')).type('1234 Elm Street, Springfield')

    browser.element(by.id('state')).click()
    browser.element(by.xpath('//div[text()="Uttar Pradesh"]')).click()
    browser.element(by.id('city')).click()
    browser.element(by.xpath('//div[text()="Agra"]')).click()

    browser.element(by.id('submit')).click()

    browser.element('.modal-header').should(have.text('Thanks for submitting the form'))

    time.sleep(2)

    browser.all('.table-responsive td:nth-child(2)').should(have.texts(
        'Alice Smith',
        'alice.smith@mail.com',
        'Female',
        '9876543210',
        '25 November,1992',
        'Computer Science',
        'Sports',
        'cat.jpg',
        '1234 Elm Street, Springfield',
        'Uttar Pradesh Agra'
    ))
