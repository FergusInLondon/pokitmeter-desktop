# Pokitmeter Desktop App

This is a fork of [jdonj/BLE-pokitMeter-Windows-App](https://github.com/jdonj/BLE-pokitMeter-Windows-App).

Initially I created the fork to try and get it to play nicely with Linux, but there doesn't seem to be any issues so far! The only changes (as of 29/01/2022) are an amended directory structure, `poetry` for dependency management, and graceful termination when executed from the terminal.

Please see the original README for full details - [README.origin.md](README.origin.md). The commit at which this fork occurred is tagged `origin` - [current diff](https://github.com/jdonj/BLE-pokitMeter-Windows-App/compare/master...FergusInLondon:master).

## Changelog

**30th Jan 2022: Apple macOS support**

A few minor amendments to how Bluetooth connectivity is handled, the end result being full functionality on environments running Apple macOS.

![](/docs/images/20220130.macos-support.png)

**29th Jan 2022: Various minor amendments - incl. graceful termination from CLI.**

No changes functionality wise, but a few with regards to dependency management and code structure. App now handles terminations gracefully - i.e. via `SIGINT`.
