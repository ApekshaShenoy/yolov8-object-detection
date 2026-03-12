# Object Detection Project Documentation

Team Members

Krishna Koumudi Koravi , Apeksha Mangalpady

## Dataset Collection

For this project, we created a custom dataset to detect three everyday objects:

* **Bottle**
* **Cup**
* **Phone**

Instead of manually capturing all images, we used an automated image scraping approach to gather a larger set of images efficiently. Images were collected from the internet using an image crawler built in Python with the **DuckDuckGo Search** API and a Python image crawler library. Search queries such as *“bottle on table”*, *“coffee cup”*, and *“mobile phone on desk”* were used to gather images containing the target objects.

This process allowed us to quickly collect many images with different:

* Backgrounds
* Object orientations
* Lighting conditions
* Real-world scenarios

After downloading the images, we manually reviewed them and removed irrelevant or low-quality images to ensure the dataset contained useful training examples.

## Data Annotation

The collected images were uploaded to **Roboflow**, which was used as the annotation platform. Each image was labeled by drawing bounding boxes around the objects and assigning the correct class label.

The three classes used for annotation were:

* Bottle
* Cup
* Phone

Bounding boxes were carefully placed around each object instance so that the model could learn both the **location and appearance** of each object. Roboflow also helped organize the dataset and prepare it for training.

## Initial Model Deployment

After annotation, the dataset was used to train an object detection model through Roboflow’s cloud training pipeline. The trained model was then deployed using Roboflow’s hosted inference API.

This allowed us to test the detector with real-time predictions using a webcam feed. However, since the inference was being performed through an external API server, the system experienced **noticeable latency**. The video stream became slow and sometimes lagged because each frame had to be sent to the remote server for processing.

## Local Model Training

To improve performance, we decided to train and run the model locally on our machine. The annotated dataset was exported and used to train a model using **YOLOv8**, a fast and efficient real-time object detection framework.

Training locally allowed us to:

* Use the dataset directly on our machine
* Generate trained model weights
* Run inference without relying on an external API

Running the model locally significantly improved performance because predictions were computed directly on the computer rather than being sent over the network.

## Real-Time Detection

Once training was completed, the trained model weights were used to perform real-time object detection through the computer’s webcam. Each frame from the webcam was passed through the trained model, and when an object was detected, the system displayed a bounding box and label around the object.

Compared to the cloud-based deployment, local inference provided **much smoother real-time detection** and reduced delays.

## Performance in Real Scenarios

During testing, the model was able to detect bottles, cups, and phones in live video with reasonable accuracy.

### Strengths

* Fast detection when running locally
* Accurate detection when objects are clearly visible
* Real-time performance suitable for simple applications

### Limitations

* Detection accuracy decreases when objects are partially hidden
* Some variations in lighting can affect confidence scores
* Internet-scraped images may include noise or irrelevant examples

These limitations are common when training models with relatively small datasets.

## Reflection and Future Improvements

This project helped us understand the complete pipeline of building an object detection system—from dataset creation to real-time deployment.

Possible improvements include:

* Collecting more images for each object class
* Increasing dataset diversity with different environments
* Applying data augmentation techniques
* Adding more object classes
* Optimizing the model further for edge devices

## Conclusion

This project demonstrates how a custom object detection system can be built using modern deep learning tools. By combining automated image collection, dataset annotation, model training, and real-time inference, we successfully created a working detector capable of identifying **Bottle, Cup, and Phone** objects in real-world scenarios.

The same pipeline can easily be extended to detect additional objects by collecting and annotating more data.
