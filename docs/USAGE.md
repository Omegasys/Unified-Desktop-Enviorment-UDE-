# Usage Instructions for UDE

The **Unified Desktop Environment (UDE)** allows for a highly customizable desktop environment with time-based theme switching. Below are some basic usage instructions for users and developers.

## Customizing Themes

### Editing Configuration Files

All customizations for themes, taskbar, and desktop behavior are handled through the `.conf` files located in the `config/` directory.

- **`ude-config.conf`**: The main configuration file where you define your default theme, taskbar, and desktop settings.
- **`time-based-config.conf`**: The configuration file for time-based theme switching, allowing you to change themes based on the time of day.

### Changing Themes

To change the theme of your desktop environment:
1. Open the `config/ude-config.conf` file.
2. Modify the `default_theme` field to use one of the available themes (e.g., `light-theme`, `neutral-theme`, or `dark-theme`).

```ini
default_theme = "dark-theme"
Taskbar Customization

You can adjust the taskbar’s position, icon placement, and visibility by editing the taskbar section in ude-config.conf:

[taskbar]
color = "#FFEB3B"
orientation = "bottom"
icon_placement = "center"
hiding_enabled = true
hiding_timeout = 2  # Seconds of inactivity before hiding the taskbar
Time-Based Theme Switching

You can enable time-based theme switching by setting enable_time_based_theme_switch = true in ude-config.conf. This will automatically change your theme based on the time of day (morning, afternoon, evening, night).

Example configuration for time-based switching:

[themes]
morning_theme = "light-theme"
afternoon_theme = "neutral-theme"
evening_theme = "dark-theme"
morning_start_time = "06:00"
afternoon_start_time = "12:00"
evening_start_time = "18:00"
night_start_time = "00:00"
Real-Time Configuration Update

Changes made to the configuration files are applied in real-time. For example, if you change the background image or taskbar color, the changes will immediately take effect without requiring a restart.

Developer Usage

If you are a developer and want to contribute to UDE, you can modify the source code in the src/ directory. UDE is written in Python and uses standard libraries, so you can easily extend its functionality or integrate new features.

Running UDE in Development Mode

To test your changes without installing them, you can run UDE directly from the src/ directory:

python3 src/main.py
