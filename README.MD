
## 三国志DS Rom静态修改器

### 实现功能：

* 人物属性修改

* 人物登场城市修改

* 人物技能修改

* NPC属性修改

* 剧本相关修改

* 都市相关修改

* 宝物及特产修改

* 游戏内图片的修改

### 使用说明：

* 使用前需安装Python和pywin32，版本要求和下载地址如下：

  * Python >= 3.6 [下载地址](https://www.python.org/downloads/windows/)

  * pywin32 >= 221 [下载地址](https://sourceforge.net/projects/pywin32/files/pywin32/)

* 安装步骤：

  * 首先安装Python，安装过程中需勾选安装pip

  * 安装pywin32，全程下一步

  * 运行cmd打开系统控制台，分别运行


```
    pip install PyQt5
    pip install Pillow
```

  * 部分依赖库会随着pip一同安装，如安装失败，可选用以下地址下载

    * SIP  [下载地址](https://pypi.org/project/sip/)

    * PyQt5  [下载地址](https://pypi.org/project/PyQt5/)

    * Pillow  [下载地址](https://pypi.org/project/Pillow/)

   * 下载时需注意库对应的版本号要与Python版本号匹配

   * 按 SIP >> PyQt5 >> Pillow 的顺序安装

   * 安装方法为在控制台输入

```
    pip install whl文件含后缀名的完整路径
```

### 注意事项：

* 必须使用游戏编号为**4032**的日版rom，中文版不行

* 一般使用繁体输入，少数文字简繁体都无法输入的情况，建议采用日文汉字输入

* 仅在win10下测试，其他系统无法保证可用，XP因最高支持Python3.4，所以肯定不能正常使用

* 图片导入建议预先调整好图片大小为游戏内导出的默认大小

* 将图片保存为256色BMP后再导入可以提升游戏内显示效果

