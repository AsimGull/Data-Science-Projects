# T-shirts-and-dress-shirts-Images-MachineLearnign-CLassification-from-Fashion-MNIST-

#### Develop a machine learning model that can classify between images of T-shirts and dress-shirts.
You are given the following files:
1. TrainData.csv: It contains 12000 training examples. Each row contains 784 values. The dataset has been derived from Fashion-MNIST dataset. Each example is a flattened 28x28 pixel gray-scale image. You can reshape the examples to visualize what each image looks like.
2. TrainLabels.csv: This file contains true labels for the examples in TrainExamples.csv
3. TestData.csv: This file contains test examples.
### You can load train and test data using the following code: 
1. Xtr=np.loadtxt("TrainData.csv")
2. Ytr=np.loadtxt("TrainLabels.csv")
3. Xts=np.loadtxt("TestData.csv")
### To visualize
1. import matplotlib.pyplot as plt 
2. plt.imshow(Xtr[10].reshape([28,28]))
