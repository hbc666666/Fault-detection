import warnings
warnings.filterwarnings('ignore')
from ultralytics import YOLO

if __name__ == '__main__':
    model = YOLO('E:\pycharm\PyCharmCommunityEdition2023.2.1\pythonProject\yolov8-main/runs\detect/train6\weights/best.pt') # select your model.pt path
    model.predict(source='E:\pycharm\PyCharmCommunityEdition2023.2.1\pythonProject\datasets\VOCjyz\images/val',
                project='runs/predict',
                name='exp',
                save=True,
                # visualize=True # visualize model features maps
                )