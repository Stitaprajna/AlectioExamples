# Apple-Sorting using YOLOv5
Source: https://github.com/Okery/YOLOv5-PyTorch

## 1. Download the Dataset
```
Dataset is included, but you download it from: 
https://blog.roboflow.com/top-agriculture-datasets-computer-vision/
```

## Description of the Dataset:
The is a single-class Apple Sorting dataset, in which we have to differentiate good apples from damaged apples.


## 2. Activate virtualenv and install requirements
(Tested in python-3.8)
```
python3.8 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install alectio-sdk
pip install -r requirements.txt
pip install pycocotools
```
If having issues with pycocotools, install these libraries:
```
sudo apt install sox ffmpeg libcairo2 libcairo2-dev libpython3.8-dev
```

## 3. [Optional] Download pretrained weights
Use pretrained weights to speed up training.
```
mkdir log
cd log
wget 'https://github.com/Okery/YOLOv5-PyTorch/releases/download/v0.3/yolov5s_official_2cf45318.pth'
```

## 4. [Optional] Fine-tune on custom dataset
- Update labels.json with your custom labels.
- Split train, test images and place images inside `data/images/train` and `data/images/test`.
- Place train labels inside `data/annotations` in COCO format JSON with filename: `data/annotations/instances_train.json`
- Place test labels inside `data/annotations` in COCO format JSON with filename: `data/annotations/instances_test.json`
- Make sure number of samples are more than you batch size (in config). 

## 5. Start training with Alectio SDK
- Place token inside main.py
- Run `python main.py`

## Misc
- Number of COCO training samples = 253
- Number of COCO test samples = 103
