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

from booklet_progress import BookletProgress
from booklet_progress_gui import Ui_Dialog
from PyQt4.QtGui import QDialog

# A class to update the progress bar shown to the user.
class BookletHandler():
	def __init__(self, source, target):
		self.dialog = QDialog()
		self.progress = Ui_Dialog()
		self.progress.setupUi(self.dialog)
		self.thread = BookletProgress()
		self.thread.set_values(source, target)
		self.thread.partDone.connect(self.update)
		self.thread.procDone.connect(self.finish)
		self.thread.start()
		self.dialog.exec_()

	# It updates the progress bar.
	#
	# Parameters:
	# -val: the progress value, e.g. 26%.
	def update(self, val):
		self.progress.progressBar.setValue(val)   

	# Called when the process is done in order to close 
	# the Dialog.
	def finish(self):
		self.dialog.close()
