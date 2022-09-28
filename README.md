# OctoPrint-GcodeScriptManager

Easily manage multiple GCODE scripts.

## Features:

- Multiple GCODE Scripts for each script type
- Add scripts to the sidebar for easy access
- Enable/Disable each script individually

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
    - `afterPrinterConnected`
    - `beforePrinterDisconnected`
    - `beforePrintStarted`
    - `afterPrintCancelled`
    - `afterPrintDone`
    - `beforePrintPaused`
    - `afterPrintResumed`
    - `beforeToolChange`
    - `afterToolChange`
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

### Plugin Settings Tab
![Settings Screenshot](https://github.com/kForth/plugins.octoprint.org/raw/register/gcodescriptmanager/assets/img/plugins/gcodescriptmanager/settings.png)

## License

Copyright © 2022-09-27 [Kestin Goforth](https://github.com/kforth/).

This program is free software: you can redistribute it and/or modify it under the terms of the GNU Affero General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the [GNU Affero General Public License](https://www.gnu.org/licenses/agpl-3.0.en.html) for more details.
