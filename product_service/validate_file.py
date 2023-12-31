from django.contrib import messages


def validate_image_size(request, image):
    ''' Validate images based on the following conditions '''

    max_upload_size = 500000  # 500KB in bytes
    if image.size > max_upload_size:
        messages.error(request, "File size must not exceed 500KB.")
        return False
    return True


def validate_file_size(request, file):
    ''' Validate files based on the following conditions '''

    max_upload_size = 500000000  # 500MB in bytes
    if file.size > max_upload_size:
        messages.error(request, "File size must not exceed 500MB.")
        return False
    return True
