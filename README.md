<h1 align="center">Road Sign Recognition Project Based on YOLOv5 (YOLOv5 GUI)</h1>

<p align="center">
  <a href="README.md">English</a> |
  <a href="data/doc/README_cn.md">简体中文</a>
</p>

<p align="center">
  <a href="data/doc/README_Parameter adjustment.md">训练策略</a>
</p>


This is a road sign recognition project based on YOLOv5, developed with a PyQt5 interface, YOLOv5 trained model, and MySQL database. The project consists of five modules: parameter initialization, sign recognition, database, data analysis, and image processing(Please refer to the Chinese document for details),This project uses YOLOv5 v6.1.
  ![00013.jpg](data/doc/00013.jpg)
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


<div align="center">
    <img src="data/doc/img.png" alt="图片1" width="30%" style="max-width: 300px;">
    <img src="data/doc/img_1.png" alt="图片1" width="30%" style="max-width: 300px;">
    <img src="data/doc/img_2.png" alt="图片2" width="30%" style="max-width: 300px;">
    <img src="data/doc/img_3.png" alt="图片3" width="30%" style="max-width: 300px;">
    <img src="data/doc/img_3.png" alt="图片1" width="30%" style="max-width: 300px;">
    <img src="data/doc/img_4.png" alt="图片2" width="30%" style="max-width: 300px;">
</div>

</div>

### Video Demo

[Road Sign Recognition System Based on YOLOV5](https://www.bilibili.com/video/BV1Ck4y1Y7Bk/?spm_id_from=333.999.0.0&vd_source=40d9cda43378fbc89cd5184e09bf1272)

### Install Dependencies

To install the required dependencies, run:

```bash
pip install -r requirements.txt
```

## Quick Start
1. Set the local database link otherwise an error will be reported：report an error：RuntimeError: 'cryptography' package is required for sha256_password or caching_sha2_password auth methods
For database connections, you need to set up your MySQL database as per the configurations below:
```python
def get_db_connection():
    return pymysql.connect(
        host='localhost',
        user='root',
        password='123456',
        database='traffic_sign_recognition'
    )
```
There are two identical database links in the code (around line 111 and line 1783) that need to be modified, check the database sql file in the data folder to set up a test database to continue running the program

2. Run `main.py`.

3. Enter your account and password to log in

Here are the default login credentials:

| Username | Password |
|----------|----------|
| admin    | 123456   |
| 1        | 2        |

Modify the main function in `main.py` to enter the system directly without authentication.

## Project Structure

- `pt` folder: Contains the YOLOv5 model file `best.pt` for road sign recognition.
- `main_with` folder: Contains `login.py` for the login UI and `win.py` for the main UI.
- `dialog` folder: Contains the RTSP pop-up interface.
- `apprcc_rc.py`: The resource file for the project.
- `login_ji.py`: Implements the login logic for the UI.
- `run/run-exp52`: The YOLOv5 road sign recognition model trained for 300 epochs.
- `utils/tt100k_to_voc-main` folder: Tool for converting JSON annotations to YOLO format.
- `result`: Folder to save inference results.
- `run`: Folder to save training logs and outputs.
- Dataset: Download from [TT100k : Traffic-Sign Detection and Classification in the Wild](https://cg.cs.tsinghua.edu.cn/traffic-sign/).
- Database files: Located in the `data` folder, see `-regn_mysql.sql` for setup.



## Acknowledgements

- For converting the TT100K dataset to VOC format and selecting more than 100 images and XMLs for each category, see this [CSDN blog post](https://blog.csdn.net/Hankerchen/article/details/120727299?spm=1001.2014.3001.5502).
- The PyQt5-YOLOv5 integration was inspired by this [GitHub repository](https://github.com/Javacr/PyQt5-YOLOv5).

## Star History

Track the GitHub star history of this project:

![Star History Chart](https://api.star-history.com/svg?repos=Ai-trainee/Traffic-Sign-Recognition-PyQt5-YOLOv5-GUI&type=Date)

