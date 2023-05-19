<h1 align="center">Road Sign Recognition Project Based on YOLOv5 (YOLOv5 GUI)</h1>

<p align="center">
  <a href="README.md">English</a> |
  <a href="README_cn.md">简体中文</a>
</p>

<p align="center">
  <a href="README_Parameter adjustment.md">训练策略</a>
</p>


This is a road sign recognition project based on YOLOv5, developed with a PyQt5 interface, YOLOv5 trained model, and MySQL database. The project consists of five modules: parameter initialization, sign recognition, database, data analysis, and image processing(Please refer to the Chinese document for details).

## Screenshots

* ### Sign Recognition Module
  ![img.png](img.png)
* ### Image Processing and Data Augmentation Module
  ![img_1.png](img_1.png)
* ### Parameter Initialization Module
  ![img_2.png](img_2.png)
* ### Database Module
  ![img_3.png](img_3.png)
* ### Data Analysis Module
  ![img_4.png](img_4.png)
* ### Login Interface
  ![img_5.png](img_5.png)

### Video

[Road Sign Recognition System Based on YOLOV5](https://www.bilibili.com/video/BV1Ck4y1Y7Bk/?spm_id_from=333.999.0.0&vd_source=40d9cda43378fbc89cd5184e09bf1272)

## Getting Started

Run `main.py`.

### Account and Password

- admin 123456
- 1 2
- Modify the main function to enter directly

## Project Modules

- `pt` folder: Contains the model
- `main_with` folder: `login.py` (login UI), `win.py` (main UI)
- `dialog` folder: RTSP pop-up interface
- `apprcc_rc.py`: Resource file
- `login_ji.py`: Interface login logic file
- `run-exp52`: Road sign recognition model trained for 300 epochs
- `tt100k_to_voc-main` folder: JSON to YOLO format converter
- Dataset: [TT100k : Traffic-Sign Detection and Classification in the Wild](https://cg.cs.tsinghua.edu.cn/traffic-sign/)

### Install Dependencies

pip install -r requirements.txt

## Acknowledgements

- [Converting the TT100K dataset to VOC format and selecting more than 100 images and XMLs for each of the 45 categories using a Python script](https://blog.csdn.net/Hankerchen/article/details/120727299?spm=1001.2014.3001.5502)
- https://github.com/Javacr/PyQt5-YOLOv5
