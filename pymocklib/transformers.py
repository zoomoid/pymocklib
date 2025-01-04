from typing import Callable, Tuple
from pymocklib.helpers import alternating_mask_iterator, random_mask_iterator, intercalate, intersperse
from functools import reduce

def to_upper_by(mask: list[bool]):
    """
    Transforms characters of a string into uppercase where the corresponding element of the bool list is true. On encountering a letter that already is uppercase the mask is reversed.
    """
    def h(t: str) -> str:
        def g(x: Tuple[str, list[bool]], char: str) -> Tuple[str, list[bool]]:
            """
            fold function that depending on a bit mask, inverts lower case letters
            """
            txt, int_mask = x
            if len(int_mask) == 0:
                return txt + char, []
            bit = int_mask.pop()
            if char.isupper():
                return txt + char, [not x for x in int_mask]
            if char.isspace():
                return txt + char, [bit] + int_mask
            if bit:
                return txt + char.upper(), mask
            if not bit:
                return txt + char, mask
        return reduce(g, list(t), ("", mask))[0]
    return h


def to_alternating(t: str) -> str:
    """
    Transforms a string into alternating capitalization
    """
    # we cannot simply use repeat from haskell which creates an infinite list
    # thus we need a custom iterator for that
    return to_upper_by(list(alternating_mask_iterator(n=len(t))))(t)

def to_alternating_alt(t: str):
    """
    decorates the to_alternating flavor with a slightly more regular version
    by setting all characters to lowercase before applying the masking reduce
    """
    return to_alternating(t.lower())

def to_random(t: str) -> str:
    """
    Transforms a string into a random capitalization
    """
    # we cannot simply use repeat from haskell which creates an infinite list
    # thus we need a custom iterator for that
    return to_upper_by(list(random_mask_iterator(hash(t), n=len(t))))(t)

def to_space(n: int):
    """
    Returns a function with a closure for the length n of each space
    """
    def _to_space(t: str) -> str:
        """
        Transforms a string into a space-seperated word with spaces of length n
        """
        return intercalate(' ' * n, list(t))
    return _to_space

def to_double(t: str) -> str:
    """
    Transforms characters into their double-struck variant if available.
    """
    def f(char: str):
        match char:
            case 'C': return chr(8450)
            case 'H': return chr(8461)
            case 'N': return chr(8469)
            case 'P': return chr(8473)
            case 'Q': return chr(8474)
            case 'R': return chr(8477)
            case 'Z': return chr(8484)
            case _:
                l = ord(char)
                if 48 <= l and l <= 57:
                    return chr(l - 48 + 120792) # Number
                elif 65 <= l and l <= 90:
                    return chr(l - 65 + 120120) # Uppercase letters
                elif 97 <= l and l <= 120:
                    return chr(l - 97 + 120146) # Lowercase letters
                else:
                    return char
    return intercalate("", [f(char) for char in list(t)])

def from_double(t: str) -> str:
    """
    Transforms double-struck characters back into their normal variant.
    """
    def f(char: str):
        c = ord(char)
        match c:
            case 8450: return 'C'
            case 8461: return 'H'
            case 8469: return 'N'
            case 8473: return 'P'
            case 8474: return 'Q'
            case 8477: return 'R'
            case 8484: return 'Z'
            case _:
                if 120792 <= c and c <= 120801:
                    return chr(c - 120792 + 48)
                elif 120120 <= c and c <= 120145:
                    return chr(c - 120120 + 65)
                elif 120146 <= c and c <= 120171:
                    return chr(c - 120146 + 97)
                else:
                    return chr(c)
    return intercalate("", [f(char) for char in list(t)])

def to_small_caps(t: str) -> str:
    """
    Transforms lowercase characters into their unicode small capital variants.
    """
    def f(char: str):
        match char:
            case 'a': return chr(7424)
            case 'b': return chr(665)
            case 'c': return chr(7428)
            case 'd': return chr(7429)
            case 'e': return chr(7431)
            case 'f': return chr(42800)
            case 'g': return chr(610)
            case 'h': return chr(668)
            case 'i': return chr(618)
            case 'j': return chr(7434)
            case 'k': return chr(7435)
            case 'l': return chr(671)
            case 'm': return chr(7437)
            case 'n': return chr(628)
            case 'o': return chr(7439)
            case 'p': return chr(7448)
            case 'q': return chr(491)
            case 'r': return chr(640)
            case 's': return chr(42801)
            case 't': return chr(7451)
            case 'u': return chr(7452)
            case 'v': return chr(7456)
            case 'w': return chr(7457)
            case 'y': return chr(655)
            case 'z': return chr(7458)
            case _: return char
    return intercalate("", [f(char) for char in list(t)])

def to_pseudo_cyrillic(t: str) -> str:
    """
    Replaces some characters with cyrillic ones *looking* similarly.
    """
    def f(char: str):
        match char:
            case 'A': return 'Д'
            case 'B': return 'Б'
            case 'E': return 'З'
            case 'N': return 'И'
            case 'O': return 'Ө'
            case 'R': return 'Я'
            case 'U': return 'Ц'
            case 'W': return 'Щ'
            case 'X': return 'Ж'
            case 'a': return 'д'
            case 'b': return 'в'
            case 'e': return 'ё'
            case 'h': return 'Ђ'
            case 'i': return 'ɪ'
            case 'k': return 'к'
            case 'o': return 'ө'
            case 'r': return 'я'
            case 't': return 'т'
            case 'u': return 'ц'
            case 'y': return 'џ'
            case _: return char
    return intercalate("", [f(char) for char in list(t)])

def to_pray(t: str) -> str:
    return intercalate("🙏", t.split())

def to_clap(t: str) -> str:
    return intercalate("👏", t.split())

def to_lines(t: str) -> str:
    return intersperse("\n", t)

def to_word_lines(t: str) -> str:
    return intercalate("\n", t.split())

def to_cc(t: str) -> str:
    """
    Replaces all occurences of *lowercase* "ck" and "k" in a string with "cc".
    """
    return t.replace("ck", "cc").replace("k", "cc")

def to_b(t: str) -> str:
    """
    Replaces all occurences of "b" and "B" with B button emojis.
    """
    return t.replace("B", "🅱️").replace("b", "🅱️")

def to_strikethrough(t: str) -> str:
    """
    Uses unicode U+0336 to let a text look struck through.
    """
    if t == "":
        return ""
    else:
        return intersperse("\u0336", t) + "\u0336"

def to_fraktur(t: str) -> str:
    """
    Converts plain characters to fracture with some exceptions
    """
    def f(char: str):
        match char: # special cases with letter code out of order
            case "C": return "ℭ"
            case 'H': return "ℌ"
            case 'I': return "ℑ"
            case 'R': return "ℜ"
            case 'Z': return "ℨ"
            case 'ß': return "ſ𝔰"
            case 'ẞ': return "𝔖𝔖"
            case 'ö': return "𝔬𝔢"
            case 'Ö': return "𝔒𝔢"
            case 'ä': return "𝔞𝔢"
            case 'Ä': return "𝔄𝔢"
            case 'ü': return "𝔲𝔢"
            case 'Ü': return "𝔘𝔢"
            case _:
                l = ord(char)
                if 65 <= l and l <= 90: # upper case letters
                    return chr(120068 + (l - 65))
                elif 97 <= l and l <= 122: # lower case letters
                    return chr(120094 + (l - 97))
                else:
                    return char
    return intercalate("", [f(char) for char in list(t)])

def to_sub_super(t: str) -> str:
    """
    Transforms a character into a unicode sub- or superscript variant. If true is given and a subscript version is available, that is used. If none is available or false is given, a superscript version is used. If none is available, the character is left unchanged.
    """
    def f(b: bool):
        def g(char: str) -> str:
            match b, char:
                case (_, 'A'): return chr(7468)
                case (_, 'B'): return chr(7470)
                case (_, 'D'): return chr(7472)
                case (_, 'E'): return chr(7473)
                case (_, 'G'): return chr(7475)
                case (_, 'H'): return chr(7476)
                case (_, 'I'): return chr(7477)
                case (_, 'J'): return chr(7478)
                case (_, 'K'): return chr(7479)
                case (_, 'L'): return chr(7480)
                case (_, 'M'): return chr(7481)
                case (_, 'N'): return chr(7482)
                case (_, 'O'): return chr(7484)
                case (_, 'P'): return chr(7486)
                case (_, 'R'): return chr(7487)
                case (_, 'T'): return chr(7488)
                case (_, 'U'): return chr(7489)
                case (_, 'V'): return chr(11389)
                case (_, 'W'): return chr(7490)
                case (False, 'a'): return 'ᵃ'
                case (True, 'a'): return 'ₐ'
                case (_, 'b'): return 'ᵇ'
                case (_, 'c'): return 'ᶜ'
                case (_, 'd'): return 'ᵈ'
                case (False, 'e'): return 'ᵉ'
                case (True, 'e'): return 'ₑ'
                case (_, 'f'): return 'ᶠ'
                case (_, 'g'): return 'ᵍ'
                case (False, 'h'): return 'ʰ'
                case (True, 'h'): return 'ₕ'
                case (False, 'i'): return 'ⁱ'
                case (True, 'i'): return 'ᵢ'
                case (False, 'j'): return 'ʲ'
                case (True, 'j'): return 'ⱼ'
                case (False, 'k'): return 'ᵏ'
                case (True, 'k'): return 'ₖ'
                case (False, 'l'): return 'ˡ'
                case (True, 'l'): return 'ₗ'
                case (False, 'm'): return 'ᵐ'
                case (True, 'm'): return 'ₘ'
                case (False, 'n'): return 'ⁿ'
                case (True, 'n'): return 'ₙ'
                case (False, 'o'): return 'ᵒ'
                case (True, 'o'): return 'ₒ'
                case (False, 'p'): return 'ᵖ'
                case (True, 'p'): return 'ₚ'
                case (False, 'r'): return 'ʳ'
                case (True, 'r'): return 'ᵣ'
                case (False, 's'): return 'ˢ'
                case (True, 's'): return 'ₛ'
                case (False, 't'): return 'ᵗ'
                case (True, 't'): return 'ₜ'
                case (False, 'u'): return 'ᵘ'
                case (True, 'u'): return 'ᵤ'
                case (False, 'v'): return 'ᵛ'
                case (True, 'v'): return 'ᵥ'
                case (_, 'w'): return 'ʷ'
                case (False, 'x'): return 'ˣ'
                case (True, 'x'): return 'ₓ'
                case (_, 'y'): return 'ʸ'
                case (_, 'z'): return 'ᶻ'
                case (_, _): return char
        return g
    return intercalate("", [f(b)(char) for b, char in zip(alternating_mask_iterator(n=len(t)), list(t))])

def to_square(t: str) -> str:
    """
    Makes a square of a string by putting it with spaces in the first line and then all characters except the first in single lines after that first line.
    """
    return intersperse(' ', t) + "\n" + intercalate("\n", [t[1:][n:n+1] for n in range(len(t) - 1)])

def to_interspersed_flag(flag: str):
    """
    Replaces all vowels in latin with a given unicode flag emoji
    """
    def _c(t: str) -> str:
        return t.replace("aeiouäöü", flag)
    return _c

"""
All available flavors of this library exported
"""
styles: list[Tuple[str, Callable[[str], str]]] = [
    ("random", to_random),
    ("alternating", to_alternating),
    ("alternating2", to_alternating_alt),
    ("strikethrough", to_strikethrough),
    ("double", to_double),
    ("dedouble", from_double),
    ("smallcaps", to_small_caps),
    ("lower", str.lower),
    ("upper", str.upper),
    ("cyrillic", to_pseudo_cyrillic),
    ("fraktur", to_fraktur),
    ("subsuper", to_sub_super),
    ("cc", to_cc),
    ("b", to_b),
    ("pray", to_pray),
    ("clap", to_clap),
    ("space", to_space(1)),
    ("space2", to_space(2)),
    ("space3", to_space(3)),
    ("lines", to_lines),
    ("wordlines", to_word_lines),
    ("square", to_square),
    ("indian", to_interspersed_flag("🇮🇳")),
    ("turkish", to_interspersed_flag("🇹🇷"))
]

def style_doc(key: str) -> str:
    """
    maps a descriptive text to each style
    """
    match key:
        case "random": return "Flips lowercase characters pseudo-randomly into uppercase letters."
        case "alternating": return "Flips every second letter into an uppercase one, starting with the second character."
        case "alternating2": return "Like alternate, but ignores case in the input. Equivalent to lower|alternate."
        case "strikethrough": return "Turns the input into strikethrough using Unicode combinators (e̶x̶a̶m̶p̶l̶e̶)."
        case "double": return "Turns characters (latin letters and numbers) into their double-struck variants (𝕖𝕩𝕒𝕞𝕡𝕝𝕖). Also known as blackboard bold."
        case "dedouble": return "Turns double-struck characters (like from the \"double\" style) back into normal ones."
        case "smallcaps": return "Turns lowercase letters into small capitals."
        case "lower": return "Turns all characters into lowercase ones."
        case "upper": return "Turns all characters into UPPERCASE ones."
        case "cyrillic": return "Turns the text into a stereotypical fake russian looking variant."
        case "fraktur": return "Turns the input into 𝔉𝔯𝔞𝔨𝔱𝔲𝔯𝔰𝔠𝔥𝔯𝔦𝔣𝔱."
        case "subsuper": return "Alternatingly put letters into sub- and superscript, where possible."
        case "cc": return "Replaces all occurences of lowercase \"c\", \"ck\" and \"k\" with \"cc\"."
        case "b": return "Replaces all occurences of Bs (lower- and uppercase) with B-button emojis (🅱)."
        case "pray": return "Puts pray emojis (🙏) between all words."
        case "clap": return "Puts clap emojis (👏) between all words."
        case "space": return "Inserts a  s p a c e  between every two characters."
        case "space2": return "Inserts two   s  p  a  c  e  s   between every two characters."
        case "space3": return "Inserts three    s   p   a   c   e   s    between every two characters."
        case "lines": return "Puts each character on a single line."
        case "wordlines": return "Puts each word on a single line."
        case "square": return "Shows the input spaced in the first line and the tail of the input lined afterwards."
        case "indian": return "Replaces all vowels with the indian flag"
        case "turkish": return "Replaces all vowels with the turkish flag"
        case _: return "No documentation available."
