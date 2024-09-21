# plot-significance-py<!-- omit in toc -->

<img src="https://img.shields.io/badge/Python-3.9.5 or Later-blue?&logo=Python"> <img src="https://img.shields.io/badge/License-MIT-green">

matplotlibやseabornを用いて作成した棒グラフや箱ひげ図上に、有意差の線とアスタリスクを描画するためのツールです。

このツール内部では統計処理は行いません。
あくまでグラフ上に線と任意のテキストを描画するのみです。
そのため、事前に統計を確認し、有意差があったところに描画を行うようにしてください。

# Table Of Contents <!-- omit in toc -->
<details>
<summary>Details</summary>

- [Environment](#environment)
- [Installation](#installation)
- [Description](#description)
- [Example](#example)
- [References](#references)
- [Troubleshooting](#troubleshooting)
- [Versions](#versions)
- [Author](#author)
- [License](#license)
</details>

# Environment
- Python 3.9.5 or later

# Installation
事前に以下がインストールされている必要があります。
- matplotlib

# Description
具体的な使用方法は `example.py` を確認してください。

一発で綺麗な描画ができることはほぼありません。
以下のパラメータを調整しながら見た目を整えていきます。

```python
def significance(text, data, i, j, column_name, x_txt_offset=0, y_txt_offset=0, x_line_offset_l=0, x_line_offset_r=0, y_line_offset_l=0, y_line_offset_r=0, shrink_l=20, shrink_r=20, line_width=1.5, font_size=20, font_weight='bold', ax=None):
```

| argument | type | description |
| ---- | ---- | ---- |
| text | str | 描画するテキスト (例: *, **, ***) |
| data | pandas.DataFrame | グラフ描画に使用したデータ |
| i, j | int | グラフの横軸のi番目とj番目の間に有意差を描画する |
| column_name | str | グラフの横軸に使用した列名 | 
| x_txt_offset | float | 描画するテキストの横軸方向オフセット |
| y_txt_offset | float | 描画するテキストの縦軸方向オフセット |
| x_line_offset_l | float | 描画する線の 左端 の 横軸 方向オフセット |
| x_line_offset_r | float | 描画する線の 右端 の 横軸 方向オフセット |
| y_line_offset_l | float | 描画する線の 左端 の 縦軸 方向オフセット |
| y_line_offset_r | float | 描画する線の 右端 の 縦軸 方向オフセット |
| shrink_l | int | 描画する線の 左端 の長さのオフセット。値を大きくすると短くなる。 |
| shrink_r | int | 描画する線の 右端 の長さのオフセット。値を大きくすると短くなる。 |
| line_width | float | 線の太さ |
| font_size | int | テキストのフォントサイズ |
| font_weight | str | テキストのフォントタイプ (例: normal, bold) |
| ax | matplotlib.axes._subplots.AxesSubplot | サブプロット用。Axesオブジェクト。任意のオブジェクトに描画する場合。 |

# Example
```python
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

import graph_annotator

# read sample data
df = pd.read_csv('sample_data.csv')

# box plot
plt.figure()
sns.boxplot(x='condition', y='score', data=df)

# set y-axis limit
plt.ylim(0, 14)

# draw line and text of significant difference
graph_annotator.significance('**', df, 0, 1, column_name='condition')
graph_annotator.significance('***', df, 2, 3, column_name='condition')

plt.show()
```

![example](https://github.com/user-attachments/assets/1513c214-0972-4135-8f8d-6c408da8f404)



# References

# Troubleshooting

# Versions
- 1.0.0: 2024/9/18

# Author
- Takayoshi Hagiwara
    - Graduate School of Media Design, Keio University
    - Toyohashi University of Technology


# License
- MIT License