# Decorator
* オブジェクトにどんどんデコレーション(飾り付け)を施していく

## 何故Decoratorを使うか

## Decoratorパターンの登場人物
* Componentの役
    * 機能を追加する時の核になる役
        * スポンジケーキのインタフェース(API)だけを定める
    * Displayクラスがこの役
* ConcreteComponentの役
    * Component役のAPIを実装している具体的なスポンジケーキ
    * StringDisplayクラスがこの役
* Decorator(装飾者)の役
    * Component役と同じAPIを持つ
    * さらに，このDecorator役が飾る対象となるComponent役を持つ
    * Borderクラスがこの役
* ConcreteDecorator(具体的な装飾者)の役
    * 具体的なDecoratorの役
    * SideBorderクラスとFullBorderクラスがこの役


## あなたの考えを広げるためのヒント
### 透過的なインタフェース(API)
* Decoratorパターンでは飾り枠と中身を同一視する
* そのため，飾り枠を使って中身を包んでもAPIは少しも隠されない
* これをインタフェースが透過的であるという
* DecoratorパターンはCompositeパターンと異なり，外枠を重ねることで機能を追加していく

### 中身を変えずに機能追加ができる
* 包まれる方を変更すること無く，機能の追加を行なうことができる

### 動的な機能追加ができる
* Decoratorパターンで使われている委譲はクラス間をゆるやかに結合している
* なので，フレームワークのソースを変更すること無く，オブジェクトの関係を変えた新しいオブジェクトを作ることができる

### 単純な品揃えでも，多様な機能追加ができる
* ConcreteDecorator役を沢山用意しておけば，それらを自由に組み合わせて新しいオブジェクトを作ることができるから
* Decoratorパターンは，アイスクリームのフレーバーを組み合わせるように，多様な要求に応えるのに向いている

### java.ioパッケージとDecoratorパターン
* LineNumberReader(BufferReader(FileReader("datafile.txt")))
* として，行番号を管理できる

### 小さいクラスがが増えてしまう
* Decoratorパターンを使うと，よく似ている小さなクラスがたくさん作られてしまう


## 補講：継承と移譲における同一視
### 継承--サブクラスとスーパークラスとを同一視
### 委譲--自分と委譲先を同一視
