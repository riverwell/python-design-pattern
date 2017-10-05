# Observer
* オブジェクトの状態変化を他のオブジェクトに通知する
    * 観察対象の状態が変化すると、観察者に対して通知される

## 何故Observerを使うか
* 状態変化に応じた処理を記述する時に有効

## Observerパターンの登場人物
* Subject(被験者)の役
    * 観察される側．観察者であるObserver役を登録するメソッドと削除するメソッドを持つ
    * また，現在の状態を取得するメソッドも宣言されている
    * NumberGeneratorがこの役をつとめる
* ConcreteSubject(具体的な被験者)の役
    * 具体的な観察される側を表現する役
    * 状態が変化したら，そのことを登録されているObserver役に伝える
    * RandomNumberGeneratorがこの役
* Observer(観察者)の役
    * Observer役は，Subject役から状態が変化したよと教えてもらう役
    * そのためのメソッドがupdate
    * Observerインタフェースがこの役
* ConcreteObserver(具体的な観察者)の役
    * 具体的なObserver
    * updateメソッドが呼び出されると，そのメソッドの中でSubject役の現在の状態を取得
    * DigitObserverクラスやGraphObserverクラスがこの役

## あなたの考えを広げるためのヒント

### ここにも交換可能性が登場する
* 抽象クラスやインタフェースを使って，具象クラスから抽象メソッドを引き剥がす
* 引数でインスタンスを渡すときや，フィールドでインスタンスを保持するときには，具象クラスの型にしないで，抽象クラスやインタフェースの型にしておく

### Observerの順序
* ConcreteObserver役のクラスを設計するときには，updateメソッドが呼び出される順序が変わっても問題が起きないようにする

### 「観察」よりも「通知」になっている
* ObserverパターンはPublish-Subscribeパターンとも呼ばれる

### Model/View/Controller (MVC)
* MVCのModelとViewの関係は，ObserverパターンのSubject役とObserver役の関係に対応

