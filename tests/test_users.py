from faker import Faker

from tests.utils.pages.sign_up import SignUpPage

def test_user_creation(action):
    fake = Faker()
    password = fake.password()
    action.navigate()
    action.click('//a[text()="Sign Up"]')
    action.enter_text(SignUpPage.email, fake.email())
    action.enter_text(SignUpPage.pass1, password)
    action.enter_text(SignUpPage.pass2, password)
    action.click(SignUpPage.submit)
    assert action.element_has_text('This account is inactive')
