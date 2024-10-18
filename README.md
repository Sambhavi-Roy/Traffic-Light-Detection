
RESULTS ON 2nd DATASET OF TRAFFIC LIGHT IMAGES


Fusing layers...
Model summary: 157 layers, 7018216 parameters, 0 gradients, 15.8 GFLOPs
test: Scanning C:\Users\Sambhavi Roy\Downloads\Traffic object train.v1i.yolov5pytorch\test\labels... 75 images, 0 backg
test: New cache created: C:\Users\Sambhavi Roy\Downloads\Traffic object train.v1i.yolov5pytorch\test\labels.cache
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100%|██████████| 3/3 [00:05<0
                   all         75        100      0.931      0.914      0.951      0.551
                 green         75         43      0.958      0.884      0.953      0.542
                   red         75         50      0.985          1      0.995      0.612
                yellow         75          7      0.851      0.857      0.904      0.499
Speed: 2.6ms pre-process, 16.4ms inference, 8.8ms NMS per image at shape (32, 3, 640, 640)
Results saved to runs\val\exp3
