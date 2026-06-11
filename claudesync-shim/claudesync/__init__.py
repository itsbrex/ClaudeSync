"""Deprecated compatibility shim: ClaudeSync has been renamed to ctxsync."""

import sys

_RENAME_NOTICE = (
    "ClaudeSync has been renamed to ctxsync. The 'claudesync' package is "
    "deprecated and will receive no further updates. Install 'ctxsync' and "
    "use the 'ctxsync' command instead: https://pypi.org/project/ctxsync/"
)


def main():
    print(f"WARNING: {_RENAME_NOTICE}", file=sys.stderr)
    from ctxsync.cli.main import cli

    cli()
