# Handwriting
According to statistics, 60% of handwritten notes at meetings later transcribe notes on the computer. 
That's why we decided to create a handwriting recognition application. 
You will need this system to convert your handwriting to text. The system will be implemented as a web application.

## Train model on IAM dataset
### Prepare dataset
Follow these instructions to get the IAM dataset:
* Register for free at this [website](https://fki.tic.heia-fr.ch/databases/iam-handwriting-database)
* Download words/words.tgz
* Download ascii/words.txt
* Create a directory for the dataset on your disk, and create two subdirectories: img and gt
* Put words.txt into the gt directory
* Put the content (directories a01, a02, ...) of words.tgz into the img directory
### Run training
* Delete files from model directory if you want to train from scratch
* Go to the src directory and execute python main.py --mode train --data_dir path/to/IAM
* The IAM dataset is split into 95% training data and 5% validation data
* If the option --line_mode is specified, the model is trained on text line images created by combining multiple word images into one
* Training stops after a fixed number of epochs without improvement

Command :
```
$ python main.py --mode train --fast --data_dir path/to/iam  --batch_size 500 --early_stopping 15
```
And the line model with:

```
$ python main.py --mode train --fast --data_dir path/to/iam  --batch_size 250 --early_stopping 10
```
