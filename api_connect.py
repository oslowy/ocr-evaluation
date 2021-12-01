import json


def package_data(image_name, is_processing_on, thresh_window_size, platform='google'):
    data = {
        "data": {
            "filename": image_name,
            "is_processing_on": is_processing_on,
            "approach": {
                "morph_kernel_size": 3,
                "gauss_kernel_size": 5,
                "thresh_window_size": thresh_window_size,
                "thresh_C": 2
            }
        }
    }

    if platform == 'google':
        return data
    return {
        "body": data
    }


def select_url(platform='google'):
    if platform == 'google':
        return "https://us-east1-essential-text-330923.cloudfunctions.net/ocr-onefunction"
    return "https://exhtaawacg.execute-api.us-east-1.amazonaws.com/OCRText/lambda"
