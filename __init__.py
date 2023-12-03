from .TerminalCommand import Terminal

NODE_CLASS_MAPPINGS = {
    "Terminal": Terminal
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "Terminal": "Run Terminal Command"
}

__all__ = [NODE_CLASS_MAPPINGS, NODE_DISPLAY_NAME_MAPPINGS]