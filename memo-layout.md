# レイアウトの方向を変更
レイアウトはデフォルトでは「orientation」に「horizontal」が設定されているので横方向にボックスが追加されていく。  
ボックスを縦に設定したい場合は、「vertical」に設定する。  
設定するときは、必ず`BoxLayoutの一番上に記述`する。
```
BoxLayout:
    orientation: 'vertical'
```
# サイズを変更
サイズの調整には、「size_hint」を使用します。  
size_intは「0.01から1」の間のパーセンテージ。  
```
BoxLayout:
    size_hint: 0.8, 0.8
```
size_hintが設定されていない時には、`デフォルトでNone`が設定されている。

# 配置を変更
配置場所を指定したい時には、「pos_hint」を使用する。
```
BoxLayout:
    pos_hint: {'x':0.5, 'y': 0.5}
```
pos_hintが設定されていない時には、`デフォルトでNone`が設定されている。