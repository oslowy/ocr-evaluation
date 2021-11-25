import json


def package_data(image_name, is_processing_on):
    return {
        "data": {
            "filename": image_name,
            "is_processing_on": is_processing_on,
            "approach": {
                "morph_kernel_size": 3,
                "gauss_kernel_size": 5,
                "thresh_window_size": 51,
                "thresh_C": 2
            }
        }
    }


def select_url(platform='google'):
    return "https://us-east1-essential-text-330923.cloudfunctions.net/ocr-onefunction" \
        if platform == 'google' else ""
