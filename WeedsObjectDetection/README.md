# Object Detection using YOLOv5
Source: https://github.com/Okery/YOLOv5-PyTorch

## 1. Download COCO Dataset
```
./download_coco.sh
```

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
If having isses with pycocotools, install these libraries:
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

## 4. Start training with Alectio SDK
- Place token inside main.py
- Run `python main.py`

## Misc
- Number of training samples = 118287
- Number of test samples = 40670