# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'decryptUi.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(611, 519)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        Dialog.setFont(font)
        Dialog.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.btn_help = QtWidgets.QPushButton(Dialog)
        self.btn_help.setMinimumSize(QtCore.QSize(0, 40))
        self.btn_help.setMaximumSize(QtCore.QSize(200, 16777215))
        self.btn_help.setObjectName("btn_help")
        self.horizontalLayout_4.addWidget(self.btn_help)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_3 = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("一纸情书")
        font.setPointSize(20)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.label_9 = QtWidgets.QLabel(Dialog)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.verticalLayout.addWidget(self.label_9)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_phone = QtWidgets.QLabel(Dialog)
        self.label_phone.setText("")
        self.label_phone.setObjectName("label_phone")
        self.gridLayout.addWidget(self.label_phone, 2, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 1, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setStyleSheet("background:transparent;\n"
"\n"
"                                                                    border-radius:5px;\n"
"                                                                    border-top: 0px solid #b2e281;\n"
"                                                                    border-bottom: 2px solid black;\n"
"                                                                    border-right: 0px solid #b2e281;\n"
"                                                                    border-left: 0px solid #b2e281;\n"
"\n"
"\n"
"                                                                    border-style:outset\n"
"                                                                ")
        self.lineEdit.setFrame(False)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 4, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 3, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 5, 0, 1, 1)
        self.label_key = QtWidgets.QLabel(Dialog)
        self.label_key.setMaximumSize(QtCore.QSize(400, 16777215))
        self.label_key.setText("")
        self.label_key.setObjectName("label_key")
        self.gridLayout.addWidget(self.label_key, 5, 1, 1, 1)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.label_pid = QtWidgets.QLabel(Dialog)
        self.label_pid.setText("")
        self.label_pid.setObjectName("label_pid")
        self.gridLayout.addWidget(self.label_pid, 0, 1, 1, 1)
        self.label_name = QtWidgets.QLabel(Dialog)
        self.label_name.setText("")
        self.label_name.setObjectName("label_name")
        self.gridLayout.addWidget(self.label_name, 3, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 4, 0, 1, 1)
        self.label_version = QtWidgets.QLabel(Dialog)
        self.label_version.setText("")
        self.label_version.setObjectName("label_version")
        self.gridLayout.addWidget(self.label_version, 1, 1, 1, 1)
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 6, 0, 1, 1)
        self.label_db_dir = QtWidgets.QLabel(Dialog)
        self.label_db_dir.setMaximumSize(QtCore.QSize(400, 300))
        self.label_db_dir.setText("")
        self.label_db_dir.setObjectName("label_db_dir")
        self.gridLayout.addWidget(self.label_db_dir, 6, 1, 1, 1)
        self.gridLayout.setColumnMinimumWidth(0, 1)
        self.gridLayout.setColumnStretch(0, 1)
        self.gridLayout.setColumnStretch(1, 10)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 2, 1)
        self.btn_getinfo = QtWidgets.QPushButton(Dialog)
        self.btn_getinfo.setMinimumSize(QtCore.QSize(0, 40))
        self.btn_getinfo.setObjectName("btn_getinfo")
        self.gridLayout_2.addWidget(self.btn_getinfo, 0, 1, 1, 1)
        self.checkBox = QtWidgets.QCheckBox(Dialog)
        self.checkBox.setText("")
        self.checkBox.setObjectName("checkBox")
        self.gridLayout_2.addWidget(self.checkBox, 0, 2, 1, 1)
        self.btn_db_dir = QtWidgets.QPushButton(Dialog)
        self.btn_db_dir.setMinimumSize(QtCore.QSize(0, 40))
        self.btn_db_dir.setObjectName("btn_db_dir")
        self.gridLayout_2.addWidget(self.btn_db_dir, 1, 1, 1, 1)
        self.checkBox_2 = QtWidgets.QCheckBox(Dialog)
        self.checkBox_2.setText("")
        self.checkBox_2.setObjectName("checkBox_2")
        self.gridLayout_2.addWidget(self.checkBox_2, 1, 2, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_2)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.btn_start = QtWidgets.QPushButton(Dialog)
        self.btn_start.setMinimumSize(QtCore.QSize(0, 40))
        self.btn_start.setMaximumSize(QtCore.QSize(100, 16777215))
        self.btn_start.setObjectName("btn_start")
        self.horizontalLayout_2.addWidget(self.btn_start)
        self.label_tip = QtWidgets.QLabel(Dialog)
        self.label_tip.setObjectName("label_tip")
        self.horizontalLayout_2.addWidget(self.label_tip)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem5)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_ready = QtWidgets.QLabel(Dialog)
        self.label_ready.setObjectName("label_ready")
        self.horizontalLayout.addWidget(self.label_ready)
        self.progressBar = QtWidgets.QProgressBar(Dialog)
        self.progressBar.setProperty("value", 50)
        self.progressBar.setObjectName("progressBar")
        self.horizontalLayout.addWidget(self.progressBar)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem6)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem7)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.btn_help.setText(_translate("Dialog", "使用说明"))
        self.label_3.setText(_translate("Dialog", "解密数据库"))
        self.label_9.setText(_translate("Dialog", "以下内容为自动获取，如获取失败请手动填写"))
        self.label_7.setText(_translate("Dialog", "版本"))
        self.label_5.setText(_translate("Dialog", "微信昵称"))
        self.label_6.setText(_translate("Dialog", "密钥"))
        self.label.setText(_translate("Dialog", "PID"))
        self.label_2.setText(_translate("Dialog", "手机号"))
        self.label_4.setText(_translate("Dialog", "wxid"))
        self.label_8.setText(_translate("Dialog", "微信路径"))
        self.btn_getinfo.setText(_translate("Dialog", "获取信息"))
        self.btn_db_dir.setText(_translate("Dialog", "设置微信路径"))
        self.btn_start.setText(_translate("Dialog", "开始启动"))
        self.label_tip.setText(_translate("Dialog", "TextLabel"))
        self.label_ready.setText(_translate("Dialog", "未就绪"))
