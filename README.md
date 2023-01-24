# OctoPrint-GcodeScriptManager

[![For OctoPrint](https://img.shields.io/badge/OctoPrint--GcodeScriptManager-white?style=flat&logo=OctoPrint)](https://plugins.octoprint.org/plugins/GcodeScriptManager/)
[![Active Instances](https://img.shields.io/badge/dynamic/json?color=brightgreen&label=Active%20Instances&query=%24%5B%3F%28%40.id%3D%3D%22GcodeScriptManager%22%29%5D.stats.instances_month&url=https%3A%2F%2Fplugins.octoprint.org%2Fplugins.json&logo=OctoPrint&labelColor=white&style=flat)](https://plugins.octoprint.org/plugins/GcodeScriptManager/)
[![New This Month](https://img.shields.io/badge/dynamic/json?color=brightgreen&label=New%20Monthly&query=%24%5B%3F%28%40.id%3D%3D%22GcodeScriptManager%22%29%5D.stats.install_events_month&url=https%3A%2F%2Fplugins.octoprint.org%2Fplugins.json&logo=OctoPrint&labelColor=white&style=flat)](https://plugins.octoprint.org/plugins/GcodeScriptManager/)
[![New This Week](https://img.shields.io/badge/dynamic/json?color=brightgreen&label=New%20Weekly&query=%24%5B%3F%28%40.id%3D%3D%22GcodeScriptManager%22%29%5D.stats.install_events_week&url=https%3A%2F%2Fplugins.octoprint.org%2Fplugins.json&logo=OctoPrint&labelColor=white&style=flat)](https://plugins.octoprint.org/plugins/GcodeScriptManager/)

[![GitHub Forks](https://img.shields.io/github/forks/kforth/OctoPrint-GcodeScriptManager?label=Forks&logo=GitHub&logoColor=black&labelColor=white&color=blue)](https://github.com/kForth/OctoPrint-GcodeScriptManager/network/members)
[![GitHub Stars](https://img.shields.io/github/stars/kforth/OctoPrint-GcodeScriptManager?label=Stars&logo=GitHub&logoColor=black&labelColor=white&color=blue)](https://github.com/kForth/OctoPrint-GcodeScriptManager/stargazers)
[![GitHub Watchers](https://img.shields.io/github/watchers/kforth/OctoPrint-GcodeScriptManager?label=Watchers&logo=GitHub&logoColor=black&labelColor=white&color=blue)](https://github.com/kForth/OctoPrint-GcodeScriptManager/watchers)
![License](https://img.shields.io/github/license/kforth/OctoPrint-GcodeScriptManager?labelColor=white&color=blue)

An OctoPrint Plugin that lets you easily manage multiple GCODE scripts.

## Features

- Manage multiple scripts for each script type
- Quickly enable or disable scripts from the sidebar
- Group multiple scripts together for easier control

## TODO

- Fix sidebar not un-collapsing properly
- Fix dialog overflow
- Better add button in edit dialog

## Setup

Install via the bundled [Plugin Manager](https://docs.octoprint.org/en/master/bundledplugins/pluginmanager.html)
or manually using this URL:

    https://github.com/kforth/OctoPrint-GcodeScriptManager/archive/main.zip

## Screenshots

### Sidebar Script Manager
![Sidebar Screenshot](https://github.com/kForth/plugins.octoprint.org/raw/register/gcodescriptmanager/assets/img/plugins/gcodescriptmanager/sidebar.png)

### Plugin Settings
![Settings Screenshot](https://github.com/kForth/plugins.octoprint.org/raw/register/gcodescriptmanager/assets/img/plugins/gcodescriptmanager/settings.png)

### Script Edit Dialog
![Edit Dialog Screenshot](https://github.com/kForth/plugins.octoprint.org/raw/register/gcodescriptmanager/assets/img/plugins/gcodescriptmanager/editdialog.png)

## License

Copyright © 2023 [Kestin Goforth](https://github.com/kforth/).

This program is free software: you can redistribute it and/or modify it under the terms of the GNU Affero General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the [GNU Affero General Public License](https://www.gnu.org/licenses/agpl-3.0.en.html) for more details.
