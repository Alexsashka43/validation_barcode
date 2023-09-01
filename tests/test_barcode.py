import allure
import pytest

from tests.params_for_tests import list_data_barcodes, list_barcodes_positions, list_orientation, \
    list_type_barcode, get_text_for_barcode, correct_positoins


@pytest.mark.smoke
@allure.step
@allure.title("Check_info_barcodes")
def test_info_barcode():
    assert list_data_barcodes == get_text_for_barcode(), 'The information on the template does not match the information ' \
                                                         'in the barcode'


@pytest.mark.smoke
@allure.step
@allure.title("Check_position_barcodes")
def test_position_barcodes():
    assert list_barcodes_positions == correct_positoins, 'Incorrect location of barcodes'


@pytest.mark.smoke
@allure.step
@allure.title("Check_orientation_barcodes")
def test_orientation_barcodes():
    assert all(x == 'UP' for x in list_orientation), 'Incorrect orientation of barcodes'


@pytest.mark.smoke
@allure.step
@allure.title("Check_type_barcodes")
def test_type_barcodes():
    assert all(x == 'CODE128' for x in list_type_barcode), 'Incorrect orientation of barcodes'
