#  handwriting-digit-identify

本仓库为 基于机器学习的手写数字识别系统 涉及的机器学习算法为 K-means

详细调试文档以及展示见 [本文档](/doc/Summary.md)

## 环境部署及运行

本仓库依赖的库为 `flask_cors` , `opencv-python` , `scikit-learn`

实际展示用到的源代码存储在 `identify` 文件中, 你可以直接点击 `click.bat` 文件来安装依赖并且运行代码

> `click.bat` 使用 `pip` 来安装依赖

`click.bat` 成功运行后会显示如下提示 : 
```
.....
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:55555
Press CTRL+C to quit
```
之后点击 `identify` 文件夹中的 `classify.html` 文件即可

> **注意: 由于 Github 对文件大小的限制, 训练好的模型无法直接上传**
>
> 模型的下载链接为 : [下载链接]()
>
> 模型下载好后请放置在 `/identify/py` 目录下, 模型名字命名为 `K-means`

## 基本代码框架
我们仅展示和实际功能相关的部分

```
handwriting-digit-identify
├─ identify             # 演示文件夹, 展示所需源代码
│  ├─ classify.html     # 主 HTML 文件
│  ├─ css
│  ├─ html
│  ├─ js
│  └─ py                # 后端代码存放
│     ├─ Centre.py      # 后端依赖函数
│     ├─ K-means        # 机器学习模型(需自行训练或下载放入)
│     └─ Net.py         # 后端入口文件
├─ README.md
├─ 手写数字数据集.zip   # 训练模型的训练集
└─ 训练+获取数据代码
   ├─ Classify.py       # 测试不同机器学习的分类效率
   ├─ DataPre.py        # 预处理数据
   ├─ TestPerformance.py    # 测试模型识别准确度
   └─ ToVictor.py       # 向量化数据

```

## HTML 使用说明

主页面

![image-20230527120449615](https://gitee.com/qq3109778990/remem_pic/raw/master/img/image-20230527120449615.png)



之后回进入操作页面，将鼠标移动到第一张图片会出现两个选项

<img src="https://gitee.com/qq3109778990/remem_pic/raw/master/img/image-20230527120559679.png" alt="image-20230527120559679" style="zoom:80%;" />



选择好图片一定要**点击开始生成**后才能**点击查看报告**，否则查看报告为空

当从查看报告页面返回后，此次查看的内容将会被**清空**

<img src="https://gitee.com/qq3109778990/remem_pic/raw/master/img/image-20230527120902701.png" alt="image-20230527120902701" style="zoom:80%;" />