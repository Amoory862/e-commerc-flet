import asyncio
from typing import Optional

import flet as ft
import requests


class NetworkManager:
    def __init__(self):
        self._connection_status = "none"
        self._check_interval = 10  # Check every 10 seconds

    async def _update_connection_status(self):
        while True:
            try:
                response = requests.get("http://www.google.com", timeout=5)
                if response.status_code == 200:
                    self._connection_status = "connected"
                else:
                    self._connection_status = "disconnected"
            except requests.ConnectionError:
                self._connection_status = "disconnected"
            await asyncio.sleep(self._check_interval)
    
    def start_monitoring(self):
        """Start monitoring network connectivity."""
        asyncio.create_task(self._update_connection_status())

    async def is_connected(self) -> bool:
        """Check the internet connection status."""
        return self._connection_status == "connected"

    def show_warning(self, page: ft.Page, message: str):
        """Display a warning snackbar or popup on the given page."""
        page.add(ft.SnackBar(content=ft.Text(message), color='red'))
        # Alternatively, use a popup or other alert mechanism as needed

    async def monitor_and_alert(self, page: ft.Page):
        """Monitor network status and show alert if disconnected."""
        while True:
            connected = await self.is_connected()
            if not connected:
                self.show_warning(page, 'No Internet Connection')
            await asyncio.sleep(self._check_interval)

# Usage
# To use NetworkManager, you need to integrate it with your Flet app.
# Initialize NetworkManager and start monitoring
# network_manager = NetworkManager()
# network_manager.start_monitoring()

# In your Flet app code, you might call monitor_and_alert to handle network changes.
