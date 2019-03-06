"""Semantic Release
"""
__version__ = '4.2.0'

from .errors import (ImproperConfigurationError, SemanticReleaseBaseError,
                     UnknownCommitMessageStyleError)

__all__ = ['ImproperConfigurationError', 'SemanticReleaseBaseError',
           'UnknownCommitMessageStyleError', 'setup_hook']


def setup_hook(argv: list):
    """
    A hook to be used in setup.py to enable `python setup.py publish`.

    :param argv: sys.argv
    """
    if len(argv) > 1 and argv[1] in ['version', 'publish', 'changelog']:
        from .cli import main
        main()
