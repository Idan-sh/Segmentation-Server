## Deploying a Machine Learning Segmentation Model as a Web Service

### Background:
In many industries, the ability to segment an image – divide it into different regions based on certain attributes – can provide critical insights.  
This could involve identifying different objects in a picture, or distinguishing areas of interest in medical or satellite images.  
This assignment will deal with a segmentation model written by a data scientist in a Jupyter notebook that needs to be transitioned into a production-ready system.  
The system should be accessible via an HTTP endpoint and should receive images as input, and output segmentation results.   

Please note that in our workflow this happens often - a data scientist builds a model based on the tools he is used to work with (like Jupyter notebooks) and afterwards we need to expose those as webservices.  
This is an iterative process that results in multiple applications under the proposed paradigm.


### Problem Statement:
Your task is creating a deployable web service utilizing a segmentation model (found in model_code.ipynb).  
The service should provide an HTTP endpoint that receives an image as an input, uses the model to perform segmentation, and returns the segmented image. The code needs to be compatible with Python 3.8.

### Bonus Tasks: 
Provide an additional endpoint for batch requests (multiple inputs)
Dockerize the application (bonus: include docker-compose)

### Deliverables:
A zip file that can be extracted and includes:
A batch/shell files that runs the service.
Everything you need to run your service (you can assume Python version 3.8 exists on the machine).
A postman collection file that contains the example of how to run your service.
A README word document that describes in highlights your considerations, assumptions and intentions when you did this specific implementation. 
