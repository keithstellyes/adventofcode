import curses, sys

from bs4 import BeautifulSoup, NavigableString

ELTYPES = ['', 'emphasis', 'link', 'code']
HTML_TO_ELTYPE = {'p':'', 'a':'link', 'em':'emphasis', 'code':'code'}

class ParagraphElement:
    def __init__(self, text, eltype=''):
        self.text = text
        self.eltype = eltype

class Paragraph:
    def __init__(self, text_els: list[ParagraphElement]):
        self.text_els = text_els

class DayDescription:
    def __init__(self, header: str, paragraphs: list[Paragraph]):
        self.header = header
        self.paragraphs = paragraphs

# to silence warning around not explicitly giving a parser
f = open('21', 'r')

def parseparagraphel(el):
    if type(el) == NavigableString:
        return ParagraphElement(el.text)
    elif el.name is None or el.name == 'script':
        return None
    elif el.name in HTML_TO_ELTYPE.keys():
        print(el.name, el.text)
        return ParagraphElement(el.text, HTML_TO_ELTYPE[el.name])
    elif el.name == 'span':
        children = [c for c in el .children]
        print(len(children))
        return parseparagraphel([c for c in el.children][0])
    else:
        return ParagraphElement(el.text)
        print('unknown el type', el.name)   

class DDParser:
    def __init__(self):
        pass
    def _parseparagraph(self):
        child = self.children.pop(0)
        els = []
        if child.name == 'pre':
            child = [c for c in child.children][0]
        if child.name == 'script':
            return None
        elif child.name == 'p' or child.name == 'pre':
            for c in child.children:
                el = parseparagraphel(c)
                if el is not None:
                    els.append(el)
        elif child.name == 'ul':
            for li in child.children:
                if li.text.strip() == '':
                    continue
                els.append(ParagraphElement(f'\n* {li.text}'))
        else:
            print('else', child.name)
            els.append(parseparagraphel(child))

        return Paragraph(els)
    def parse(self, f):
        self.soup = BeautifulSoup(f, features='lxml')
        f.close()
        self.descsoup = self.soup.select('article', {'class':'day-desc'})[0]
        self.children = [c for c in self.descsoup.children if type(c) != NavigableString]
        header = self.children.pop(0).text
        paras = []
        while len(self.children) > 0:
            para = self._parseparagraph()
            if para is not None:
                paras.append(para)
        return DayDescription(header, paras)

parser = DDParser()
dd = parser.parse(f)

def renderdd(stdscr, dd):
    stdscr.addstr(dd.header, curses.A_BOLD)
    for p in dd.paragraphs:
        stdscr.addstr('\n\n')
        for el in p.text_els:
            print('rendering el:', el.eltype, file=sys.stderr)
            try:
                if el.eltype == '':
                    stdscr.addstr(el.text)
                elif el.eltype == 'link':
                    stdscr.addstr(el.text, curses.A_UNDERLINE)
                elif el.eltype == 'emphasis':
                    stdscr.addstr(el.text, curses.A_BOLD)
                elif el.eltype == 'code':
                    print('rendering code')
                    lines = el.text.split('\n')
                    lines = [f'{l}' for l in lines if l.strip() != '']
                    if len(lines) > 1:
                        mx = max([len(l) for l in lines])
                        lines = [l.ljust(mx, ' ') for l in lines]
                    stdscr.addstr('\n'.join(lines), curses.A_STANDOUT)
                else:
                    print('tried to render unknown el type', file=sys.stderr)
            except Exception as e:
                f = open('ex', 'w')
                f.write(str(e))
                f.close()
                print('except', e)
                pass


def main(stdscr):
    curses.use_default_colors()
    curses.init_pair(1, -1, -1)
    stdscr.clear()
    renderdd(stdscr, dd)
    stdscr.getkey()

if __name__ == '__main__':
    curses.wrapper(main)

# TODO support <a href> to other years/days
# for clicking, just keep track of cursor if it's on the selected thing
