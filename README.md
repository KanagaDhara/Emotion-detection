# Emotion-detection
**Emotion Detection Project**

Emotion detection, also known as facial emotion recognition, is an intriguing field within artificial intelligence and computer vision. It involves identifying and interpreting human emotions from facial expressions¹. This project aims to classify the emotion on a person's face into one of seven categories: angry, disgusted, fearful, happy, neutral, sad, and surprised³.

The project uses Convolutional Neural Networks (CNNs), a type of deep learning neural network architecture specifically designed for processing grid-like data, such as images and videos¹. CNNs have revolutionized the field of computer vision and are widely used for various tasks, including image classification, object detection, facial recognition, and image generation¹.

The model is trained on the FER-2013 dataset, which consists of 35887 grayscale, 48x48 sized face images with seven emotions³. The architecture of a typical CNN for this task includes several layers:

1. **Input Layer**: Receives the raw image data. Images are typically represented as grids of pixels with three color channels (red, green, and blue – RGB)¹.
2. **Convolutional Layers**: Consist of multiple filters (also called kernels). Each filter scans over the input image using a sliding window¹.
3. **Pooling Layers**: Reduce the spatial dimensions of feature maps while retaining important information¹.
4. **Flatten Layer**: Reshapes the output of the previous layers into a 1D vector, allowing it to be input to a dense layer¹.
5. **Fully Connected Layers**: After several convolutional and pooling layers, CNNs typically have one or more fully connected layers (also called dense layers)¹.

**Applications**
Accurate emotion detection has numerous practical applications, including human-computer interaction, customer feedback analysis, and mental health monitoring¹.
