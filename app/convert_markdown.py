import markdown

headOpen = '''
<!DOCTYPE html>
<html>
<head>
<style>
'''

typoraWhiteStyle = ''
with open('./typora_white_style.css', 'r') as readCSS :
    typoraWhiteStyle = readCSS.read();

headClose = '''
</style>
</head>
'''

bodyOpen = '''
<body>
'''

sample_text = '''
# h1の文字が出てくると嬉しい

---

## h2の文字はでてくるだろう

* リスト1
* リスト2
* リスト3

> 引用してくれ

本文で **太字にもなるし**、*斜体にもなるはず* 。

```
まさかコードも入れられるんですか？
if (!lie) {
    return true;
}
```

| header1 | header2 | header3 |
|:-----------|------------:|:------------:|
| 左寄せ | 右寄せ | 中央寄せ |

すごい！
'''

bodyClose = '''
</body>
</html>
'''


md = markdown.Markdown(extensions=['tables','toc'])

outputPath = './converted.html'
with open(outputPath , 'w') as writer:
    writer.write(headOpen)
    writer.write(typoraWhiteStyle)
    writer.write(headClose)
    writer.write(bodyOpen)
    writer.write(md.convert(sample_text))
    writer.write(bodyClose)