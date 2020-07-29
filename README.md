# Flower Identification Project  
It is spring time during the Covid-19 pandameic.  The flowers are in bloom, but the time I spend outdoors is legally limited. To provide an alternate avenue into flower gazing, I will train a computer to descriminate between types of flowers.  

---  

1. Data
- [original source: Kaggle](https://www.kaggle.com/alxmamaev/flowers-recognition/data)
- [raw_data_in_repo](./data/flowers)
- [tts_data](./data/split)

In order to create the train test split of the images, run the 

2. Models
- [FSM](./models/fsm.ipynb): a simple convolutional neural net with a Convolutional2D layer, a MaxPooling layer, one dense layer and a softmax output. 
- [SSM](./models/ssm.py): added one extra dense layer to the fsm, which reulted in a validation accuracy of .4422 after 10 epochs.



  
