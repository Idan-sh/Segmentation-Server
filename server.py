import http
import shutil
from pathlib import Path

from flask import Flask, request, send_file, Request

import model
import server_functions
import server_properties

app = Flask(__name__)
server_logger = server_functions.setup_server_logger()
request_logger = server_functions.setup_request_logger()


def generate_request_message(req: Request) -> str:
    return 'Method= \'' + req.method + '\', Endpoint= \'/' + req.endpoint + '\''


@app.route('/', methods=['GET'])
def home():
    request_logger.info(generate_request_message(request))
    server_logger.info('Sent response that the server is up and running')
    return 'Server is running!', http.HTTPStatus.OK


@app.errorhandler(http.HTTPStatus.NOT_FOUND)
def not_found_error(error):
    server_logger.error('Received bad endpoint')
    return 'Error: The requested resource was not found', http.HTTPStatus.NOT_FOUND


@app.errorhandler(http.HTTPStatus.INTERNAL_SERVER_ERROR)
def internal_server_error(error):
    server_logger.error('Internal server error occurred')
    return 'Error: An internal server error occurred', http.HTTPStatus.INTERNAL_SERVER_ERROR


@app.route('/perform-segmentation', methods=['POST'])
def handle_post_request():
    request_logger.info(generate_request_message(request))

    # Check for input errors:
    if 'image' not in request.files:
        server_logger.error('No image key received')
        return 'No \'image\' key found in the request', http.HTTPStatus.BAD_REQUEST

    images = request.files.getlist('image')

    if len(images) == 0 or images[0].filename == '':
        server_logger.error('No image uploaded')
        return 'No image uploaded', http.HTTPStatus.BAD_REQUEST

    if len(images) > 1:
        server_logger.error('Received more than 1 image')
        return 'Received more than 1 image\nTo send more than 1 image please use the ' \
               '\'/perform-multi-segmentation\' endpoint', http.HTTPStatus.BAD_REQUEST

    # Access the data from the POST request
    image_file = request.files['image']

    if not server_functions.allowed_file(image_file.filename):
        server_logger.error('Invalid image format')
        return 'File received is in an invalid format', http.HTTPStatus.BAD_REQUEST

    # input is valid, process it:
    server_functions.create_directories()
    server_logger.info('Got image ' + image_file.filename)
    server_logger.debug('Initialized input and output directories')

    # Save the image to process it
    image_file.save(server_properties.images_to_segment_directory_path + image_file.filename)
    image_path = server_properties.images_to_segment_directory_path + image_file.filename

    segmented_image = model.process_image_and_predict(str(image_path))
    server_logger.info('processed image ' + image_file.filename)

    # Save the segmented image
    segmented_image.save(server_properties.images_after_segment_directory_path + image_file.filename)
    segmented_image_path = Path(server_properties.images_after_segment_directory_path + image_file.filename)
    server_logger.info('Saved segmented image ' + image_file.filename)

    # return result
    server_logger.info('Sending segmented image as response')
    return send_file(segmented_image_path, mimetype='image/jpeg', as_attachment=True), http.HTTPStatus.OK


@app.route('/perform-multi-segmentation', methods=['POST'])
def handle_multi_post_request():
    request_logger.info(generate_request_message(request))

    # Check for input errors:
    if 'images' not in request.files:
        server_logger.error('No image key received')
        return 'No \'images\' key found in the request', http.HTTPStatus.BAD_REQUEST

    images = request.files.getlist('images')

    if len(images) == 0 or images[0].filename == '':
        server_logger.error('No images uploaded')
        return 'No images uploaded', http.HTTPStatus.BAD_REQUEST

    # Input is valid, process it:
    server_functions.create_directories()
    server_logger.debug('Initialized input and output directories')

    # Access the data from the POST request
    images_files = request.files.getlist('images')

    # Process the images
    for image_file in images_files:
        if image_file and server_functions.allowed_file(image_file.filename):
            server_logger.info('Got image ' + image_file.filename)
            # Save the image
            image_file.save(server_properties.images_to_segment_directory_path + image_file.filename)
            image_path = server_properties.images_to_segment_directory_path + image_file.filename

            # Process the image
            segmented_image = model.process_image_and_predict(str(image_path))

            server_logger.info('processed image ' + image_file.filename)

            # Save the segmented image
            segmented_image.save(server_properties.images_after_segment_directory_path + image_file.filename)

            server_logger.info('Saved segmented image ' + image_file.filename + '\n')

    # Create a zip archive of all the segmented images
    shutil.make_archive('archives/archive', 'zip', root_dir=None, base_dir='segmented_images')
    server_logger.info('Created archive of segmented images')

    # return segmented images
    server_logger.info('Sending archive as response')
    return send_file('archives/archive.zip', as_attachment=True), http.HTTPStatus.OK


if __name__ == '__main__':
    # Start the server with the defined port and host ip
    print(' * Running server on: http://localhost' + ':' + str(server_properties.SERVER_PORT))
    app.run(port=server_properties.SERVER_PORT, host=server_properties.SERVER_HOST)
