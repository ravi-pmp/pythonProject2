import re

my_string = input( "enter a string" )
pattern = re.compile( r'[0-9]+' )
result = pattern.sub( "_", my_string )
print( result )

\

def split_in_columns(message=message):
    """Split the message by newline (\n) and join it together on '|'
       (pipe), return the obtained output string"""
    for line in message.split("\n"):
        line.join('|')
        print(line)
