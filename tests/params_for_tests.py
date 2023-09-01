import datetime
from pyzbar.locations import Point
from conftest import name_file, resources_path
from core.parser_pdf import barcode_reader, extract_text_from_pdf

param_from_barcodes = barcode_reader(f'{resources_path}{name_file}_1.png')
param_from_pdf = extract_text_from_pdf(resources_path)

correct_positoins = [[Point(x=56, y=431), Point(x=56, y=511), Point(x=227, y=512), Point(x=227, y=430)], [Point(x=38, y=51), Point(x=38, y=107), Point(x=717, y=106), Point(x=717, y=50)]]

list_data_barcodes = []
list_param_barcodes = []
list_barcodes_positions = []
list_orientation = []
list_type_barcode = []


exp_date = datetime.datetime.strptime(param_from_pdf['EXP_DATE'].strip(), "%d.%m.%Y").date()
rec_date = datetime.datetime.strptime(param_from_pdf['REC_DATE'].strip(), "%d.%m.%Y").date()
dom = datetime.datetime.strptime(param_from_pdf['DOM'].strip(), "%d.%m.%Y").date()
description = param_from_pdf['DESCRIPTION'].strip()


for barcode in param_from_barcodes:
    list_data_barcodes.append(barcode.data)
    list_barcodes_positions.append(barcode.polygon)
    list_orientation.append(barcode.orientation)
    list_type_barcode.append(barcode.type)


def get_text_for_barcode():
    list_param_barcodes.append(bytes(str(param_from_pdf['Qty']).strip(), 'utf-8'))
    list_param_barcodes.append(bytes(param_from_pdf['PN'].strip(), 'utf-8'))
    return list_param_barcodes
