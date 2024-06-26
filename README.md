<div align="center">

# Facial Landmarks Detection

<a href="https://pytorch.org/get-started/locally/"><img alt="PyTorch" src="https://img.shields.io/badge/PyTorch-ee4c2c?logo=pytorch&logoColor=white"></a>
<a href="https://pytorchlightning.ai/"><img alt="Lightning" src="https://img.shields.io/badge/-Lightning-792ee5?logo=pytorchlightning&logoColor=white"></a>
<a href="https://hydra.cc/"><img alt="Config: Hydra" src="https://img.shields.io/badge/Config-Hydra-89b8cd"></a>
<a href="https://github.com/ashleve/lightning-hydra-template"><img alt="Template" src="https://img.shields.io/badge/-Lightning--Hydra--Template-017F2F?style=flat&logo=github&labelColor=gray"></a><br>
[![Paper](http://img.shields.io/badge/paper-arxiv.1001.2234-B31B1B.svg)](https://www.nature.com/articles/nature14539)
[![Conference](http://img.shields.io/badge/AnyConference-year-4b44ce.svg)](https://papers.nips.cc/paper/2020)

</div>

## Description

In filter project, we are developing an application that applies filters to human faces in an image. Specifically, we use  ResNet18 for facial landmarks detection, and then apply filters to the faces using Delaunay triangulation and affine transformation.

In this repository, I implement the training process for the ResNet18 model for facial landmarks detection using [the IBUG 300w dataset](https://www.kaggle.com/datasets/toxicloser/ibug-300w-large-face-landmark-dataset). You can refer to the implementation of other parts here.

- [Report on the training process of ResNet18 for facial landmarks detection task](https://api.wandb.ai/links/project_ai/eiifb8yy)

## Installation

### Pip

```bash
# clone project
git clone https://github.com/Le-Bao-181003/Filter.git
cd Filter

# create conda environment
conda create -n myenv python=3.9
conda activate myenv
pip install -r requirements.txt

```

## How to run

Train model with default configuration

```bash
# train on CPU
python src/train.py trainer=cpu

# train on GPU
python src/train.py trainer=gpu

```

You can override any parameter from command line like this

```bash
python src/train.py trainer.max_epochs=20 data.batch_size=64

```

## Results
You can see result in folder deploy/outputs

I have trained the pre-trained ResNet18 model on ImageNet with the IBUG 300w dataset for 20 epochs. 
Model checkpoint in deploy/checkpoints
