import mock

"""
All available flavors of this library exported
"""
styles = [
    ("random", mock.to_random),
    ("alternating", mock.to_alternating),
    ("alternating2", mock.to_alternating_alt),
    ("strikethrough", mock.to_strikethrough),
    ("double", mock.to_double),
    ("dedouble", mock.from_double),
    ("smallcaps", mock.to_small_caps),
    ("lower", str.lower),
    ("upper", str.upper),
    ("cyrillic", mock.to_pseudo_cyrillic),
    ("fraktur", mock.to_fraktur),
    ("subsuper", mock.to_sub_super),
    ("cc", mock.to_cc),
    ("b", mock.to_b),
    ("pray", mock.to_pray),
    ("clap", mock.to_clap),
    ("space", mock.to_space(1)),
    ("space2", mock.to_space(2)),
    ("space3", mock.to_space(3)),
    ("lines", mock.to_lines),
    ("wordlines", mock.to_word_lines),
    ("square", mock.to_square),
]
