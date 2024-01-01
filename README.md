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

To run the segmentation server, you can clone the project, and then run the included bash script `run_server.sh`.   
Alternatively, you can use Docker using the instructions below.   
   
Inside the `additional_files` folder, you can find the postman collection `Segmentation Server.postman_collection.json`,
which contains an example on how to run the service.   

Furthermore, inside said folder you can find a README Word document that describes in highlights my considerations, assumptions, and intentions on this specific implementation. 
This document also contains more details about the project's structure, the running process of the service, and the web service's endpoints.
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
