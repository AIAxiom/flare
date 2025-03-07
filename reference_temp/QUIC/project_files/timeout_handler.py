import threading
import logging

class TimeoutHandler:
    def __init__(self):
        self.timers = {}
        self.lock = threading.Lock()
        logging.info("Timeout Handler initialized")

    def start_timer(self, dcid, timeout=30):
        with self.lock:
            if dcid in self.timers:
                self.timers[dcid].cancel()
            self.timers[dcid] = threading.Timer(timeout, self._trigger_timeout, args=(dcid,))
            self.timers[dcid].start()
            logging.info(f"Started timeout timer for {dcid}")

    def reset_timer(self, dcid, timeout=30):
        with self.lock:
            if dcid in self.timers:
                self.timers[dcid].cancel()
            self.timers[dcid] = threading.Timer(timeout, self._trigger_timeout, args=(dcid,))
            self.timers[dcid].start()
            logging.info(f"Reset timeout timer for {dcid}")

    def cancel_timer(self, dcid):
        with self.lock:
            if dcid in self.timers:
                self.timers[dcid].cancel()
                del self.timers[dcid]
                logging.info(f"Cancelled timeout timer for {dcid}")

    def _trigger_timeout(self, dcid):
        logging.warning(f"Connection timeout triggered for {dcid}")
        # Handle connection timeout logic here
        