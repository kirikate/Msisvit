types: str = r"(?:int|char|float|double|bool|long|long long|short|size_t|void|long double|string|unsigned long long|void|unsigned char|signed char)"

variable: str = r'(?:const)?' + types + r'\s*\**\s*(\w+)\s*(=\s*[^;])?;'
func: str = types + r'\s+(\w+)\s*\((?:' + variable + ',?)*\)'

operators: list = [r'(?<!\+)\+(?![\+=])',
                   r'(?<![\+\-\*/&\|\^!])=',
                   r'\+=',
                   r'(?<!-)-(?!-)(?![=\-])',
                   r'-=',
                   r'--',
                   r'\+\+',
                   r'/(?!=)',
                   r'/=',
                   r'\*(?!=)',
                   r'\*=',
                   r'(?<!<)<(?![<=])',
                   r'(?<!>)>(?![>=])',
                   r'!=',
                   r'(?<!=)==(?!=)'
                   r';',
                   r'&&',
                   r'(?<!\|)\|(?![\|=])',
                   r'\|\|',
                   r'(?<!&)&(?![&=])',
                   r'\\',
                   r'\^(?!=)',
                   r'\^=',
                   r'for',
                   r'while',
                   r'>=',
                   r'<=',
                   r'if',
                   r'(?<!cout )<<',
                   r'(?<!cin )>>',
                   r'&=']
cout: str = r'(?:std::\s*)?cout(?:\s*<<\s*\w+)+'
cin: str = r'(?:std::\s*)?cin(?:\s*>>\s*\w+)+'
brackets: str = r'(?:(?<!\w)\(|{)'
include: str = r'#include \s*(<|")([^>"]+)([>"])'

string_literal: str = r'"(?:[^"]|(?<=\\)")*"'
numb_literal: str = r'\d+(?:\.\d+)?'
char_literal: str = r"'..?'"
