# Visitor
* データ構造と処理を分離する
    * データ構造の中を巡り歩く主体である「訪問者」を表すクラスを用意し，そのクラスに処理を任せる
    * データ構造は戸を叩いてくる訪問者を受け入れてあげれば良い

## 何故Visitorを使うか
*

## Visitorパターンの登場人物
* Visitor(訪問者)の役
    * データ構造の具体的な要素(ConcreteElement役)ごとに「XXXXを訪問した」というvisit(XXXX)メソッドを宣言する
    * visit(XXXX)はXXXXを処理するためのメソッドで，実際のコードはConcreteVisitor役の側に書かれる
    * Visitorクラスがこの役
* ConcreteVisitor(具体的な訪問者)の役
    * Visitor役のインタフェース(API)を実装
    * visit(XXXX)という形のメソッドを実装し，個々のConcreteElement役ごとの処理を記述する
    * ListVisitorクラスがこの役
* Element(要素)の役
    * Visitor役の訪問先を表す役
    * 訪問者を受け入れるacceptメソッドを宣言する
        * 引数にVisitor役が渡される
    * Elementインタフェースがこの役
* ConcreteElement(具体的な要素)の役
    * Element役のインタフェースを実装する役
    * FileクラスやDirectoryクラスがこの役
* ObjectStructure(オブジェクト構造)の役
    * Element役の集合を扱う役
    * ConcreteVisitor役が個々のElementを扱えるようなメソッドを備えている
    * Directoryクラスがこの役(一人二役)
        * ConcreteVisitor役が個々のElement役を扱えるように，iteratorメソッドが用意されている


## あなたの考えを広げるためのヒント
### ダブルディスパッチ
* accept(受け入れメソッド)は次のような呼び出し
    * element.accept(visitor)，visitor.visit(element)
* visit(訪問)メソッドは次のような呼び出し
    * visitor.visit(element)
* この2つを見比べると，ちょうど反対の関係にありますね
* Visitorパターンでは，ConcreteElement役とConcreteVisitor役の組によって実際の処理が決定する
* これを一般にダブルディスパッチ(double dispatch:二重の振り分け)と呼ぶ

### なぜこんなに複雑なことをするのか
* Visitorパターンの役割は，処理をデータ構造から分離すること
* Visitorパターンは，FileクラスやDirecotryクラスの部品としての独立性を高めていることになります
* もし処理の内容をFileクラスやDirectoryクラスのメソッドとしてプログラムしてしますと，新しい処理を追加して機能拡張したくなる度，FileクラスやDirectoryクラスを修正しなければならなくなる

### The Open-Closed Principle -- 拡張については開き，修正については閉じる
* 機能拡張と修正の話が出たところで，OCP原則について話そう
* OCP原則
    * 拡張(extension)については開かれている(open)が
        * 理由なく拡張を禁止してはいけない
    * 修正(modification)については閉じられている(closed)
        * 拡張を行っても既存のクラスを修正する必要がない
* 既存のクラスを修正せずに拡張できるようにせよ
    * 部品として再利用性が高きクラスになる

### ConcreteVisitor役の追加は簡単
* 新しいConcreteVisitor役を追加するのは簡単
* 具体的な処理はConcreteVisitor役に任せることができ，その処理のためにConcreteElement役を修正する必要はまったくない

### ConcreteElement役の追加は困難
* EntryクラスのサブクラスとしてDeviceクラスを追加する場合
    * つまりFile，Directoryの兄弟
* Visitorクラスにはvisit(Device)を追加する必要が処汁
* そして，Visitorクラスのサブクラス全部に新たにvisit(Device)メソッドを実装しなければならない

### Visitorが処理するためには何が必要か
* Visitorパターンでは，データ構造の要素に対する処理を切り出してVisitor役に任せる
* Element役はVisitor役に対して十分な情報を公開する必要がある
* 必要な情報が得られないと訪問者はうまく働けないが，公開すべきでない情報までを公開してしまうと，将来的に構造を改良するのが難しくなる


## メモ
* pythonでオーバーロードを使うにはsigledispatch(PyPlよりインストール)を使う
* メソッドディスパッチは、メッセージに応答して呼び出されるメソッドを決定するために使用されるアルゴリズム