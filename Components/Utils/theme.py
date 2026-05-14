import tkinter as tk

def apply_style(widget, type="primary"):
    styles = {
        "primary": {"bg": "#2c3e50", "fg": "white", "font": ("Segoe UI", 10, "bold")},
        "secondary": {"bg": "#34495e", "fg": "#ecf0f1", "font": ("Segoe UI", 9)},
        "danger": {"bg": "#e74c3c", "fg": "white", "font": ("Segoe UI", 9, "bold")},
        "accent": {"bg": "#3498db", "fg": "white", "font": ("Segoe UI", 9)}
        #"button":{"bg":}
    }
    config = styles.get(type, styles["primary"])
    widget.config(**config, padx=10, pady=5, relief=tk.FLAT)