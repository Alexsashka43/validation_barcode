import cv2
from pyzbar.pyzbar import decode
from pdfminer.high_level import extract_text
from pdf2image import convert_from_path

from conftest import resources_path, name_file, poppler_path, list_fields_int


def extract_text_from_pdf(resources_path):
    text = extract_text(f'{resources_path}{name_file}.pdf')
    data_dict = {}
    for item in text.split('\n\n'):
        parts = item.split(':')
        if len(parts) == 2:
            key, value = parts
            key = key.strip().replace(' ', '_').replace('.', '_').replace('#', '')
            if key in list_fields_int:
                value = int(value.strip())
            data_dict[key] = value
    return data_dict


def pdf_to_image(resources_path):
    images = convert_from_path(
        f'{resources_path}{name_file}.pdf', poppler_path=poppler_path)
    for i in range(len(images)):
        images[i].save(f'{resources_path}{name_file}_{i + 1}.png', 'PNG')


def barcode_reader(image):
    pdf_to_image(resources_path)
    img = cv2.imread(image)
    detected_barcodes = decode(img)
    return detected_barcodes
