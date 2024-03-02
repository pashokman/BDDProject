from behave import *


@given(u'I navigate to login page')
def step_impl(context):
    print('Inside - I navigate to login page')


@when(u'I enter valid Email as "{email}" and valid Password as "{password}" into the fields')
def step_impl(context, email, password):
    print(f'I enter valid Email as "{email}" and valid Password as "{password}" into the fields')


@when(u'I click on Login button')
def step_impl(context):
    print('Inside - I click on Login button')


@then(u'I should get successfully logged in')
def step_impl(context):
    print('Inside - I should get successfully logged in')


@when(u'I enter valid email and invalid password into the fields')
def step_impl(context):
    print('Inside - I enter valid email and invalid password into the fields')


@then(u'I should get a proper warning message')
def step_impl(context):
    print('Inside - I should get a proper warning message')
          

@when(u'I enter invalid email and valid password into the fields')
def step_impl(context):
    print('Inside - I enter invalid email and valid password into the fields')