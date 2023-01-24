class TYPE:
    AFTER_PRINTER_CONNECTED = "afterPrinterConnected"
    BEFORE_PRINTER_DISCONNECTED = "beforePrinterDisconnected"
    BEFORE_PRINT_STARTED = "beforePrintStarted"
    AFTER_PRINT_CANCELLED = "afterPrintCancelled"
    AFTER_PRINT_DONE = "afterPrintDone"
    BEFORE_PRINT_PAUSED = "beforePrintPaused"
    AFTER_PRINT_RESUMED = "afterPrintResumed"
    BEFORE_TOOL_CHANGE = "beforeToolChange"
    AFTER_TOOL_CHANGE = "afterToolChange"


class WHEN:
    AFTER_DEFAULT = "afterDefaultScript"
    BEFORE_DEFAULT = "beforeDefaultScript"


TYPE_OPTIONS = [
    {
        'label': 'After Printer Connected',
        'value': TYPE.AFTER_PRINTER_CONNECTED,
    },
    {
        'label': 'Before Printer Disconnected',
        'value': TYPE.BEFORE_PRINTER_DISCONNECTED,
    },
    {
        'label': 'Before Print Started',
        'value': TYPE.BEFORE_PRINT_STARTED,
    },
    {
        'label': 'After Print Cancelled',
        'value': TYPE.AFTER_PRINT_CANCELLED,
    },
    {
        'label': 'After Print Done',
        'value': TYPE.AFTER_PRINT_DONE,
    },
    {
        'label': 'Before Print Paused',
        'value': TYPE.BEFORE_PRINT_PAUSED,
    },
    {
        'label': 'After Print Resumed',
        'value': TYPE.AFTER_PRINT_RESUMED,
    },
    {
        'label': 'Before Tool Change',
        'value': TYPE.BEFORE_TOOL_CHANGE,
    },
    {
        'label': 'After Tool Change',
        'value': TYPE.AFTER_TOOL_CHANGE,
    },
]

WHEN_OPTIONS = [
    {
        'label': 'After Default',
        'value': WHEN.AFTER_DEFAULT,
    },
    {
        'label': 'Before Default',
        'value': WHEN.BEFORE_DEFAULT,
    },
]

DEFAULT_SCRIPTS = [
    {
        "name": "Power Off After Print",
        "description": "Send 'M81' after the print finishes or fails.",
        "scripts": [{
            "type": TYPE.AFTER_PRINT_DONE,
            "when": WHEN.AFTER_DEFAULT,
            "script": "M81",
        }],
        "sidebarToggle": True,
        "enabled": False,
    },
    {
        "name": "Park On Pause",
        "description": "Park and unpark the print head when pausing.",
        "scripts": [
            {
                "type": TYPE.BEFORE_PRINT_PAUSED,
                "when": WHEN.AFTER_DEFAULT,
                "script": """{% if pause_position.x is not none %}
; relative XYZE
G91
M83

; retract filament, move Z slightly upwards
G1 Z+5 E-5 F4500

; absolute XYZE
M82
G90

; move to a safe rest position, adjust as necessary
G1 X0 Y0
{% endif %}
""",
            },
            {
                "type": TYPE.AFTER_PRINT_RESUMED,
                "when": WHEN.BEFORE_DEFAULT,
                "script": """{% if pause_position.x is not none %}
; relative extruder
M83

; prime nozzle
G1 E-5 F4500
G1 E5 F4500
G1 E5 F4500

; absolute E
M82

; absolute XYZ
G90

; reset E
G92 E{{ pause_position.e }}

; move back to pause position XYZ
G1 X{{ pause_position.x }} Y{{ pause_position.y }} Z{{ pause_position.z }} F4500

; reset to feed rate before pause if available
{% if pause_position.f is not none %}G1 F{{ pause_position.f }}{% endif %}
{% endif %}
""",
            }
        ],
        "enabled": True,
        "sidebarToggle": False,
    }
]
