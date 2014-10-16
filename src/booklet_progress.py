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

import commands
import errno

from os.path import isdir
from os.path import expanduser
from os import makedirs
from PyQt4 import QtCore

# This class is responsible for the creation of the booklet.
# It performs all the necessary steps while notifying the gui
# of the current state.
class BookletProgress(QtCore.QThread):
	procDone = QtCore.pyqtSignal(bool)
	partDone = QtCore.pyqtSignal(int)

	# This method receives the input and output name and it creates
	# the hidden directory for temporary files.
	# 
	# Parameters:
	# - source: The input pdf file.
	# - target: The output pdf file which is usually in the home directory.
	def set_values(self, source, target):
		self.source = source
		self.target = target
		self.home = expanduser("~") + '/.booklet'
		if not isdir(self.home):
			self.mkdir_p(self.home)

	# It creates a directory.
	#
	# Parameters:
	# - The path to be created. If the path already exists, it will supress 
	# the exception.
	def mkdir_p(self, path):
		try:
			makedirs(path)
		except OSError as exc:  # Python >2.5
			if exc.errno == errno.EEXIST and isdir(path):
				pass
			else: raise

	# It creates the name of the temporary file as a Postscript. 
	def create_folder_name(self):
		temp = '%s/temp.ps' % self.home
		return temp

	# Creating the Postscript.
	#
	# Parameters:
	# - temp: the temporary postcript file representing the input.
	def pdftops(self, temp):
		commands.getoutput('pdftops %s %s' % (self.source, temp))

	# Rearranging pages using psbook.
	#
	# Parameters:
	# - temp: the temporary file created by pdftops.
	def psbook(self, temp):
		temp1 = self.home + '/temp1.ps'
		commands.getoutput('psbook %s %s' % (temp, temp1))
		return temp1

	# Preparing multiple logical pages per sheet of paper.
	def psnup(self, temp, temp1):
		commands.getoutput('psnup -2 %s %s' % (temp1, temp))

	# The actual booklet creation.
	def pstops(self, temp, temp1):
		booklet = 'pstops "2:0@1.0(-0.00cm,0.0cm),1U@1.0(21cm,29.7cm)" %s %s' % (temp, temp1)
		commands.getoutput(booklet)
	
	# It converts back the ps to pdf.
	def ps2pdf(self, temp, temp1):
		commands.getoutput('ps2pdf %s %s' % (temp, self.target))

	# The main method run which calls each step necessary until the booklet is 
	# created. 
	def run(self):
		self.partDone.emit(16)
		temp = self.create_folder_name()
		self.partDone.emit(32)
		self.pdftops(temp)
		self.partDone.emit(48)
		temp1 = self.psbook(temp)
		self.partDone.emit(64)
		self.psnup(temp, temp1)
		self.partDone.emit(70)
		self.pstops(temp, temp1)
		self.partDone.emit(86)
		self.ps2pdf(temp1, self.target)
		self.partDone.emit(100)
		self.procDone.emit(True)   

