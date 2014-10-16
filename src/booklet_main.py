# Copyright 2014 - Samuel de Sousa (felixjr.org)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from booklet_gui import Ui_Booklet
from booklet_viewer import BookletViewer
from PyQt4.QtGui import QApplication
from PyQt4.QtGui import QMainWindow
from PyQt4.QtGui import QDesktopWidget
from signal import SIGINT
from signal import SIG_DFL
from signal import signal
from sys import argv
from sys import exit

if __name__ == "__main__":
	# The following command allows the user to kill the app with crtl-c.
	signal(SIGINT, SIG_DFL)

	# Creating the Gui
	app = QApplication(argv)
	main_window = QMainWindow()
	screen = QDesktopWidget().screenGeometry(1)
	ui = Ui_Booklet()
	ui.setupUi(main_window)

	# Adjusting to the middle of the screen.
	main_window.move(screen.center() - main_window.frameGeometry().center())
	viewer = BookletViewer(ui)

	# Connecting Signals and Slots.
	ui.actionOpen.triggered.connect(viewer.open_pdf)
	ui.actionSave.triggered.connect(viewer.save_pdf)
	ui.actionPrint.triggered.connect(viewer.print_pdf)
	ui.actionAbout.triggered.connect(viewer.open_about)
	ui.actionFirst.triggered.connect(viewer.go_first)
	ui.actionNext.triggered.connect(viewer.go_next)
	ui.actionPrevious.triggered.connect(viewer.go_previous)
	ui.actionLast.triggered.connect(viewer.go_last)

	# Running the Application.
	main_window.resizeEvent = viewer.onResize
	main_window.show()
	exit(app.exec_())
