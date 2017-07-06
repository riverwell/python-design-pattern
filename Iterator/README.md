# Iterator
* 集合体から1つずつ要素を取り出して数え上げていく

## 何故Iteratorを使うか
* Iteratorを使うことで，実装とは切り離して，数え上げを行なうことが出来るから
    * 例えば，本の管理に配列を使うのを辞めて，ベクトルを使うようプログラムが修正されても，has_nextとnextが正しく実装されていれば，whileループを変更しなくても，動作する


## Iteretaorパターンの登場人物
* Iterator(反復子)の役
    * 要素を順番にスキャンしていくインタフェース(API)を定める役
    * Iteratorインタフェースが該当

* ConcreteIterator(具体的な反復子)の役
    * Iteratorが定めたインターフェース（API）を実装する役
    * スキャンするために必要な情報を持っておく必要がある
    * BookShelfIteratorクラスが該当

* Aggregate(集合体)の役
    * Iterator役を作り出すインタフェース(API)を定める役
    * APIは「私が持っている要素を順番にスキャンしてくれる人」を作り出すメソッド
    * Aggregateインタフェースが該当

* ConcreteAggregate(具体的な集合体)の役
    * Aggregate役が定めたインタフェース(API)を実際に実装する役
    * ConcreteIterator役のインスタンスを作り出す
    * BookShelfクラスが該当

## 抽象クラスやインタフェースは苦手で，，，
* 抽象クラスやインタフェースがよくわからない人は，いきなりConcreteAggregate役やConcreteIterator役の上でプログラミングをしてしまいがち．
* すべての問題を具体的なクラスだけで解決させてしまいたくなる
* しかし，具体的なクラスだけを使うと，クラス間の結合が強くなってしまい，部品として再利用することが難しくなる
* 結合を弱め，クラスを部品として再利用しやすくするために，抽象クラスやインタフェースが導入される

## AggregateとIteratorの対応
* BookShelfの実装をガラリと変えた場合には，BookShelfIteratorも修正が必要になる
* AggregateとIteratorの2つのインタフェースが対になっているように，BookShelfとBookShelfIteratorという2つのクラスも対になっている


### インターフェースと抽象クラスの違い
* インターフェース
    * メソッドの実装を強制
    * pythonでは，classのメソッドに@abstractmethodをつけることで代わりとした
    * 抽象メソッドで実装することで子クラスでの実装を強制

* 抽象クラス
    * 継承して子クラスの作成を強制
    * 実装する際はclass Hoge(metaclass=ABCMeta)を指定

* pythonでの実装には from abc import ABCMeta, abstractmethod を使用する

