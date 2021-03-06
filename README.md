# 汉字构造表

在尽量保留汉字意符的情况下，为汉字按结构分类，并依其结构（包括复合结构）拆分为基础部件及其变体。目的是用于简化中文字库制作流程。

现版本收录``6763``个汉字（国标一级、二级），依``14``种基础结构拆分为``808``个基础部件

## 基础结构

| 基础结构 | 汉字 | 拆分 |
| --- | :---: | --- |
| 上下 | 艾 | 艹、乂 |
| 上中下 | 害 | 宀、丯、口 |
| 上半包围 | 参 | 弁、彡 |
| 上三包围 | 闭 | 门、才 |
| 下半包围 | 凼 | 凵、水 |
| 左右 | 啊 | 口、阿 |
| 左中右 | 瓣 | 辛、瓜、辛 |
| 左上包围 | 癌 | 疒、喦 |
| 左下包围 | 迸 | 辶、并 |
| 左三包围 | 匪 | 匚、非 |
| 右上包围 | 氨 | 气、安 |
| 右三包围 | 甸 | 勹、田 |
| 全包围 | 囤 | 囗、屯 |
| 单体 | 凹 | |

## 内容说明

``hanzi-jiegou.json`` 构造表的数据结构如下

```json
"表": {
    "format": "上下",
    "components": [
        "毛>丰",
        "衣-亠"
    ],
    "explain": [
        "表：上衣也。从衣从毛。古者衣裘，以毛爲表。",
        "從「衣」，從「毛」，本義為外衣。"
    ]
},
"办": {
    "format": "单体",
    "components": [],
    "explain": [
        "辦：致力也。从力，辡聲。",
        "從「力」，「辡」聲，本義為治理、辦理。"
    ],
    "source": "力"
},
"碧": {
    "format": "上下",
    "components": [
        {
            "format": "左右",
            "components": [
                "玉",
                "白"
            ]
        },
        "石"
    ],
    "explain": [
        "碧：石之青美者。从玉、石，白聲。",
        "從「玉」從「石」，「白」聲。本義是青綠色的玉石。"
    ]
},
```

仅说明特殊内容：

- ``“毛>丰”`` 指明了该字意符部件已经演化为其他含义的部件
- ``“衣-亠”`` 用 "字 - 部件" 表明某个难以用单字表示的部件
- ``“source”`` 仅单体结构汉字可能会拥有此项，指明该字字型源于哪个汉字
- 复合结构如``碧``字内容所示，复合结构主要是为了保留意符，或是应对某些难以解构为单一基础结构的汉字

## 参考资料

《说文解字》

[漢語拆字字典](https://github.com/kfcd/chaizi)、[汉典](https://www.zdic.net/)、[漢語多功能字庫](http://humanum.arts.cuhk.edu.hk/Lexis/lexi-mf//)

## 附言

创建这份文档的起因是我想制作一款中文字库，仅算一级加二级六千多个字，手动创建一个个字型非常令人恼火且把控风格、后期修改十分不便。简单网上搜索了一下，并没找到关于中文字库简化制作相应的方案或工具，或许已经有了但是没有普及。很讶异为何中文字库发展了这么多年，那些初入此门的人依旧只能繁琐的手动制作与管理。

现在，已经有一份解决方案了。即使只是一个雏形，难以使用且存在着令专家血压飙升的错误，但它确实能帮我解决很多问题。然而基于个人需求而诞生的东西在问题被初步解决后，优化改进的动力确实所剩不多了。

我不在乎这份文档被如何使用，若你也希望能改进这份文档，很期待你与我联系。
