<h1 align="center">⚠ bili-interactive-spoiler ⚠</h1>
<p align="center">
  <img alt="Version" src="https://img.shields.io/badge/version-0.1.2-blue.svg?cacheSeconds=2592000" />
  <a href="https://twitter.com/Miracle_XYZ">
    <img alt="Twitter: Miracle_XYZ" src="https://img.shields.io/twitter/follow/Miracle_XYZ.svg?style=social" target="_blank" />
  </a>
</p>

> Spoiler for bilibili interactive videos.
> 
> *[SPOILER ALERT] DO NOT ABUSE IT! We are not responsible for the consequences of your abuse.*
> 
> 中文用户请点击[这里](README_CN.md)。

## Install

### Python Requirements

```sh
pip install -r requirements.txt
```

### Graphviz

Make sure you have installed Graphviz on your computer and put it to `PATH`.

## Usage

### config.py

Configure the file `config.py`. Parameters are:

- `aid`: video id
- `graph_version`: graph version
- `fontname`: font name (Now it's Source Han Sans CN. You can change it to any other installed Chinese fonts.)
- `interval`: interval (Break time after node requested, in seconds)
- `output`: output file name (Ends with '.gv')
- `layout`: layout ('horizontal' or 'edge')

Here's how to get `graph_version`:

1. Open the video web page. Press `F12` to toggle Developers Tool, and switch to `Network` tab.
2. Input `nodeinfo` in `Filter` textbox.
3. Press `F5` to refresh the page and wait.
4. When something pops up on the list, right click on the first URL and select `Copy > Copy link address`.
5. Paste the link into a text editor. Find `graph_version=...&` and copy the content represented by `...`. This is exactly what we want: `graph_version` parameter.

### main.py

```sh
python main.py
```

Your output will appear on the current folder. (including `gv` and `pdf`)

## Effect

<details>
  <summary>Click to unfold (SPOILER ALERT)</summary>

  <img src="asset/result.png">
</details>

## Author

👤 **MiracleXYZ**

* Twitter: [@Miracle_XYZ](https://twitter.com/Miracle_XYZ)
* Github: [@MiracleXYZ](https://github.com/MiracleXYZ)

## Show your support

Give a ⭐️ if this project helped you!

***
_This README was generated with ❤️ by [readme-md-generator](https://github.com/kefranabg/readme-md-generator)_