import importlib as imp

from adam.error import NotSupportedLanguageError, NotFoundError
from adam.grammar import transpiler_name

class Language():
	def __init__(self, name = "nqs"):
		self.language_name = name
		self.errors = 0

		module_name = "adam.embedding." + self.language_name

		try:
			# from adam.embedding.{language_name} import *
			lang = imp.import_module(module_name)
			
			self.author  = lang._author
			self.build = lang._build
			self.required_data = lang._required_data

		except ModuleNotFoundError:
			self.errors += NotSupportedLanguageError(None, f"Language '{self.language_name}' is not supported yet. Please make sure the language template exists in the embedding location")

		except ImportError:
			self.errors += NotFoundError(None, f"Some language variables are missing. Check the '/{transpiler_name}/embedding/{self.language_name}.*' files")