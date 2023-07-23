# Student grade predictor
The purpose of this project was to predict the final mark of a student given some information about him and his mark in first and second period and also to provide a gui to easily enter the data of the to be predicted student.

### How to use
1. Run [train-model](/train-model.py) file to train the model and save the  weights of the model in the [saved](/saved.npz) file
2. Run [gui](/gui.py) file and enter the data of the student then click predict mark

### Key
- School: 0 == Gabriel Pereira or 1 == Mousinho da Silveira
- Age
- Address: 0 == Urban or Rural
- Family Size: 0 == Less than 3 or 1 == More than 3
- Parental status: 0 == Apart or 1 == Together

The rest of the data is explained in the student.txt file provided with the dataset, with the irrelevent data marked with #.