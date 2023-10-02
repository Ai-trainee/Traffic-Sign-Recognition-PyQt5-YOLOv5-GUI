<h1 align="center">Road Sign Recognition Project Based on YOLOv5 (YOLOv5 GUI)</h1>

<p align="center">
  <a href="README.md">English</a> |
  <a href="data/doc/README_cn.md">简体中文</a>
</p>

<p align="center">
  <a href="data/doc/README_Parameter adjustment.md">训练策略</a>
</p>


This is a road sign recognition project based on YOLOv5, developed with a PyQt5 interface, YOLOv5 trained model, and MySQL database. The project consists of five modules: parameter initialization, sign recognition, database, data analysis, and image processing(Please refer to the Chinese document for details).

## Screenshots

* ### Sign Recognition Module
  ![img.png](data/doc/img.png)
* ### Image Processing and Data Augmentation Module
  ![img_1.png](data/doc/img_1.png)
* ### Parameter Initialization Module
  ![img_2.png](data/doc/img_2.png)
* ### Database Module
  ![img_3.png](data/doc/img_3.png)
* ### Data Analysis Module
  ![img_4.png](data/doc/img_4.png)
* ### Login Interface
  ![img_5.png](data/doc/img_5.png)

### Video Demo

[Road Sign Recognition System Based on YOLOV5](https://www.bilibili.com/video/BV1Ck4y1Y7Bk/?spm_id_from=333.999.0.0&vd_source=40d9cda43378fbc89cd5184e09bf1272)

## Getting Started

Run `main.py`.

### Account and Password

- admin 123456
- 1 2
- Modify the main function to enter directly

## Project Modules

- `pt` folder: Contains the model(best.pt is Road Sign Recognition model)
- `main_with` folder: `login.py` (login UI), `win.py` (main UI)
- `dialog` folder: RTSP pop-up interface
- `apprcc_rc.py`: Resource file
- `login_ji.py`: Interface login logic file
- `run/run-exp52`: Road sign recognition model trained for 300 epochs
- `utils/tt100k_to_voc-main` folder: JSON to YOLO format converter
-  `result`Save some reasoning files，`run`Save training file
- Dataset: [TT100k : Traffic-Sign Detection and Classification in the Wild](https://cg.cs.tsinghua.edu.cn/traffic-sign/)
- Database files: in the `data` folder `-regn_mysql.sql`

### Install Dependencies

pip install -r requirements.txt

### Attention
1. The project is based on YOLOv5 v6.1
2. Database connection
```python
def get_db_connection():
    return pymysql.connect(
        host='localhost',
        user='root',
        password='123456',
        database='traffic_sign_recognition'
    )
```
There are two identical database links in the code that need to be modified, please check the database sql file under the data folder to establish the test database

## Acknowledgements

- [Converting the TT100K dataset to VOC format and selecting more than 100 images and XMLs for each of the 45 categories using a Python script](https://blog.csdn.net/Hankerchen/article/details/120727299?spm=1001.2014.3001.5502)
- https://github.com/Javacr/PyQt5-YOLOv5
## Star History

[![Star History Chart](https://api.star-history.com/svg?repos=Ai-trainee/Traffic-Sign-Recognition-PyQt5-YOLOv5-GUI&type=Date)](https://star-history.com/#Ai-trainee/Traffic-Sign-Recognition-PyQt5-YOLOv5-GUI&Date)
