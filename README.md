# Web Service Deployment of a Machine Learning Segmentation Model

## Background
In many industries, the ability to segment an image (divide it into different regions based on certain attributes) can provide critical insights.  
This could involve identifying different objects in a picture or distinguishing areas of interest in medical or satellite images.  
This project deals with a segmentation model written by a data scientist in a Jupyter Notebook that was transitioned into a production-ready system.  
The system is accessible via an HTTP endpoint and should receive images as input, and output segmentation results.   
<br>


## Project Details
This project is a deployable web service utilizing a segmentation model (found in `model_code.ipynb`). The service provides an HTTP endpoint that receives an image as input, uses the model to perform segmentation, and returns the segmented image.

> Note: The code is compatible with Python 3.8
<br>


## Docker
The application is Dockerized using `Docker`.

#### Command to build the image file:
```
docker build -t idansm/segmentation-server:1.0 . --platform linux/amd64
```
> Note: remove `--platform linux/amd64` to build a docker image that is compatible with the host OS (Perform only on MacOS, on Linux and Windows keep the tag)
   
#### Command to create a docker container from the image file created (running on port 8989 both internally in the container and on the outside):
```
docker run --name segmentation-server -p 8989:8989 segmentation-server:1.0
```
   
#### Command to run the docker container pulled from docker-hub:
```
docker run --name segmentation-server -p 8989:8989 idansm/segmentation-server:1.0
```
<br>


## Deliverables
A zip file that can be extracted and includes:
A batch/shell files that runs the service.
Everything you need to run your service (you can assume Python version 3.8 exists on the machine).
A postman collection file that contains the example of how to run your service.
A README word document that describes in highlights your considerations, assumptions and intentions when you did this specific implementation. 
