<h1 align="center">基于YOLOv5的道路标志识别项目（yolov5界面GUI）</h1>
<p align="center">
  <a href="../../README.md">English</a> |
  <a href="README_cn.md">简体中文</a>
</p>


这是一个关于yolov5的道路标志识别项目，使用Pyqt5开发界面，Yolov5训练模型，数据库Mysql，包含五个模块：初始化参数、标志识别、数据库、数据分析和图像处理。

## 软件截图

* ### 标志识别模块
  ![img.png](img.png)
 左下角三个勾选框分别是结果保存、启动数据库录入、以及模型可视化分析
  
  
* ### 图像处理与数据增强模块
  ![img_1.png](img_1.png)
  右侧栏是自定义参数的批量图像数据增强（按一定概率对一个文件夹所有图片使用勾选的数据增加方法）
* ### 初始化参数模块
  ![img_2.png](img_2.png)
  模型基本参数勾选配置

* ### 数据库模块
  ![img_3.png](img_3.png)
  
 
* ### 数据分析模块
  ![img_4.png](img_4.png)
* ### 登录界面
  ![img_5.png](img_5.png)

### 演示视频

[基于YOLOV5的道路标志识别系统](https://www.bilibili.com/video/BV1Ck4y1Y7Bk/?spm_id_from=333.999.0.0&vd_source=40d9cda43378fbc89cd5184e09bf1272)


### 安装依赖

pip install -r requirements.txt

---
## **快速开始**

### 1. **设置数据库**

为了运行应用程序，您需要设置您的 MySQL 数据库。按照以下步骤准备您的数据库：

- **自动数据库创建（可选）**：
    - 如果您喜欢自动设置，我们提供了一个批处理脚本。运行 **`setup_database.bat`** 脚本来创建数据库。这需要在您的系统上安装并配置 MySQL。
- **手动数据库创建**：
    - 或者，您可以在 MySQL 中手动创建数据库。在您的 MySQL 环境中导入并执行 **`data/regn_mysql.sql`** 文件，以设置必要的数据库和表。

### 2. **在代码中配置数据库连接**

设置数据库之后，请更新代码中的连接设置，请更改成你本地数据库的身份验证信息（这4个变量在代码的开头 , 大约在59行，具体如下）；附：这些身份验证信息在代码中被两次调用(大约第111行和第1783行)

```python
# 数据库连接设置作为全局变量
DB_HOST = 'localhost'    # 数据库主机
DB_USER = 'root'         # 数据库用户
DB_PASSWORD = '1234'     # 数据库密码
DB_NAME = 'traffic_sign_recognition'  # 数据库名
```

### **关于数据库链接的注意事项**

如果遇到 **`RuntimeError: 'cryptography' package is required for sha256_password or caching_sha2_password auth methods`** 错误，这是因为数据库身份验证出错了，需要正确地创建数据库并输入密码。
并且如果你本地没有启动mysql服务，也会报这个错，所以请确保你的mysql服务已经启动。
### 3. 运行 `main.py`。

### 4. 输入您的账号和密码以登录。

以下是默认的登录凭据：

| 用户名   | 密码     |
|----------|----------|
| admin    | 123456   |
| 1        | 2        |

或者修改`main.py`中的主函数：删除登陆逻辑，以直接进入系统而无需进行身份验证。

---

## 项目模块

- `pt`文件夹：存放模型(best.pt是道路标志识别模型)
- `main_with`文件夹：`login.py`(登陆ui)、`win.py`(主ui)
- `dialog`文件夹：rtsp弹出界面
- `apprcc_rc.py`：资源文件
- `login_ji.py`：界面登陆逻辑文件
- `data/run/run-exp52`：300轮训练后的道路标志识别模型
- `utils/tt100k_to_voc-main`文件夹：json转yolo格式
- `result`保存一些推理文件，`run`保存训练文件
- 数据集：[TT100k : Traffic-Sign Detection and Classification in the Wild](https://cg.cs.tsinghua.edu.cn/traffic-sign/)
- 数据库文件：`data`文件夹下`-regn_mysql.sql`


> 由于这个项目是在我学习YOLOv5时完成的（已经过了很长一段时间），因此主要的逻辑代码都集中在main.py文件中。换句话说，我没有将不同功能模块化，没有进行模块结构的清晰划分。虽然现在我想给它划分一下模块结构，但是我还是太懒了，嘻嘻 :smile:。如果您有兴趣，可以将其模块化，这样它就会更加清晰。



## 致谢

- [将TT100K数据集转成VOC格式，并且用Python脚本选出45类超过100张的图片和XML](https://blog.csdn.net/Hankerchen/article/details/120727299?spm=1001.2014.3001.5502)
- https://github.com/Javacr/PyQt5-YOLOv5
## Star History

[![Star History Chart](https://api.star-history.com/svg?repos=Ai-trainee/Traffic-Sign-Recognition-PyQt5-YOLOv5-GUI&type=Date)](https://star-history.com/#Ai-trainee/Traffic-Sign-Recognition-PyQt5-YOLOv5-GUI&Date)
