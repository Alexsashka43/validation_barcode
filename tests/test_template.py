import datetime

import allure
import jsonschema
import jsonschema.exceptions


import pytest

from conftest import list_description
from core.parser_pdf import extract_text_from_pdf, resources_path
from scheme.schema_template import schema

from tests.params_for_tests import exp_date, description, dom, rec_date


@pytest.mark.smoke
@allure.step
@allure.title("Validation_schema")
def test_validation_schema():
    try:
        jsonschema.validate(instance=extract_text_from_pdf(resources_path), schema=schema)
    except jsonschema.exceptions.ValidationError as e:
        raise AssertionError(f"JSON data does not match schema: {e}")


''' Не уверен в некоторых аббревиатурах и сокращениях:
dom - дата изготовления,
rec.date - дата получения, 
expiry_date - срок годности 
Имея на руках документацию, можно покрыть остальные параметры.
'''


@pytest.mark.smoke
@allure.step
@allure.title("Check_exp_date_and_current_date")
@pytest.mark.parametrize("expiry_date", [exp_date])
def test_exp_date_and_current_date(expiry_date):
    current_date = datetime.date.today()
    assert expiry_date > current_date, f'The expiration date: {expiry_date} is greater than the current date'


@pytest.mark.smoke
@allure.step
@allure.title("Check_exp_date_and_DOM")
@pytest.mark.parametrize("expiry_date,dom", [(exp_date, dom)])
def test_exp_date_and_dom(expiry_date, dom):
    assert expiry_date > dom, f'The expiration date: {expiry_date} equal or less than the date of manufacture: {dom}'


@pytest.mark.smoke
@allure.step
@allure.title("Check_exp_date_and_rec_date")
@pytest.mark.parametrize("expiry_date,rec_date", [(exp_date, rec_date)])
def test_exp_date_and_rec_date(expiry_date, rec_date):
    assert expiry_date > rec_date, f'The expiration date: {expiry_date} is greater than the date received: {rec_date}'


@pytest.mark.smoke
@allure.step
@allure.title("Check_rec_date_and_DOM")
@pytest.mark.parametrize("rec_date,dom", [(rec_date, dom)])
def test_rec_date_and_dom(rec_date, dom):
    assert rec_date > dom, f'The date of manufacture: {dom} is greater than the date received: {rec_date}'


@pytest.mark.smoke
@allure.step
@allure.title("Check_text_description")
@pytest.mark.parametrize("description", [description, pytest.param('smth', marks=pytest.mark.xfail(reason='This type will be added to the task ...'))])
def test_text_description(description):
    assert description in list_description, f'Value: {description} is not in the list of description'
