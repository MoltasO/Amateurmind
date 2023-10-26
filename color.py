#https://www.lihaoyi.com/post/BuildyourownCommandLinewithANSIescapecodes.html#256-colors
#https://gist.github.com/rene-d/9e584a7dd2935d0f461904b9f2950007
#https://en.wikipedia.org/wiki/ANSI_escape_code#Colors
import os
os.get_terminal_size
class ANSI():
    def background(code):
        return "\33[{code}m".format(code=code)
 
    def style_text(code):
        return "\33[{code}m".format(code=code)
 
    def color_text(code):
        return "\33[{code}m".format(code=code)
    def blink():
        return "\033[5m"
    def negative():
        return "\033[7m"
 
 
example_ansi = ANSI.background(97) + ANSI.color_text(35) + ANSI.style_text(4) +" TESTE ANSI ESCAPE CODE"
print(example_ansi)
