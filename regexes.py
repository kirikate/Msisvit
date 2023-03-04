types: str = r"(?:int|char|float|double|bool|long|long long|short|size_t|void|long double|string|unsigned long long|void|unsigned char|signed char)"

variable: str = r'(?:const)?' + types + r'\s*(\w+)\s*(=\s*[^;])?'
func: str = types + r'(\w+)\s*\((?:' + variable + ')*\)'

operators: str = r'(\+|\=|\+=|-|-=|--|\+\+|/|/=|\*|\*=|(?:std::\s*)?cout(?:\s*<<\w+)+|(?:std::\s*)?cin(?:\s*>>\w+)+|\<|\>|!=|==|;|&&|\|\||&|\||\^|for|while|>=|<=)'

for_expr: str = ''
while_expr: str = ''
if_expr: str = ''
