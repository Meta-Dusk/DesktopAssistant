import asyncio
import flet as ft
from screeninfo import Monitor
from typing import List
from ui.styles import transparent_window
from utilities.monitor import get_all_monitors
from utilities.debug import debug_msg


WINDOW_WIDTH = 288
WINDOW_HEIGHT = 270

def set_win_pos_bc(monitors: List[Monitor], page: ft.Page):
    """Sets the window's position to the primary monitor's bottom center."""
    if monitors:
        primary = monitors[0] # Gets the primary monitor
        window = page.window
        
        # Sets the window horizontally centered
        window.left = primary.x + (primary.width - window.width) / 2
        
        # Sets the window vertically centered
        window.top = primary.y + primary.height - window.height

async def before_main_app(page: ft.Page, debug: bool = False):
    """Serves as the setup function. Must be called before the `main`."""
    # -------- Before Main App --------
    transparent_window(page, width=WINDOW_WIDTH, height=WINDOW_HEIGHT, debug=debug)
    
    # -- Set Window Position --
    monitors = get_all_monitors()
    set_win_pos_bc(monitors, page)
    
    # Attach global page/window handlers before main starts.
    def on_keyboard_event(e: ft.KeyboardEvent):
        # Keep it minimal here, actual logic handled in main
        debug_msg(f"Keyboard event captured: {e.key}", debug=True)

    def on_window_event(e: ft.WindowEvent):
        # Same here, lightweight placeholder
        debug_msg(f"Window event captured: {e.type}", debug=True)
    
    if debug:
        page.on_keyboard_event = on_keyboard_event
    
    page.window.on_event = on_window_event
    page.update()
    
async def fix_stretched_window(
    page: ft.Page, *,
    center_page: bool = False
):
    """
    When launching a Flet desktop app, sometimes the window appears to be stretched.
    The fix? Just resize it. So, that's exactly what this does.
    """
    page.window.width = WINDOW_WIDTH * 1.1
    page.window.height = WINDOW_HEIGHT * 1.1
    page.window.update()
    await asyncio.sleep(1)
    page.window.width = WINDOW_WIDTH
    page.window.height = WINDOW_HEIGHT
    page.window.update()
    if center_page:
        await page.window.center()
        