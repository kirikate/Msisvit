types: str = r"(?:int|char|float|double|bool|long|long long|short|size_t|void|long double|string|unsigned long long|void|unsigned char|signed char)"

variable: str = r'(?:const)?' + types + r'\s*\**\s*(\w+)\s*(=\s*[^;])?'
func: str = types + r'\s+(\w+)\s*\((?:' + variable + ',?)*\)'

operators: str = r'(\+|\=|\+=|-|-=|--|\+\+|/|/=|\*|\*=|(?:std::\s*)?cout(?:\s*<<\w+)+|(?:std::\s*)?cin(?:\s*>>\w+)+|\<|\>|!=|==|;|&&|\|\||&|\||\^|for|while|>=|<=|if|\(|\))'


string_literal: str = r'"(?:[^"]|(?<=\\)")*"'
numb_literal: str = r'\d+(?:\.\d+)?'
char_literal: str = r"'..?'"
