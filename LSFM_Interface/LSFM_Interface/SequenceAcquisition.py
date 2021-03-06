# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SequenceAcquisitionModalDialog.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import Controller


class Ui_Dialog(object):


    def __init__(self, listOfCameras,listOfPositionsFocusUp, listOfPositionsFocuDown):
        self.cameraValues = listOfCameras
        self.listOfPositionsFocusUp = listOfPositionsFocusUp
        self.listOfPositionsFocuDown  = listOfPositionsFocuDown
        self._want_to_close = False





    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(300, 500)
        Dialog.setMaximumSize(QtCore.QSize(300, 500))
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.CameraSelector = QtWidgets.QFrame(Dialog)
        self.CameraSelector.setMinimumSize(QtCore.QSize(0, 20))
        self.CameraSelector.setMaximumSize(QtCore.QSize(16777215, 20))
        self.CameraSelector.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.CameraSelector.setFrameShadow(QtWidgets.QFrame.Raised)
        self.CameraSelector.setObjectName("CameraSelector")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.CameraSelector)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.camera = QtWidgets.QLabel(self.CameraSelector)
        self.camera.setObjectName("camera")
        self.horizontalLayout_6.addWidget(self.camera, 0, QtCore.Qt.AlignHCenter)
        self.cameraList = QtWidgets.QComboBox(self.CameraSelector)
        self.cameraList.setObjectName("cameraList")
        self.horizontalLayout_6.addWidget(self.cameraList)
        self.verticalLayout.addWidget(self.CameraSelector)
        self.FocusUp_Frame = QtWidgets.QFrame(Dialog)
        self.FocusUp_Frame.setMinimumSize(QtCore.QSize(0, 20))
        self.FocusUp_Frame.setMaximumSize(QtCore.QSize(16777215, 20))
        self.FocusUp_Frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.FocusUp_Frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.FocusUp_Frame.setObjectName("FocusUp_Frame")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.FocusUp_Frame)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.FocusUp_label = QtWidgets.QLabel(self.FocusUp_Frame)
        self.FocusUp_label.setObjectName("FocusUp_label")
        self.horizontalLayout_7.addWidget(self.FocusUp_label, 0, QtCore.Qt.AlignHCenter)
        self.focusUp_value = QtWidgets.QDoubleSpinBox(self.FocusUp_Frame)
        self.focusUp_value.setObjectName("focusUp_value")
        self.horizontalLayout_7.addWidget(self.focusUp_value)
        self.verticalLayout.addWidget(self.FocusUp_Frame)
        self.FocusDown_Frame = QtWidgets.QFrame(Dialog)
        self.FocusDown_Frame.setMinimumSize(QtCore.QSize(0, 20))
        self.FocusDown_Frame.setMaximumSize(QtCore.QSize(16777215, 20))
        self.FocusDown_Frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.FocusDown_Frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.FocusDown_Frame.setObjectName("FocusDown_Frame")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.FocusDown_Frame)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.focusDown_label = QtWidgets.QLabel(self.FocusDown_Frame)
        self.focusDown_label.setObjectName("focusDown_label")
        self.horizontalLayout_8.addWidget(self.focusDown_label, 0, QtCore.Qt.AlignHCenter)
        self.focusDown_value = QtWidgets.QDoubleSpinBox(self.FocusDown_Frame)
        self.focusDown_value.setObjectName("focusDown_value")
        self.horizontalLayout_8.addWidget(self.focusDown_value)
        self.verticalLayout.addWidget(self.FocusDown_Frame)
        self.Z_UP_Frame = QtWidgets.QFrame(Dialog)
        self.Z_UP_Frame.setMinimumSize(QtCore.QSize(0, 20))
        self.Z_UP_Frame.setMaximumSize(QtCore.QSize(16777215, 20))
        self.Z_UP_Frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.Z_UP_Frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Z_UP_Frame.setObjectName("Z_UP_Frame")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.Z_UP_Frame)
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.Z_UPLabel = QtWidgets.QLabel(self.Z_UP_Frame)
        self.Z_UPLabel.setObjectName("Z_UPLabel")
        self.horizontalLayout_9.addWidget(self.Z_UPLabel, 0, QtCore.Qt.AlignHCenter)
        self.ZUP_value = QtWidgets.QDoubleSpinBox(self.Z_UP_Frame)
        self.ZUP_value.setObjectName("ZUP_value")
        self.horizontalLayout_9.addWidget(self.ZUP_value)
        self.verticalLayout.addWidget(self.Z_UP_Frame)
        self.Z_Down_Frame = QtWidgets.QFrame(Dialog)
        self.Z_Down_Frame.setMinimumSize(QtCore.QSize(0, 20))
        self.Z_Down_Frame.setMaximumSize(QtCore.QSize(16777215, 20))
        self.Z_Down_Frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.Z_Down_Frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Z_Down_Frame.setObjectName("Z_Down_Frame")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.Z_Down_Frame)
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.ZDownLabel = QtWidgets.QLabel(self.Z_Down_Frame)
        self.ZDownLabel.setObjectName("ZDownLabel")
        self.horizontalLayout_10.addWidget(self.ZDownLabel, 0, QtCore.Qt.AlignHCenter)
        self.ZDown_Value = QtWidgets.QDoubleSpinBox(self.Z_Down_Frame)
        self.ZDown_Value.setObjectName("ZDown_Value")
        self.horizontalLayout_10.addWidget(self.ZDown_Value)
        self.verticalLayout.addWidget(self.Z_Down_Frame)
        self.XRichtung_Frame = QtWidgets.QFrame(Dialog)
        self.XRichtung_Frame.setMinimumSize(QtCore.QSize(0, 20))
        self.XRichtung_Frame.setMaximumSize(QtCore.QSize(16777215, 20))
        self.XRichtung_Frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.XRichtung_Frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.XRichtung_Frame.setObjectName("XRichtung_Frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.XRichtung_Frame)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.xRichtunh = QtWidgets.QLabel(self.XRichtung_Frame)
        self.xRichtunh.setObjectName("xRichtunh")
        self.horizontalLayout.addWidget(self.xRichtunh, 0, QtCore.Qt.AlignHCenter)
        self.xValue = QtWidgets.QDoubleSpinBox(self.XRichtung_Frame)
        self.xValue.setObjectName("xValue")
        self.horizontalLayout.addWidget(self.xValue)
        self.verticalLayout.addWidget(self.XRichtung_Frame)
        self.YRichtung_Frame = QtWidgets.QFrame(Dialog)
        self.YRichtung_Frame.setMinimumSize(QtCore.QSize(0, 20))
        self.YRichtung_Frame.setMaximumSize(QtCore.QSize(16777215, 20))
        self.YRichtung_Frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.YRichtung_Frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.YRichtung_Frame.setObjectName("YRichtung_Frame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.YRichtung_Frame)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.yRichtung = QtWidgets.QLabel(self.YRichtung_Frame)
        self.yRichtung.setObjectName("yRichtung")
        self.horizontalLayout_2.addWidget(self.yRichtung, 0, QtCore.Qt.AlignHCenter)
        self.yValue = QtWidgets.QDoubleSpinBox(self.YRichtung_Frame)
        self.yValue.setObjectName("yValue")
        self.horizontalLayout_2.addWidget(self.yValue)
        self.verticalLayout.addWidget(self.YRichtung_Frame)
        self.dz_Frame = QtWidgets.QFrame(Dialog)
        self.dz_Frame.setMinimumSize(QtCore.QSize(0, 20))
        self.dz_Frame.setMaximumSize(QtCore.QSize(16777215, 20))
        self.dz_Frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.dz_Frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.dz_Frame.setObjectName("dz_Frame")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.dz_Frame)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.dz = QtWidgets.QLabel(self.dz_Frame)
        self.dz.setObjectName("dz")
        self.horizontalLayout_3.addWidget(self.dz, 0, QtCore.Qt.AlignHCenter)
        self.dz_Value = QtWidgets.QDoubleSpinBox(self.dz_Frame)

        self.dz_Value.setObjectName("dz_Value")
        self.horizontalLayout_3.addWidget(self.dz_Value)
        self.verticalLayout.addWidget(self.dz_Frame)
        self.ImageNumberFrame = QtWidgets.QFrame(Dialog)
        self.ImageNumberFrame.setMinimumSize(QtCore.QSize(0, 20))
        self.ImageNumberFrame.setMaximumSize(QtCore.QSize(16777215, 20))
        self.ImageNumberFrame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.ImageNumberFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.ImageNumberFrame.setObjectName("ImageNumberFrame")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.ImageNumberFrame)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.ImageNumber = QtWidgets.QLabel(self.ImageNumberFrame)
        self.ImageNumber.setObjectName("ImageNumber")
        self.horizontalLayout_4.addWidget(self.ImageNumber, 0, QtCore.Qt.AlignHCenter)
        self.image_value = QtWidgets.QDoubleSpinBox(self.ImageNumberFrame)
        self.image_value.setObjectName("image_value")
        self.horizontalLayout_4.addWidget(self.image_value)
        self.verticalLayout.addWidget(self.ImageNumberFrame)
        self.LaserFrame = QtWidgets.QFrame(Dialog)
        self.LaserFrame.setMinimumSize(QtCore.QSize(0, 20))
        self.LaserFrame.setMaximumSize(QtCore.QSize(16777215, 20))
        self.LaserFrame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.LaserFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.LaserFrame.setObjectName("LaserFrame")
        self.fastForward = QtWidgets.QRadioButton(self.LaserFrame)
        self.fastForward.setGeometry(QtCore.QRect(20, 0, 231, 20))
        self.fastForward.setObjectName("fastForward")
        self.verticalLayout.addWidget(self.LaserFrame)
        self.move_Z_up = QtWidgets.QPushButton(Dialog)
        self.move_Z_up.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.move_Z_up)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        self.move_Z_up.clicked.connect(lambda : self.Move_to_Z_UP())
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        for camera in self.cameraValues:
            self.cameraList.addItem(camera)

        self.xValue.setRange(0, 75)
        self.xValue.setValue(self.listOfPositionsFocusUp["X Controller"])
        self.xValue.setSingleStep(0.5)
        self.yValue.setRange(0, 75)
        self.yValue.setValue(self.listOfPositionsFocusUp["Y Controller"])
        self.yValue.setSingleStep(0.5)
        self.focusDown_value.setRange(0, 75)
        self.focusDown_value.setSingleStep(0.05)
        self.focusDown_value.setValue(self.listOfPositionsFocuDown['Focus Controller'])
        print(self.listOfPositionsFocusUp)
        print(self.listOfPositionsFocuDown)

        self.focusUp_value.setRange(0, 75)
        self.focusUp_value.setValue(self.listOfPositionsFocusUp['Focus Controller'])
        self.focusUp_value.setSingleStep(0.05)
        self.ZUP_value.setRange(-5,5)
        self.ZUP_value.setSingleStep(0.05)
        self.ZUP_value.setValue(self.listOfPositionsFocusUp["Z Controller"])
        self.ZDown_Value.setRange(-5,5)
        self.ZDown_Value.setSingleStep(0.05)
        self.ZDown_Value.setValue(self.listOfPositionsFocuDown["Z Controller"])
        self.image_value.setSingleStep(1)
        self.image_value.setRange(0, 1000)
        self.dz_Value.setValue(10.00)

        imageCount = int(abs((self.ZUP_value.value() - self.ZDown_Value.value()))*100)

        if(imageCount > 0):
            self.image_value.setValue(imageCount)

    def Move_to_Z_UP(self):
        Controller.MoveAbsolut(2, self.ZUP_value.value(), 0)
        Controller.MoveAbsolut(3, self.focusUp_value.value(), 0)


    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.camera.setText(_translate("Dialog", "Camera"))
        self.FocusUp_label.setText(_translate("Dialog", "Focus Up "))
        self.focusDown_label.setText(_translate("Dialog", "Focus Down "))
        self.Z_UPLabel.setText(_translate("Dialog", "Z _ Up "))
        self.ZDownLabel.setText(_translate("Dialog", "Z _ Down "))
        self.xRichtunh.setText(_translate("Dialog", "x Richtung "))
        self.yRichtung.setText(_translate("Dialog", "Y Richtung "))
        self.dz.setText(_translate("Dialog", "dZ in micrometer "))
        self.ImageNumber.setText(_translate("Dialog", "Anzahl Bilder"))
        self.fastForward.setText(_translate("Dialog", "With Fast Forward (Acquisition will be Delete!!)"))
        self.move_Z_up.setText(_translate("Dialog", "Move first to Z_Up"))


