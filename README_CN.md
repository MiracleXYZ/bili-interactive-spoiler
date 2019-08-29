<h1 align="center">⚠ bili-interactive-spoiler ⚠</h1>
<p align="center">
  <img alt="Version" src="https://img.shields.io/badge/version-0.2.0-blue.svg?cacheSeconds=2592000" />
  <a href="https://twitter.com/Miracle_XYZ">
    <img alt="Twitter: Miracle_XYZ" src="https://img.shields.io/twitter/follow/Miracle_XYZ.svg?style=social" target="_blank" />
  </a>
</p>

> 哔哩哔哩互动视频剧透工具
> 
> **[剧透警告] 不要滥用！滥用行为造成的后果我们概不负责。**
> 
> Click [here](README.md) for English version.

## 安装

### Python库

```sh
pip install -r requirements.txt
```

### Graphviz

确保你的电脑上安装了 Graphviz 并放在了你的 `PATH` 环境变量下。

## 使用

### config.py

按照实际情况修改 `config.py` ，参数说明如下：

- `aid`: 视频av号
- `fontname`: 字体名称（这里是「思源黑体」，可以改为其他的中文字体名称）
- `interval`: 时间间隔（每访问一个节点后的休息时间，以秒为单位）
- `output`: 输出文件名（以'.gv'结尾）
- `output_format`：输出文件格式（支持pdf/png/svg）
- `layout`: 布局：'horizontal'（横向）, 'edge'（纵向，选项在边上表示）

### main.py

```sh
python main.py
```

执行完毕后，生成的结果将会出现在同一文件夹下。（包括 `gv` 文件和最终输出的文件）


## 效果

<details>
  <summary>点击查看效果（剧透慎点）</summary>

  <img src="asset/result.png">
</details>


## 作者

👤 **MiracleXYZ**

* Twitter: [@Miracle_XYZ](https://twitter.com/Miracle_XYZ)
* Github: [@MiracleXYZ](https://github.com/MiracleXYZ)

## 支持

觉得好用就赏个⭐️吧~

***
_This README was generated with ❤️ by [readme-md-generator](https://github.com/kefranabg/readme-md-generator)_