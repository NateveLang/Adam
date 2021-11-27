import importlib as imp

from adam.error import NotSupportedLanguageError, NotFoundError
from adam.grammar import transpiler_name

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

		except ModuleNotFoundError:
			self.errors += NotSupportedLanguageError(None, f"Language '{self.language_name}' is not supported yet. Please make sure the language template exists in the embedding location")

		except ImportError:
			self.errors += NotFoundError(None, f"Some language variables are missing. Check the '/{transpiler_name}/embedding/{self.language_name}.*' files")

		return result

	def build(self, code, *args):

		text = "# Embedding code build failed"

		def main(self, lang):
			return lang._build(code, *args)

		text = self.execute_with_module(main)

		return text

