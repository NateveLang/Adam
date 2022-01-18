author = "eanorambuena"
author_email = "eanorambuena@uc.cl"

#	MIT License
#	
#	Copyright (c) 2021 Emmanuel Norambuena Sepulveda
#	
#	Permission is hereby granted, free of charge, to any person obtaining a copy
#	of this software and associated documentation files (the "Software"), to deal
#	in the Software without restriction, including without limitation the rights
#	to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#	copies of the Software, and to permit persons to whom the Software is
#	furnished to do so, subject to the following conditions:

#	The above copyright notice and this permission notice shall be included in all
#	copies or substantial portions of the Software.
#	
#	THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#	IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#	FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#	AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#	LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#	OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#	SOFTWARE.

import importlib as imp

from adam.error import		NotFoundError, NotSupportedLanguageError
from adam.grammar import	transpiler_name

def void(x):
    pass

class Language():
	def __init__(self, name = "nqs"):
		self.language_name = name
		self.errors = 0
		self.module_name = "adam.embedding." + self.language_name

		def main(self, lang):
			self.author  = lang._author
			self.required_data = lang._required_data

		self.execute_with_module(main)

	def execute_with_module(self, function = void):
    	
		result = "Execution output is None"

		try:
			# from adam.embedding.{language_name} import *
			lang = imp.import_module(self.module_name)

			result = function(self, lang)

		except ImportError:
			self.errors += NotFoundError(None, f"Some language variables are missing. Check the '/{transpiler_name}/embedding/{self.language_name}.*' files")
			
		except ModuleNotFoundError:
			self.errors += NotSupportedLanguageError(None, f"Language '{self.language_name}' is not supported yet. Please make sure the language template exists in the embedding location")

		return result

	def build(self, code, *args):

		text = "# Embedding code build failed"

		def main(self, lang):
			return lang._build(code, *args)

		text = self.execute_with_module(main)

		return text
