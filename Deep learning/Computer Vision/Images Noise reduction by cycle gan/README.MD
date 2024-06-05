## Implement CycleGAN for converting poor-quality images of Specular/ confocal microscopy into good quality


### Project background:
The critical business problem addressed by this project is the enhancement of low-quality corneal endothelium images obtained from specular and confocal microscopy. These images often suffer from blurring effects or uneven intensity, which hinders automated screening, assessment, and diagnosis. By improving the quality of these images, the project aims to assist eye practitioners in better understanding and analyzing the corneal endothelium layer, potentially leading to more accurate diagnostics and treatment plans.

Dataset: https://github.com/daboe01/SREP-18-33533B
### Preprocessing Steps:
1. **Separating Images**:
   - The dataset includes both good and bad images, with labels provided in an Excel file.
   - Using SQL, the bad images are separated and moved to a different folder.

2. **Cropping Images**:
   - The black boundaries around the images are removed to facilitate better data augmentation.

3. **Image Augmentation**:
   - Data augmentation techniques (e.g., rotation, width shift, height shift, zoom, and horizontal flip) are applied to increase the dataset size.

4. **Loading and Converting Images to Arrays**:
   - Images are loaded and converted to numpy arrays, and then saved in a compressed file format.

### Model Training:
1. **CycleGAN Architecture**:
   - **Discriminator**: Uses InstanceNormalization instead of BatchNormalization.
   - **Generator**: An encoder-decoder model with ResNet blocks, which takes an input image, generates a target image, and reconstructs the original image using skip connections.

2. **Composite Model**:
   - Combines the generator and discriminator models for both directions (A->B and B->A).
   - Uses adversarial and cycle consistency losses for training.

3. **Training Process**:
   - The model is trained over multiple epochs with batches of real and fake samples.
   - Discriminator and generator losses are calculated and updated iteratively.
   - Performance is periodically summarized by generating and saving images.

### Evaluation Steps:
1. **Loading Trained Models**:
   - Pre-trained models are loaded for evaluation.
   
2. **Generating and Plotting Images**:
   - Real, generated, and reconstructed images are selected and plotted to visually assess the quality of the image enhancement.

![CycleGAN Noise Reduction Result](../Deep learning/Computer Vision/Images Noise reduction by cycle gan/Results/atob.JPG)

### Summary:
This project uses CycleGAN to improve low-quality corneal endothelium images by transforming them into high-quality images without requiring paired datasets. The preprocessing includes separating, cropping, and augmenting images. The model training involves a complex CycleGAN architecture with adversarial and cycle consistency losses. Evaluation involves visual assessment of generated and reconstructed images, showing promising results for better understanding and diagnosis of corneal endothelium.
