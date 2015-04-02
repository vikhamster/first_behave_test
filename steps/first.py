"""

Feature: Authentification on server

   Scenario: Active sender can successfully authentificats on server
     Given customer has an active sender
     And mail server
     When customer try to authentificate active sender on mail server
     Then active sender is successfully authentificated



"""


from behave import given, when, then
from mta import Authentification
from mta import get_active_sender_login
from mta import get_active_sender_password
from nose.tools import eq_

@given('customer has an active sender')
def step_get_sender_credantials(context):
    context.sender_name = get_active_sender_login()
    context.sender_password = get_active_sender_password()


@when('customer try to authentificate active sender on server')
def send(context):
    context.auth_try = Authentification()
    result = context.auth_try.auth(context.sender_name, context.sender_password)


@then('active sender is successfully authentificated')
def auth_is_success(context):
    eq_(result, 235, msg = None)


