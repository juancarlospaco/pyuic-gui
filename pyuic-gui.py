#!/usr/bin/env python
# -*- coding: utf-8 -*-


#############################################################################
## This file may be used under the terms of the GNU General Public
## License version 2.0 or 3.0 as published by the Free Software Foundation
## and appearing in the file LICENSE.GPL included in the packaging of
## this file.  Please review the following information to ensure GNU
## General Public Licensing requirements will be met:
## http:#www.fsf.org/licensing/licenses/info/GPLv2.html and
## http:#www.gnu.org/copyleft/gpl.html.
##
## This file is provided AS IS with NO WARRANTY OF ANY KIND, INCLUDING THE
## WARRANTY OF DESIGN, MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE.
#############################################################################


# metadata
"""PyUIc4 GUI"""
__version__ = ' 0.6.66 '
__license__ = ' GPL '
__author__ = ' juancarlospaco '
__email__ = ' juancarlospaco@gmail.com '
__url__ = 'https://github.com/juancarlospaco/pyuic-gui'
__date__ = ' 04/2014 '
__docformat__ = 'html'


# imports
import sys
from os import path
import subprocess

from PyQt4 import QtCore
from PyQt4.QtCore import Qt
from PyQt4.QtGui import (QMainWindow, QLabel, QSlider, QCursor, QIcon,
                         QDialogButtonBox, QComboBox, QApplication,
                         QPainter, QPalette, QColor, QFileDialog, QMessageBox)


###############################################################################


class MyMainWindow(QMainWindow):
    ' Main Window '
    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)
        self.statusBar().showMessage(__doc__)
        self.setWindowTitle(__doc__)
        self.setMinimumSize(250, 280)
        self.setMaximumSize(300, 300)
        self.resize(250, 290)
        self.setWindowIcon(QIcon.fromTheme("face-monkey"))
        self.setStyleSheet('''QWidget { color: rgba( 0, 255, 255, 255 );
            background-color: #323232; font-family: 'Ubuntu Light';
            font-size: 14px;
            }

            QToolTip {
                border: 1px solid black;
                background-color: #ffa02f;
                background-image: None;
                padding: 1px;
                border-radius: 3px;
                opacity: 100;
            }

            QWidget:item:hover {
                background-color: QLinearGradient(
                    x1: 0, y1: 0,
                    x2: 0, y2: 1,
                    stop: 0 #ffa02f,
                    stop: 1 #ca0619
                );
                color: #000000;
            }

            QWidget:item:selected {
                background-color: QLinearGradient(
                    x1: 0, y1: 0,
                    x2: 0, y2: 1,
                    stop: 0 #ffa02f,
                    stop: 1 #d7801a
                );
            }

            QWidget:disabled {
                color: #404040;
                background-color: #323232;
            }

            QWidget:focus {
                background-image: None;
                border: 2px solid QLinearGradient(
                    x1: 0, y1: 0,
                    x2: 0, y2: 1,
                    stop: 0 #ffa02f,
                    stop: 1 #d7801a
                );
            }

            QPushButton {
                background-color: QLinearGradient(
                    x1: 0, y1: 0,
                    x2: 0, y2: 1,
                    stop: 0 #565656,
                    stop: 0.1 #525252,
                    stop: 0.5 #4e4e4e,
                    stop: 0.9 #4a4a4a,
                    stop: 1 #464646
                );
                border-width: 1px;
                border-color: #1e1e1e;
                border-style: solid;
                border-radius: 6;
                padding: 3px;
                font-size: 12px;
                padding-left: 5px;
                padding-right: 5px;
                background-image: None;
            }

            QPushButton:pressed {
                background-image: None;
                background-color: QLinearGradient(
                    x1: 0, y1: 0,
                    x2: 0, y2: 1,
                    stop: 0 #2d2d2d,
                    stop: 0.1 #2b2b2b,
                    stop: 0.5 #292929,
                    stop: 0.9 #282828,
                    stop: 1 #252525
                );
            }

            QComboBox {
                background-image: None;
                selection-background-color: #ffaa00;
                background-color: QLinearGradient(
                    x1: 0, y1: 0,
                    x2: 0, y2: 1,
                    stop: 0 #565656,
                    stop: 0.1 #525252,
                    stop: 0.5 #4e4e4e,
                    stop: 0.9 #4a4a4a,
                    stop: 1 #464646
                );
                border-style: solid;
                border: 1px solid #1e1e1e;
                border-radius: 5;
            }

            QComboBox:hover, QPushButton:hover {
                background-image: url(.bg.png);
                border: 2px solid QLinearGradient(
                    x1: 0, y1: 0,
                    x2: 0, y2: 1,
                    stop: 0 #ffa02f,
                    stop: 1 #d7801a
                );
            }

            QComboBox:on {
                padding-top: 3px;
                padding-left: 4px;
                background-color: QLinearGradient(
                    x1: 0, y1: 0,
                    x2: 0, y2: 1,
                    stop: 0 #2d2d2d,
                    stop: 0.1 #2b2b2b,
                    stop: 0.5 #292929,
                    stop: 0.9 #282828,
                    stop: 1 #252525
                );
                selection-background-color: #ffaa00;
                background-image: None;
            }

            QComboBox QAbstractItemView {
                background-image: None;
                border: 2px solid darkgray;
                selection-background-color: QLinearGradient(
                    x1: 0, y1: 0,
                    x2: 0, y2: 1,
                    stop: 0 #ffa02f,
                    stop: 1 #d7801a
                );
            }

            QComboBox::drop-down {
                 subcontrol-origin: padding;
                 subcontrol-position: top right;
                 width: 15px;
                 border-left-width: 0px;
                 border-left-color: darkgray;
                 border-left-style: solid;
                 border-top-right-radius: 3px;
                 border-bottom-right-radius: 3px;
                 background-image: None;
             }

            QComboBox::down-arrow { background-image: None; }

            QSlider {
                border-width: 2px;
                border-color: #1e1e1e;
                border-style: solid;
                padding: 3px;
                font-size: 8px;
                padding-left: 5px;
                padding-right: 5px;
                width: 25px;
                border-radius: 5px;
            }

            QSlider::sub-page:vertical {
                background: red;
                border: none;
                width: 25px;
            }

            QSlider::add-page:vertical {
                background: green;
                border: none;
                width: 25px;
            }

            QSlider::handle:vertical {
                background-color: QLinearGradient(spread:pad, x1:0, y1:0, x2:1,
                    y2:0.273, stop:0 rgba(0, 0, 0, 255),
                    stop:1 rgba(150, 255, 255, 255)
                    );
                width: 10px;
                height: 25px;
                border: 1px solid grey;
                text-align: center;
                border-top-left-radius: 2px;
                border-bottom-left-radius: 2px;
                border-top-right-radius: 2px;
                border-bottom-right-radius 2px;
                margin-left: 2px;
                margin-right: 2px;
            }

            QSlider::handle:vertical:hover {
                border: 2px solid #ffaa00;
                margin-left: 2px;
                margin-right: 2px;
            }

            QSlider::sub-page:vertical:disabled {
                background: #bbb;
                border-color: #999;
            }

            QSlider::add-page:vertical:disabled {
                background: #eee;
                border-color: #999;
            }

            QSlider::handle:vertical:disabled {
                background: #eee;
                border: 1px solid #aaa;
                border-radius: 4px;
            } ''')

        self.label1 = QLabel(self)
        self.label1.setText('Use Debug')
        self.label1.setGeometry(QtCore.QRect(25, 25, 125, 25))

        self.slider1 = QSlider(self)
        self.slider1.setGeometry(QtCore.QRect(150, 25, 25, 25))
        self.slider1.setTickInterval(1)
        self.slider1.setCursor(QCursor(QtCore.Qt.OpenHandCursor))
        self.slider1.TickPosition(QSlider.TicksBothSides)
        self.slider1.setRange(0, 1)
        self.slider1.setValue(1)
        self.sli1lbl = QLabel(str(self.slider1.value()), self.slider1)
        self.sli1lbl.move(9, 5)
        self.sli1lbl.setAutoFillBackground(False)
        self.slider1.valueChanged.connect(
            lambda: self.sli1lbl.setText(str(self.slider1.value())))
        self.slider1.sliderPressed.connect(
            lambda: self.slider1.setCursor(QCursor(QtCore.Qt.ClosedHandCursor)))
        self.slider1.sliderReleased.connect(
            lambda: self.slider1.setCursor(QCursor(QtCore.Qt.OpenHandCursor)))

        self.label2 = QLabel(self)
        self.label2.setText('Make Executable')
        self.label2.setGeometry(QtCore.QRect(25, 75, 125, 25))

        self.slider2 = QSlider(self)
        self.slider2.setGeometry(QtCore.QRect(150, 75, 25, 25))
        self.slider2.setTickInterval(1)
        self.slider2.setCursor(QCursor(QtCore.Qt.OpenHandCursor))
        self.slider2.TickPosition(QSlider.TicksBothSides)
        self.slider2.setRange(0, 1)
        self.slider2.setValue(1)
        self.sli2lbl = QLabel(str(self.slider2.value()), self.slider2)
        self.sli2lbl.move(9, 5)
        self.sli2lbl.setAutoFillBackground(False)
        self.slider2.valueChanged.connect(
            lambda: self.sli2lbl.setText(str(self.slider2.value())))
        self.slider2.sliderPressed.connect(
            lambda: self.slider2.setCursor(QCursor(QtCore.Qt.ClosedHandCursor)))
        self.slider2.sliderReleased.connect(
            lambda: self.slider2.setCursor(QCursor(QtCore.Qt.OpenHandCursor)))

        self.label3 = QLabel(self)
        self.label3.setText('Relative Imports')
        self.label3.setGeometry(QtCore.QRect(25, 125, 125, 25))

        self.slider3 = QSlider(self)
        self.slider3.setGeometry(QtCore.QRect(150, 125, 25, 25))
        self.slider3.setTickInterval(1)
        self.slider3.setCursor(QCursor(QtCore.Qt.OpenHandCursor))
        self.slider3.TickPosition(QSlider.TicksBothSides)
        self.slider3.setRange(0, 1)
        self.slider3.setValue(0)
        self.sli3lbl = QLabel(str(self.slider3.value()), self.slider3)
        self.sli3lbl.move(9, 5)
        self.sli3lbl.setAutoFillBackground(False)
        self.slider3.valueChanged.connect(
            lambda: self.sli3lbl.setText(str(self.slider3.value())))
        self.slider3.sliderPressed.connect(
            lambda: self.slider3.setCursor(QCursor(QtCore.Qt.ClosedHandCursor)))
        self.slider3.sliderReleased.connect(
            lambda: self.slider3.setCursor(QCursor(QtCore.Qt.OpenHandCursor)))

        self.label4 = QLabel(self)
        self.label4.setText('Indent Spaces')
        self.label4.setGeometry(QtCore.QRect(25, 175, 125, 25))

        self.combo1 = QComboBox(self)
        self.combo1.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.combo1.addItems(['4', '0', '2', '6', '8'])
        self.combo1.setGeometry(QtCore.QRect(150, 175, 50, 25))

        self.buttonBox = QDialogButtonBox(self)
        self.buttonBox.setGeometry(QtCore.QRect(25, 225, 200, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(
            QDialogButtonBox.Ok | QDialogButtonBox.Cancel |
            QDialogButtonBox.Close | QDialogButtonBox.Help)
        self.buttonBox.setCenterButtons(False)
        self.buttonBox.helpRequested.connect(lambda: QMessageBox.about(
            self, __doc__, str(__doc__ + ', ' + ',\nversion ' + __version__ +
                               '(' + __license__ + '),\nby ' + __author__ + ', '
                               + __email__)))
        self.buttonBox.accepted.connect(self.run)
        self.buttonBox.rejected.connect(self.close)
        palette = self.palette()
        palette.setBrush(QPalette.Base, Qt.transparent)
        self.setPalette(palette)
        self.setAttribute(Qt.WA_OpaquePaintEvent, False)

    def run(self):
        'Run the actual conversion.'
        # Ask the User for the source .ui file as input
        filein = str(QFileDialog.getOpenFileName(
            self, __doc__, path.expanduser("~"), 'UI(*.ui)')).strip()
        # Parse Value of Slider1 as the Debug flag parameter
        if self.slider1.value() == 0:
            arg1 = ''
        else:
            arg1 = '--debug '
        # Parse Value of Slider2 as the Execute flag parameter
        if self.slider2.value() == 0:
            arg2 = ''
        else:
            arg2 = '--execute '
        # Parse Value of Slider3 as the relative imports flag parameter
        if self.slider3.value() == 0:
            arg3 = ''
        else:
            arg3 = '--from-imports '
        # debug
        #print(arg1, arg2, arg3, str(self.combo1.currentText()))
        # run the subprocesses
        subprocess.Popen(
            'nice --adjustment=19 pyuic4 ' + arg1 + arg2 + arg3 +
            '--indent=' + str(self.combo1.currentText()) +
            ' --output=' + str(filein).lower().replace('.ui', '.py') +
            ' ' + filein +
            ' && chmod -v +x ' + str(filein).lower().replace('.ui', '.py'),
            shell=True)

    def paintEvent(self, event):
        ' Paint semi-transparent background '
        painter = QPainter(self)
        painter.fillRect(event.rect(), Qt.transparent)
        painter.setPen(Qt.NoPen)
        painter.setBrush(QColor(0, 0, 0))
        painter.setOpacity(0.75)
        painter.drawRoundedRect(self.rect(), 75, 50)
        painter.end()


###############################################################################


def main():
    """Main Loop"""
    app, w = QApplication(sys.argv), MyMainWindow()
    app.setStyle('Windows')
    w.setAttribute(Qt.WA_TranslucentBackground, True)
    w.setWindowFlags(w.windowFlags() | QtCore.Qt.FramelessWindowHint)
    w.show()
    sys.exit(app.exec_())


if __name__ in '__main__':
    main()
