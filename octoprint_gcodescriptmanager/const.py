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
