def validate_image_size(image):
    if image.size > 5 * 1024 * 1024:  # 5 MB limit
        raise ValueError("Image size should not exceed 5 MB.")