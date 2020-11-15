# Markdown to HTML by Python

Markdown → HTML変換をPythonで行う試み。  
Pythonのmarkdownを使うとHTMLが生成されるが、CSSがTyporaのCSSを使えばいい感じにならないか？

## 結果

[実際にやってみた](./app/converted.html)  
[Typoraで同じMarkdownを変換した](./byTypora/SampleText.html)  

ちょっと違うんだよな…  
- 生成結果として出力されるHTMLタグが違う？  
- CSS足りてない？
- ツール探したほうがいい気がする…


## 実行

```
docker-compose build
docker-compose up
```

下記に出力される。
```
./app/converted.html
```

## 参考

- (https://qiita.com/masakuni-ito/items/593b9d753c44da61937b)
- (https://note.nkmk.me/python-file-io-open-with/)
  - ファイル読み書き
