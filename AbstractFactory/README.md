# AbstractFactory
* 抽象的な工場で，抽象的な部品を組み合わせて抽象的な製品を作る
    * オブジェクト指向における「抽象的」
        * 「具体的にどのように実装されているかには考えず，インタフェース(API)にだけ注目している」状態
* 言い換えると，部品のAPIにだけ注目し，そのAPIを使って，部品を組み立て，製品にまとめる
* 著者曰くAbstractFactoryが一番難しい

## 何故AbstractFactoryを使うか
* インスタンスの生成を専門に行うクラスを用意することで、整合性を必要とされる一連のオブジェクト群を間違いなく生成する
* 具体的なクラスで，変数itemの中身が実際に何なのかを調べてswitch文やif文を使うようなプログラムを書いてはいけない
    * とても非オブジェクト指向的なプログラムになる

## AbstractFactoryパターンの登場人物
* AbstractProduct(抽象的な製品)の役
    * AbstractFactory役によって作り出される抽象的な部品や製品のインタフェース(API)を定める
    * Link，Tray，Pageクラスがこの役
* AbstractFactory(抽象的な工場)の役
    * AbstractProduct役のインスタンスを作り出すためのインタフェース(API)を定める
    * Factoryクラスがこの役
* Client(依頼者)の役
    * AbstractFactory約とAbstractProduct約のインタフェース(API)だけを使って仕事を行なう役
    * Client役は具体的な製品や工場については知らない
    * Mainがこの役を務める
* ConcreteProduct(具体的な製品)の役
    * AbstractProduct役のインタフェースを実装する
    * ListLink，ListTray，ListPageクラスがこの役
* ConcreteFactory(具体的な工場)の役
    * AbstarctFactory役のインタフェース(API)を実装する
    * ListFactoryクラスがこの役を務める

## あなたの考えを広げるためのヒント
### 具体的な工場を新たに追加するのは簡単
* 簡単というのは，どのようなクラスを作り，どのようなメソッドを実装すればいいかがはっきりしている
* このときいくら具体的な工場を追加しても，抽象的な工場やMainの部分を修正する必要は全くない

## 部品を新たに追加するのは困難
* factoryパッケージに画像を表すPictureという部品を追加する場合，既に存在する具体的な工場全てにPictureに対応した修正が加わる
