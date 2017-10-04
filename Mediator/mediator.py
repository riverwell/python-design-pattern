#!/usr/bin/env python
# coding: utf-8

import argparse
import sys
from abc import ABCMeta, abstractmethod

from zope.interface import Interface, implementer
import better_exceptions
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QRadioButton, QGridLayout, QButtonGroup


# Mediatorインタフェース
class Mediator(Interface):
    @abstractmethod
    def create_colleagues(self):
        """

        :return:
        """

    @abstractmethod
    def colleague_changed(self):
        """

        :return:
        """


# Colleagueインタフェース
class Colleague(Interface):
    @abstractmethod
    def set_mediator(self, mediator: 'Mediator'):
        """

        :param mediator:
        :return:
        """

    @abstractmethod
    def set_colleague_enabled(self, enabled: bool):
        """

        :param enabled:
        :return:
        """


@implementer(Colleague)
class ColleagueButton(QPushButton):
    def __init__(self, caption: str, parent: object):
        super().__init__(caption, parent)

    def set_mediator(self, mediator: 'Mediator'):
        self.mediator = mediator

    def set_colleague_enabled(self, enabled: bool):
        self.setEnabled(enabled)


@implementer(Colleague)
class ColleagueTextField(QLineEdit):
    def __init__(self, text: str, columns: int, parent: object):
        super().__init__(parent)

    # Mediatorを保持
    def set_mediator(self, mediator: 'Mediator'):
        self.mediator = mediator

    # Mediatorから有効/無効が指示される
    def set_colleague_enabled(self, enabled: bool):
        self.setEnabled(enabled)

    # 独自
    # 文字列が変化したらMediatorに通知
    def text_value_changed(self):
        self.mediator.colleague_changed()


@implementer(Colleague)
class ColleagueCheckBox(QRadioButton):
    def __init__(self, caption: str, g: QButtonGroup, state: bool, no: int, parent: object):
        super().__init__(caption, parent)
        g.addButton(self, no)

    # Mediatorを保持
    def set_mediator(self, mediator: 'Mediator'):
        self.mediator = mediator

    # Mediatorから有効/無効が指示される
    def set_colleague_enabled(self, enabled: bool):
        self.setEnabled(enabled)

    # 独自
    # 文字列が変化したらMediatorに通知
    def item_state_changed(self):
        self.mediator.colleague_changed()


@implementer(Mediator)
class LoginFrame(QWidget):
    def __init__(self, title: str):
        super().__init__()
        self.create_colleagues()
        grid_layout = QGridLayout()
        grid_layout.addWidget(self.check_guest, 0, 0)
        grid_layout.addWidget(self.check_login, 0, 1)
        grid_layout.addWidget(self.text_user, 1, 0)
        grid_layout.addWidget(self.text_pass, 2, 0)
        grid_layout.addWidget(self.button_ok, 3, 0)
        grid_layout.addWidget(self.button_cancel, 3, 1)
        self.setLayout(grid_layout)

    def create_colleagues(self):
        self.g = QButtonGroup()
        self.check_guest = ColleagueCheckBox('Guest', self.g, True, 1, self)
        self.check_login = ColleagueCheckBox('Login', self.g, False, 2, self)
        self.text_user = ColleagueTextField('', 10, self)
        self.text_pass = ColleagueTextField('', 10, self)
        self.button_ok = ColleagueButton("OK", self)
        self.button_cancel = ColleagueButton("Cancel", self)

        # Mediatorセット
        self.check_guest.set_mediator(self)
        self.check_login.set_mediator(self)
        self.text_user.set_mediator(self)
        self.text_pass.set_mediator(self)
        self.button_ok.set_mediator(self)
        self.button_cancel.set_mediator(self)

        # Listenerのセット
        self.check_guest.clicked.connect(self.check_guest.item_state_changed)
        self.check_login.clicked.connect(self.check_login.item_state_changed)
        self.text_user.textChanged.connect(self.text_user.text_value_changed)
        self.text_pass.textChanged.connect(self.text_pass.text_value_changed)

        self.setGeometry(300, 300, 300, 200)

    def colleague_changed(self):
        if self.check_guest.isChecked():
            self.text_user.set_colleague_enabled(False)
            self.text_pass.set_colleague_enabled(False)
            self.button_ok.set_colleague_enabled(True)
        else:
            self.text_user.set_colleague_enabled(True)

    # text_userまたはtext_passの変更があった
    # 各Colleagueの有効/無効を判定する
    def __user_pass_changed(self):
        if len(self.text_user.text):
            self.text_pass.set_colleague_enabled(True)
            if len(self.text_pass.text):
                self.button_ok.set_colleague_enabled(True)
            else:
                self.text_pass.set_colleague_enabled(False)
                self.button_ok.set_colleague_enabled(False)


def main():
    app = QApplication(sys.argv)

    window = LoginFrame('Login')
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
