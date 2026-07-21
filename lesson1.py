
#! When providing a file to the Python Interpreter, always put the path to the file in quotes

#* These are STATEMENTS. A statement is a complete instruction. They can be simple or complex
print('hello python')
print(23 - 5)

#* adding a line between statements for readbility
print('')

#* This line throws this error: SyntaxError: unterminated string literal
# print('Python is a high-level programming language. It is used for web development, data analysis, artificial intelligence, scientific computing, and more. I'm learning Python to leverage it within the SharePoint ecosystem, so I can build custom solutions for my department and org.')

#! The python interpreter will fail if it encounters an error. The file will not be executed at all

#* Adding three quotes fixes the error
print('''Python is a high-level programming language. It is used for web development, data analysis, artificial intelligence, scientific computing, and more. I'm learning Python to leverage it within the SharePoint ecosystem, so I can build custom solutions for my department and org.''')

print('')

#* New lines can be added to a string by using the escape sequence \n
print('''Python is a high-level programming language. It is used for web development, data analysis, artificial intelligence, scientific computing, and more.\nI'm learning Python to leverage it within the SharePoint ecosystem, so I can build custom solutions for my department and org.\n''')

#* Four spaces (tab) can be added to a string by using the escape sequence \t
print('The next word\tis four spaces away from the previous word.\n')

#* Variables are used to store data. They can be assigned values using the assignment operator
#* Variable names can contain letters, numbers, and underscores. They cannot start with a number. They are case-sensitive
lang = "python"

print(lang)
print('')

id = 100
name = 'Idris'

print(id, lang, name)
print('')

print('Language =',lang, '\nName =',name, '\nSuccess rate =',id)
print('')