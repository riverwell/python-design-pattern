# Singleton
* インスタンスが1個しか存在しないことを保証する
    * singletonとは，要素を1個しか持たない集合のこと

## aaa
* Singletonのコンスタラクタはprivateにする(pythonではできない)
    * インスタンスが一個しか生成されない(うっかり外からnewされない)ことを保証するため

## 何故Singletonを使うか


## Singletonパターンの登場人物
* Singletonの役
    * Singletonの役は，唯一のインスタンスを得るためのstaticメソッドを持っている(pythonでは実装が異なる)
    * このメッソッドはいつも同じインスタンスを返す
    * Singletonクラスが該当

## あなたの考えを広げるためのヒント
### なぜ制限を設ける必要があるか
* Singletonパターンではインスタンスの数に制限を設ける
* 制限を課すということは，前提になる条件を増やす，ということ
* インスタンスが複数存在すると，相互に影響し合って思いがけないバグを生み出してしまう可能性がある
* インスタンスが1つと保証されていれば，その前提条件の元でプログラミングができる

## 関連しているパターン
* 以下のパターンは，インスタンスが1つである場合が多い
    * Abstract Factory
    * Builder
    * Facade
    * Prototype