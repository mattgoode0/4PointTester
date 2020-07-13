# This Python file uses the following encoding: utf-8

import sys
import KeithleyInterface  # Code to talk to Keitley
from os.path import abspath, dirname, join

from PySide2.QtCore import QObject, Slot
from PySide2.QtGui import QGuiApplication
from PySide2.QtQml import QQmlApplicationEngine


class Bridge(QObject):

    # start test after it has been setup
    @Slot(str, str, str, str, str, str, str, str, result=str)
    def start_test(self, name, startV, endV, steps, wait, mode, units, sweep_type):
        print(name, startV, endV, steps, wait, mode, units, sweep_type)

        KeithleyInterface.FourPointProbe(name, startV, endV, steps, wait, mode, units, sweep_type)
        return ("Test Complete")


if __name__ == '__main__':
    app = QGuiApplication(sys.argv)
    engine = QQmlApplicationEngine()

    # Instance of the Python object
    bridge = Bridge()

    # Expose the Python object to QML
    context = engine.rootContext()
    context.setContextProperty("con", bridge)

    # Get the path of the current directory, and then add the name
    # of the QML file, to load it.
    qmlFile = join(dirname(__file__), 'gui.qml')
    engine.load(abspath(qmlFile))

    if not engine.rootObjects():
        sys.exit(-1)

    sys.exit(app.exec_())
