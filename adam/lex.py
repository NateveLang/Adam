import adam.grammar as gr
import adam.templates as temp
import adam.translation as tr
from adam.token import Tokens, get_token_ID
from adam.error import LexicalError
from adam.utils import tostring

F = False

def scanner(text = "", args = ["none"]):
	dev_mode = "dev" in args

	tp = temp.Template("english")
	templates = [tp]

	commentary, string, name, number, float = F, F, F, F, F
	matrix, vector, operator = F, F, F
	using, including, docstring, waiting_close_bracket =  F, F, 0, 0

	tokens = Tokens()
	modules = []
	errors = 0
	line, pos = 1, 1

	lexema = ""
	string_ch = ""

	security_tokens = "\n ~eof tokens for security~ ~including the \n, DO NOT REMOVE THE EXTRA \n~"
	text = security_tokens + text + "\npass\n" + security_tokens
	
	i = 0
	while i < len(text):

		ch = text[i]

		tokens_num = len(tokens)

		if tokens_num > 0:
			last_line = tokens[tokens_num - 1][4]

		if docstring > 0 and ch != string_ch:
			lexema += ch

		elif ch == tp.matrices:
				
			if matrix:
				tokens.add(lexema, gr.MATRIX, line, pos, last_line)
				lexema = ""
				matrix = F
			else:
				matrix = True

		elif ch == "\n":

			if string:

				if using:
					tp = None
					tp = temp.Template(lexema)

					if tp not in templates:
						templates += [tp]

					using = F

				elif including:
					modules.append(lexema)
					including = F
					
				else:
					tokens.add(lexema, gr.STRING, line, pos)
					
				lexema = ""
				string_ch = ""
				string = F
			
			elif vector:
				tokens.add(lexema, gr.VECTOR, line, pos, last_line)
				lexema = ""
				waiting_close_bracket = 0
				vector = F

			elif number:

				if float:
					tokens.add(lexema + "0", gr.FLOAT, line, pos, last_line)
				else:
					tokens.add(lexema, gr.INT, line, pos, last_line)

				number = F
				float = F
			
			elif name:
				lexema, errors = tr.translate(lexema, errors, tp)
				
				if lexema == gr.USE:
					using = True
				elif lexema == gr.INCLUDE:
					including = True
				else:
					tokens.add(lexema, get_token_ID(lexema), line, pos)

				name = F
				
			elif operator:
				id = get_token_ID(lexema)

				if id == gr.identifier:

					for lex in lexema:
						tokens.add(lex, get_token_ID(lex), line, pos, last_line)

				else:
					tokens.add(lexema, id, line, pos, last_line)
				
				operator = F

			if matrix:
				lexema += ch

			else:
				lexema = ""

			line += 1
			pos = 1

		elif docstring > 0 and ch == string_ch:
			docstring -= 1

			if docstring == 0:
				tokens.add(lexema, gr.DOCSTRING, line, pos)
				string_ch = ""
				lexema = ""

		elif commentary and ch not in tp.commentaries:
			pass

		elif commentary and ch in tp.commentaries:
			commentary = F

		elif vector:
			lexema += ch

			if ch == tp.vectors[1]:
				waiting_close_bracket -=1

				if waiting_close_bracket == 0:
					tokens.add(lexema, gr.VECTOR, line, pos, last_line)
					lexema = ""
					vector = F

		elif matrix:
			lexema += ch

		elif string and ch not in tp.strings:
			lexema += ch

		elif string and ch == string_ch:

			if text[i + 1] == string_ch:
				docstring = 3
				i += 1

			else:
					
				if using:
					tp = None
					tp = temp.Template(lexema)
					
					if tp not in templates:
						templates += [tp]
					
					using = F

				elif including:
					modules.append(lexema)
					including = F

				else:
					tokens.add(lexema, gr.STRING, line, pos)

				lexema = ""
				string_ch = ""
			
			string = F
		
		elif float and ch in tp.digits:
			lexema += ch

		elif float and ch in tp.floating:
			errors += LexicalError(line, f"two {gr.floating} in float definition")
			break

		elif number and not float and ch in (tp.digits + tp.floating):
			lexema += ch

			if ch in tp.floating:
				float = True

		elif number and ch not in (tp.digits + tp.floating):

			if float:
				tokens.add(lexema + "0", gr.FLOAT, line, pos, last_line)
			else:
				tokens.add(lexema, gr.INT, line, pos, last_line)

			lexema = ""
			i -= 1
			pos -= 1
			number, float = F, F
		
		elif name and ch in tp.alphanum:
			lexema += ch

		elif name and ch not in tp.alphanum:
			lexema, errors = tr.translate(lexema, errors, tp)

			if lexema == gr.USE:
				using = True
			elif lexema == gr.INCLUDE:
				including = True
			else:
				tokens.add(lexema, get_token_ID(lexema), line, pos)

			lexema = ""
			i -= 1
			pos -= 1
			name = F
		
		elif operator and ch in tp.operators:
			lexema += ch

		elif operator and ch not in tp.operators:
			id = get_token_ID(lexema)

			if id == gr.identifier:
				for lex in lexema:
					tokens.add(lex, get_token_ID(lex), line, pos, last_line)
			else:
				tokens.add(lexema, id, line, pos, last_line)

			lexema = ""
			i -= 1
			pos -= 1
			operator = F

		elif not commentary and ch in tp.commentaries:
			commentary = True

		elif not string and ch in tp.strings:
			string = True
			string_ch = ch

		elif not vector and ch == tp.vectors[0]:
			vector = True
			lexema += ch
			waiting_close_bracket += 1

		elif not name and ch in tp.alphabet:
			name = True
			lexema += ch

		elif not name and not number and ch in tp.digits:
			number = True
			lexema += ch

		elif not name and not number and not operator and ch in tp.operators:
			operator = True
			lexema += ch

		elif ch not in tp.blanks:
			tokens.add(ch, ch, line, pos)
		
		i += 1
		pos += 1

	if errors > 0:
		print("Traceback:", tokens)

	tokens.set_last_line(line, pos)

	log = ""

	if dev_mode:
		log += f"Last line: {line} Last column: {pos}\n"
		log += f"Tokens detected: {len(tokens)}\n"

		names = tokens.get_names()
		string_of_names = tostring(names, ", ")
		log += f"Names detected ({len(names)}): {string_of_names}\n"

	return tokens, errors, log, templates, modules
