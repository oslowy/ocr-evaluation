def split_batch(image_names, max_items_per_sub):
    return [image_names[sublist_start: sublist_start + max_items_per_sub]
            for sublist_start in range(0, len(image_names), max_items_per_sub)]


def join_responses(response_batches):
    return {image_name: batch[image_name] for batch in response_batches for image_name in batch}
