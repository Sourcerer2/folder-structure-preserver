import os
import shutil
from pynicotine.pluginsystem import BasePlugin


class Plugin(BasePlugin):

    def download_finished_notification(self, user, virtual_path, real_path):
        """Called after a download finishes."""

        try:
            # Normalize remote path
            virtual_path = virtual_path.lstrip("/\\")
            virtual_path = virtual_path.replace("\\", os.sep)

            downloads_dir = os.path.dirname(real_path)

            # New destination:
            # If the option "Store completed downloads in username subfolders" is enabled, files are moved to:
            # <downloads>/<user>/<virtual_path>
            # Otherwise, they're moved to:
            # <downloads>/<virtual_path>
            new_path = os.path.join(downloads_dir, virtual_path)

            os.makedirs(os.path.dirname(new_path), exist_ok=True)
            shutil.move(real_path, new_path)
            self.log(f"Moved download to {new_path}")
        except Exception as e:
            self.log(f"Failed to move download: {e}")
