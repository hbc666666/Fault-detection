import warnings
warnings.filterwarnings('ignore')
from ultralytics import YOLO

if __name__ == '__main__':
    '''model = YOLO('ultralytics/cfg/models/v8/yolov8n.yaml')
    model.load('yolov8n.pt') # loading pretrain weights
    model.train(data='dataset/data.yaml',
                cache=False,
                imgsz=640,
                epochs=100,
                batch=16,
                close_mosaic=10,
                workers=4,
                device='0',
                optimizer='SGD', # using SGD
                # resume='', # last.pt path
                # amp=False # close amp
                # fraction=0.2,
                project='runs/train',
                name='exp',
                )'''

    # 加载模型
    model = YOLO("ultralytics/cfg/models/v8/yolov8s-EMA.yaml")  # 从头开始构建新模型
    #model.load('E:\pycharm\PyCharmCommunityEdition2023.2.1\pythonProject\yolov8-main/runs\detect/train25\weights/best.pt')
    #model.load('E:\pycharm\PyCharmCommunityEdition2023.2.1\pythonProject/ultralytics-main/runs\detect/train27\weights/best.pt')

    # Use the model
    #results = model.train(data="E:\pycharm\PyCharmCommunityEdition2023.2.1\pythonProject/ultralytics-main/ultralytics\cfg\datasets\cocoshaixuan.yaml",epochs=200, batch=16)  # 训练模型
    results = model.train(data="E:\pycharm\PyCharmCommunityEdition2023.2.1\pythonProject/ultralytics-main/ultralytics\cfg\datasets/transmission.yaml", epochs=200, batch=16)  # 训练模型
    #results = model.train(data="E:\pycharm\PyCharmCommunityEdition2023.2.1\pythonProject/ultralytics-main/ultralytics\cfg\datasets\plane.yaml",epochs=100, batch=8)  # 训练模型