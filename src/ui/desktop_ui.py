# desktop_ui.py

class DesktopUI:
    def __init__(self, desktop_manager):
        self.desktop_manager = desktop_manager
    
    def render(self):
        """Render the desktop background and icons."""
        # Example of displaying background and icons
        self.display_background()
        self.display_icons()

    def display_background(self):
        """Render the background image or color."""
        if self.desktop_manager.background_image:
            # Render the background image
            pass
        else:
            # Render the background color
            pass

    def display_icons(self):
        """Display the icons on the desktop."""
        for icon in self.desktop_manager.icons:
            icon.display()
