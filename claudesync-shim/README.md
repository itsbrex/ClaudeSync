# ClaudeSync has been renamed to ctxsync

This package is **deprecated** and will receive no further updates.

The project now lives at [ctxsync](https://pypi.org/project/ctxsync/)
([GitHub](https://github.com/jahwag/ctxsync)).

```shell
pip uninstall claudesync
pip install ctxsync
```

Installing this final `claudesync` release pulls in `ctxsync` as a dependency,
and the `claudesync` command keeps working as a deprecated alias for `ctxsync`.
Your existing configuration is picked up automatically: `~/.claudesync` is
migrated on first run and project-local `.claudesync` directories keep working.
