"""import time

def wait_for_file(download_dir, timeout=20):
    end = time.time() + timeout
    while time.time() < end:
        files = [f for f in download_dir.iterdir() if f.is_file()]
        if files:
            return True
        time.sleep(3)
    return False"""

# --- Robust download waiter (supports pattern/timeout/stable_seconds) ---
import time
from pathlib import Path

def wait_for_file(download_dir: Path, pattern: str = "*", timeout: int = 30, stable_seconds: int = 1) -> Path:
    """
    Polls download_dir for files matching pattern until one finishes downloading:
    - ignores temp extensions (.crdownload/.part/.tmp)
    - requires file size to stay unchanged for `stable_seconds`
    Returns: Path to the completed file
    Raises: TimeoutError if nothing completes within `timeout` seconds
    """
    end = time.time() + timeout
    last_size = {}
    while time.time() < end:
        candidates = [
            p for p in download_dir.glob(pattern)
            if not p.name.endswith((".crdownload", ".part", ".tmp"))
        ]
        if candidates:
            f = max(candidates, key=lambda p: p.stat().st_mtime)  # newest file
            size = f.stat().st_size
            if f not in last_size:
                last_size[f] = (size, time.time())
            else:
                prev_size, prev_t = last_size[f]
                if size == prev_size and time.time() - prev_t >= stable_seconds:
                    return f
                last_size[f] = (size, time.time())
        time.sleep(2)
    raise TimeoutError(f"No completed download matching {pattern!r} in {download_dir}")