#!/usr/bin/env python
# coding: utf-8

import argparse
import sys
from abc import ABCMeta, abstractmethod
from functools import singledispatch

from zope.interface import Interface, implementer
import better_exceptions
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QCheckBox

# Mediatorインタフェース
class Mediator():
    @abstractmethod
    def create_colleagues(self):
        pass

    @abstractmethod
    def colleague_changed(self):
        pass

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
    def __init__(self, caption: str, obj):
        super().__init__(caption, obj)

    def set_mediator(self, mediator: 'Mediator'):
        self.mediator = mediator

    def set_colleague_enabled(self, enabled: bool):
        self.setEnabled(enabled)


@implementer(Colleague)
class ColleagueTextField(QLineEdit):
    def __init__(self, obj):
        super().__init__(obj)

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
class ColleagueCheckBox(QCheckBox):
    def __init__(self, caption, obj):
        super().__init__(caption, obj)

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


class LoginFrame(QWidget):
    def __init__(self, title: str):
        super().__init__()
        self.create_colleague()
        self.show()

    def create_colleague(self):
        self.check_guest = ColleagueCheckBox('Guest', self)
        self.check_login = ColleagueCheckBox('Login', self)
        self.text_user = ColleagueTextField(self)
        self.text_pass = ColleagueTextField(self)

        self.button_ok = ColleagueButton("OK", self)
        self.button_ok.resize(self.button_ok.sizeHint())
        self.button_ok.move(50, 50)
        self.button_ok.set_colleague_enabled(False)

        self.setGeometry(300, 300, 300, 200)
        # self.button_cancel = ColleagueButton("Cancel")

    def colleague_changed(self):
        pass


def main():
    app = QApplication(sys.argv)

    window = LoginFrame('Login')
    # window = QWidget()
    # window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
