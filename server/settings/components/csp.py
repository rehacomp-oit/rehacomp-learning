'''
This file contains a definition for Content-Security-Policy headers.
'''

# These values might and will be redefined in `development.py` env:
CSP_SCRIPT_SRC: tuple[str, ...] = ('\'self\'',)
CSP_IMG_SRC: tuple[str, ...] = ('\'self\'',)
CSP_FONT_SRC: tuple[str, ...] = ('\'self\'',)
CSP_STYLE_SRC: tuple[str, ...] = ('\'self\'',)
CSP_DEFAULT_SRC: tuple[str, ...] = ('\'none\'',)
CSP_CONNECT_SRC: tuple[str, ...] = ()
