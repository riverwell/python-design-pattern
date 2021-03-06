# Prototype
* クラスからインスタンスを生成するのではなく，原型・模範となるインスタンスから新しいインスタンスを作り出す
    * 複製を作る操作をjavaではcloneと呼ぶ

## 何故Prototypeを使うか
* 次のような時，クラスからインスタンスを作るのでなく，インスタンスを複製したい
    1. 種類が多すぎてクラスにまとめられない場合
        * 1つ1つを別のクラスにしていたら，ソースファイルを多数作成する必要が生じてしまう場合
    2. クラスからのインスタンス生成が難しい
        * 生成したいインスタンスが複雑な過程を経て作られるので，クラスから作り上げることが難しい場合
            * 例えば，グラフィカルエディタでユーザが描画した図形クラスなど
    3. フレームワークと生成するインスタンスを分けたい場合
        * インスタンスを生成する時のフレームワークを，特定のクラスに依存しないように作りたい場合
            * 前もって「雛形」となるインスタンスを登録しておき，その登録したインスタンスをコピーすることでインスタンスを生成

## Prototypeパターンの登場人物
* Prototype(原型)の役
    * インスタンスをコピー(複製)して新しいインスタンスを作るためのメソッドを定める
    * Productインターフェイスが該当
* ConcretePrototype(具体的な原型)の役
    * インスタンスをコピーして新しいインスタンスを作るメソッド
    * MessageBoxやUnderlineクラスが該当
* Client(利用者)の役
    * インスタンスをコピーするメソッドを利用して，新しいインスタンスを作る
    * Managerクラスが該当

## あなたの考えを広げるためのヒント
### クラスからインスタンスを作ってはいけないのか
1. 種類が多すぎてクラスにまとめられない場合
    * サンプルプログラムでは3つの雛形が登場した
    * これらを全て別々のクラスにしてしまっては，クラスの種類が多くなりすぎてソースコードを管理しづらくなる
2. クラスからのインスタンス生成が難しい場合
3. フレームワークと生成するインスタンスを分けたい場合
    * サンプルプログラムではインスタンスのコピーを行う部分をframeworkパッケージにれている
    * これによりクラス名の束縛からフレームワークを分離している

### クラス名は束縛なのか
* ソースの中に利用するクラスの名前がかかれていると，そのクラスと切り離して再利用することはできなくなってしまう
* 手元にあるのがクラスファイル(.class)だけでもそのクラスを再利用できるかが大切
* ソースファイル(.java)がなくても再利用できるか，がポイント
* 蜜に結合しなければならないクラスの名前がソース中に書かれるのは当然
* 部品として独立させなければならないクラスの名前がソースの中に書かれていることが問題
