import json
import os
import sys
from datetime import datetime

import requests
import concurrent.futures as thread

import api_connect
import subbatch
from datetime_format import datetime_format


def send_batch(image_names, is_processing_on, platform):
    print(f"Sending batch starting with: {image_names[0]}")
    
    return {image_name:
            requests.post(url=api_connect.select_url(platform),
                          json=api_connect.package_data(image_name, is_processing_on),
                          headers={"Content-Type": "application/json"})
            for image_name in image_names}


def main():
    args = sys.argv[1:]
    image_names_filename = args[0]
    is_processing_on = args[1] == 'True'
    platform = args[2]

    # Read list of image filenames
    with open(image_names_filename) as image_names_file:
        image_names = [image_name.rstrip() for image_name in image_names_file]

    # Split list of names into batches
    image_name_batches = subbatch.split_batch(image_names, max_items_per_sub=10)

    with thread.ThreadPoolExecutor(max_workers=10) as tpx:
        # Fan out threads with one batch of names per thread
        futures = [tpx.submit(send_batch, batch, is_processing_on, platform)
                   for batch in image_name_batches]

        # Collect the responses
        all_responses = subbatch.join_responses([future.result()
                                                 for future in thread.as_completed(futures)])

    # Write the responses to files
    datetime_finished = datetime.now().strftime(datetime_format)
    print(f"Finished at {datetime_finished}. Writing to files...")

    directory = f"ocr-batch_{platform}_{is_processing_on}_{datetime_finished}"
    os.mkdir(directory)

    for image_name in all_responses:
        open(f"{directory}/{image_name[:5]}.txt", 'w').write(json.dumps(all_responses[image_name].json()))


if __name__ == "__main__":
    main()
