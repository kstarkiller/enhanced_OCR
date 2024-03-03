# b13_enhanced_OCR

## Description

This project is about enhancing Optical Character Recognition (OCR) using machine learning. The main script is `website_recognition.ipynb` which uses a trained model to predict digits from photos taken and drawings both from the website specially built for this project.

## Usage
### Create a conda environnement
Once you retrieved this porject, execute the following command:

```bash
conda create --name <env> --file requirements.txt
```
where `<env>` is the name you choose for this new environnement

### Train model
You first need to locally run notebooks/number_recognition.ipynb which will train, validate and test a Sequential model with MNIST dataset.
This model will then be saved as a keras model in `models/number_recon_model.keras`

```bash
jupyterlab notebooks/number_recognition.ipynb
```

### Take your own photos
Thanks to [Loke-60000's](https://github.com/Loke-60000) and [fdeage's](https://github.com/fdeage) website including in this project, you can take photos of handwritted numbers.
To do so :

```bash
cd website
python -m http.server 8001
```

Your photos and drawings will be saved in your downloads' folder.
You need to copy them into `this_project/data/webcam` for the photos and `this_project/data/drawings` for the drawings.
Each file must be renamed with its own value (if several files have the same value, add underscores ("_") after the value). This will serve to display the actual value of the number and calculate the accuracy of the prediction.

### Make predictions
Run `website_recognition.ipynb` to load your images, process them and use `number_recon_model.keras` to predict what number you draw.

```bash
jupyterlab website_recognition.ipynb
```
