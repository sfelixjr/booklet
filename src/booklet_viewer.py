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

from booklet_handler import BookletHandler
from booklet_about import Ui_About
from os.path import expanduser
from popplerqt4 import Poppler
from PyQt4.QtCore import Qt
from PyQt4.QtGui import QDialog
from PyQt4.QtGui import QFileDialog
from PyQt4.QtGui import QIntValidator
from PyQt4.QtGui import QPixmap
from PyQt4.QtGui import QPrintPreviewDialog
from shutil import copyfile

# This class is responsible for rendering the PDF inside the Qt Gui.
# It also triggers the methods for opening and saving the pdfs.
class BookletViewer(object):

	# Default constructor initializes the page number zero and creates
	# the hidden home directory where we will store temporary files.
	#
	# Parameters:
	#
	# - window: The main window created by Qt Designer.
	def __init__(self, window):
		self.window = window
		self.page_number = 0
		self.img = None
		self.home = '%s/.booklet' % expanduser("~")
		self.output_pdf = None
		self.n_pages = -1

	# We connect with poppler to render the pdf.
	#
	# Parameters:
	#
	# - filename: The booklet file generated to be rendered for the user.
	# - page_number: Poppler will load only this page of the PDF.
	def pdf_view(self, filename, page_number):
		doc = Poppler.Document.load(filename)
		doc.setRenderHint(Poppler.Document.Antialiasing)
		doc.setRenderHint(Poppler.Document.TextAntialiasing)

		self.page = doc.page(self.page_number)
		self.n_pages = doc.numPages()
		image = self.page.renderToImage(200,200)
		self.window.actionPageNumber.setValidator(QIntValidator(0, self.n_pages))
		self.img = QPixmap.fromImage(image)
		self.window.label.setPixmap(self.img)
		self.window.label.setMinimumSize(640, 420)
		self.onResize(None)
		self.update_number()

	# Shows the credits for this application. My Name! Yey!
	def open_about(self):
		dialog = QDialog()
		about_dialog = Ui_About()
		about_dialog.setupUi(dialog)
		dialog.exec_()

	# We open the pdf and starts the conversion process.
	def open_pdf(self):
		input_pdf = QFileDialog.getOpenFileName(None,'Open PDF File',expanduser("~"),'*.pdf')
		if input_pdf == '':
			return
		self.output_pdf = '%s/temporary.pdf' % self.home
		BookletHandler(input_pdf,self.output_pdf)
		self.pdf_view(self.output_pdf, self.page_number)
		# Toggling buttons
		self.window.actionSave.setEnabled(True)
		self.window.actionFirst.setEnabled(True)
		self.window.actionPrevious.setEnabled(True)
		self.window.actionNext.setEnabled(True)
		self.window.actionLast.setEnabled(True)
		self.window.actionPageNumber.setEnabled(True)
		
	# Update the number shown in the gui.
	def update_number(self):
		self.window.actionPageNumber.setText(str(self.page_number+1))

	# Render the first page.
	def go_first(self):
		self.window.actionPrevious.setEnabled(False)
		self.window.actionFirst.setEnabled(False)
		self.window.actionNext.setEnabled(True)
		self.window.actionLast.setEnabled(True)
		self.page_number = 0
		self.pdf_view(self.output_pdf, self.page_number)

	# Render the last page.
	def go_last(self):
		self.window.actionNext.setEnabled(False)
		self.window.actionLast.setEnabled(False)
		self.window.actionFirst.setEnabled(True)
		self.window.actionPrevious.setEnabled(True)		
		self.page_number = self.n_pages - 1
		self.pdf_view(self.output_pdf, self.page_number)	

	# Render the next page.
	def go_next(self):
		if (self.page_number >= self.n_pages - 2):
			self.window.actionNext.setEnabled(False)
			self.window.actionLast.setEnabled(False)
		else:
			self.window.actionNext.setEnabled(True)
			self.window.actionLast.setEnabled(True)
		self.window.actionFirst.setEnabled(True)
		self.window.actionPrevious.setEnabled(True)			
		self.page_number += 1
		self.pdf_view(self.output_pdf, self.page_number)

	# Render the previous page.
	def go_previous(self):
		if (self.page_number <= 1):
			self.window.actionPrevious.setEnabled(False)
			self.window.actionFirst.setEnabled(False)
		else:
			self.window.actionPrevious.setEnabled(True)
			self.window.actionFirst.setEnabled(True)
		self.window.actionNext.setEnabled(True)
		self.window.actionLast.setEnabled(True)
		self.page_number -= 1
		self.pdf_view(self.output_pdf, self.page_number)

	# We save the booklet generated.
	def save_pdf(self):
		to_be_copied = QFileDialog.getSaveFileName(None,'Output PDF File',expanduser("~"),'*.pdf')
		if to_be_copied == '':
			return
		if self.output_pdf != None:
			copyfile(self.output_pdf,to_be_copied)

	# Printing is still not available
	def print_pdf(self):
		dialog = QPrintPreviewDialog()
		dialog.exec_()

	# We resize the PDF image shown 
	def onResize(self,event):
		if self.page_number == None or self.img == None:
			return
		lw = self.window.label.width()
		lh = self.window.label.height()
		newimg = self.img.scaled(lw,lh, Qt.KeepAspectRatio)
		self.window.label.setPixmap(newimg)
