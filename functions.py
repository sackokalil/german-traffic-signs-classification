import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import os
from tqdm import tqdm
from PIL import Image
import random
import math
import matplotlib.pyplot as plt
import numpy as np
from tqdm import tqdm
from keras.preprocessing.image import load_img

      
            
def load_all_data(df):
    #Number of class to be displayed
    num_classes_to_display = 43

    class_name_count = 5

    # Number of image per class to be displayed
    images_per_class = 1

    # Calculate the number of rows and columns needed
    rows = math.ceil(math.sqrt(num_classes_to_display))
    cols = math.ceil(num_classes_to_display / rows)

    # Adjust the figsize
    plt.figure(figsize=(25, 12))
    
    for i in tqdm(range(num_classes_to_display)):
        temp = df[df['label'] == f"{i:0{class_name_count}}"]['images']
        start = random.randint(0, len(temp))
        files = temp[start: start + images_per_class]
        
        plt.subplot(rows, cols, i + 1)
        
        for index, file in enumerate(files):
            img = load_img(file)
            img = np.array(img)
            plt.imshow(img)
            plt.title(f"{i:0{class_name_count}}")
            plt.axis('off')

    plt.tight_layout()
    
    # Adjust spacement between graphics
    plt.subplots_adjust(hspace=0.2, wspace=0.2)
    
    # Show the plot
    plt.show()
            
            
            
            
            
def plot_graph(history):
    
    acc = history.history['accuracy']
    val_acc = history.history['val_accuracy']
    epochs = range(len(acc))

    plt.plot(epochs, acc, 'b', label='Training Accuracy')
    plt.plot(epochs, val_acc, 'r', label='Validation Accuracy')
    plt.title('Accuracy Graph')
    plt.legend()
    plt.figure()

    loss = history.history['loss']
    val_loss = history.history['val_loss']
    plt.plot(epochs, loss, 'b', label='Training Loss')
    plt.plot(epochs, val_loss, 'r', label='Validation Loss')
    plt.title('Loss Graph')
    plt.legend()
    plt.show()

    




    
    


    
    
    

   