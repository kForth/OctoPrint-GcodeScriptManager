# OctoPrint-GcodeScriptManager

An OctoPrint Plugin that lets you easily manage multiple GCODE scripts.

## Features

- Manage multiple scripts for each script type
- Quickly enable or disable individual scripts from the sidebar

## TODO

- Fix sidebar not un-collapsing properly

## Setup

Install via the bundled [Plugin Manager](https://docs.octoprint.org/en/master/bundledplugins/pluginmanager.html)
or manually using this URL:

    https://github.com/kforth/OctoPrint-GcodeScriptManager/archive/main.zip

## Configuration

GCODE Script Settings:

- **Name**
  - Easily identifieable name for script.
- **Type**
  - The type of GCODE script.
    - `After Printer Connected`
    - `Before Printer Disconnected`
    - `Before Print Started`
    - `After Print Cancelled`
    - `After Print Done`
    - `Before Print Paused`
    - `After Print Resumed`
    - `Before Tool Change`
    - `After Tool Change`
- **When**
  - When to execute the script, relative to the default GCODE script of the same type.
    - `Before Default Script`
    - `After Default Script`
- **Script**
  - The GCODE command(s) to execute.
- **Enabled**
  - If `true`, the script will be executed with the default GCODE script of the same type.
    - `true` / `false`
- **SidebarToggle**
  - If `true`, the script will be added to the sidebar manager.
    - `true` / `false`

## Screenshots

### Sidebar Script Manager
![Sidebar Screenshot](https://github.com/kForth/plugins.octoprint.org/raw/register/gcodescriptmanager/assets/img/plugins/gcodescriptmanager/sidebar.png)

### Plugin Tab Tab
![Tab Screenshot](https://github.com/kForth/plugins.octoprint.org/raw/register/gcodescriptmanager/assets/img/plugins/gcodescriptmanager/tab.png)

### Script Edit Dialog
![Edit Dialog Screenshot](https://github.com/kForth/plugins.octoprint.org/raw/register/gcodescriptmanager/assets/img/plugins/gcodescriptmanager/editdialog.png)

## License

Copyright © 2023 [Kestin Goforth](https://github.com/kforth/).

This program is free software: you can redistribute it and/or modify it under the terms of the GNU Affero General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the [GNU Affero General Public License](https://www.gnu.org/licenses/agpl-3.0.en.html) for more details.
