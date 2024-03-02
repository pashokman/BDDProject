from behave import given, when, then


@given(u'I am on the Application Home page')
def step_impl(context):
    print('Inside - I am on the Application Home page')


@when(u'I enter valid product "{product}" into Search box field')
def step_impl(context, product):
    print(f'Inside - I enter valid product - {product} into Search box field')


@when(u'I click on Search button')
def step_impl(context):
    print('Inside - I click on Search button')


@then(u'Valid product should be displayed in Search results page')
def step_impl(context):
    print('Inside - Valid product should be displayed in Search results page')


@when(u'I enter invalid product "{product}" into Search box field')
def step_impl(context, product):
    print(f'Inside - I enter invalid product - {product} into Search box field')


@then(u'Proper message should be displayed in Search results page')
def step_impl(context):
    print('Inside - Proper message should be displayed in Search results page')


@when(u'I don\'t enter any product into Search box field')
def step_impl(context):
    print('Inside - I don\'t enter any product into Search box field')