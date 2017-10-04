# Mediator
* メンバーはみんな相談役だけに報告し，メンバーへの指示は相談役だけから来る

## 何故Mediatorを使うか
* 多数のオブジェクト間の調整を行わなければならない時こそMediatorの出番
* 表示のコントロールのロジックは相談役の中にだけ記述する

## Mediatorパターンの登場人物

* Mediator(調停者，仲介者)の役
    * Colleague役と通信を行って，調整を行なうためのインタフェース(API)を定める
    * Mediatorインタフェースがこの役
* ConcreteMediator(具体的な調停者)の役
    * Mediator役のインタフェース(API)を実装し，実際の調整を行なう
    * LoginFrameがこの役
* Colleague(同僚)の役
    * Mediator役と通信を行なうインタフェース(API)を定める
    * Colleagueインタフェースがこの役
* ConcreteColleague(具体的な同僚)の役
    * Colleague役のインタフェースを定義する
    * ColleagueButton，ColleagueTextField，ColleagueCheckboxの各クラスがこの役

## あなたの考えを広げるためのヒント

### 分散が災いになるとき
* colleagueChangedメソッドは複雑だが，このメソッドにバグが入っても，表示の有効/無効に関するロジックはここにだけ存在するので，ここだけデバッグすればいい
* オブジェクト指向では一極集中を避け，処理を分散させることが多い
* しかし，サンプルプログラムのような場合は分散させるのは賢明でない
* 各クラスに分散させるべきことは分散させ，集中させるべきことは集中させないと帰って災いとなる

### 通信経路の増加
* 同じ立場のインスタンスがたくさん存在するとき，それらを互いに通信(メソッドを呼び合う)させると，プログラムは複雑になる

### 再利用できるのは何か？
* ConcreteColleague役は再利用しやすい
* ConcreteMediator役は再利用しにくい
    * アプリケーションへの依存性が高い部分が閉じ込められているため

## この章で学んだこと
* Mediatorパターンは，複雑に絡み合うオブジェクトたちの相互通信を辞め，Mediator役に情報を集中させることで処理を整理する