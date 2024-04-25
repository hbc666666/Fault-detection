import warnings
warnings.filterwarnings('ignore')
from ultralytics import YOLO

if __name__ == '__main__':
    '''model = YOLO('E:\pycharm\PyCharm Community Edition 2023.2.1\pythonProject\yolov8-main/runs\detect/train2\weights/best.pt')
    model.val(data='dataset/data.yaml',
              split='val',
              batch=16,
            #   save_json=True, # if you need to cal coco metrice
              project='runs/val',
              name='exp',
              )'''

    #model = YOLO("E:\pycharm\PyCharm Community Edition 2023.2.1\pythonProject/ultralytics-main/runs\detect/train27\weights/best.pt")
    model = YOLO("E:\pycharm\PyCharmCommunityEdition2023.2.1\pythonProject\yolov8-main/runs\detect/train13\weights/best.pt")  # 加载预训练模型（推荐用于训练）
    results = model.val(data="E:\pycharm\PyCharmCommunityEdition2023.2.1\pythonProject/ultralytics-main/ultralytics\cfg\datasets/transmission.yaml")  # 训练模型
    #results = model.val(data="E:\pycharm\PyCharmCommunityEdition2023.2.1\pythonProject/ultralytics-main/ultralytics\cfg\datasets/plane.yaml")