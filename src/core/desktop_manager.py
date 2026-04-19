# desktop_manager.py

class DesktopManager:
    def __init__(self):
        self.background_color = "#FFFFFF"
        self.background_image = None
        self.icons = []
    
    def set_background(self, color=None, image=None):
        """Set background color or image."""
        if color:
            self.background_color = color
        if image:
            self.background_image = image
    
    def add_icon(self, icon):
        """Add an icon to the desktop."""
        self.icons.append(icon)

    def remove_icon(self, icon):
        """Remove an icon from the desktop."""
        self.icons.remove(icon)
