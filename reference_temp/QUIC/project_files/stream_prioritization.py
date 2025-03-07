import heapq
import logging

class StreamPriorityQueue:
    def __init__(self):
        self.queue = []  # Min-heap priority queue
        self.entry_finder = {}  # Mapping of stream_id to entry
        self.counter = 0  # Unique sequence count
        logging.info("Stream Priority Queue initialized")
    
    def add_stream(self, stream_id, priority=0):
        """Adds a stream with a given priority (lower value = higher priority)."""
        if stream_id in self.entry_finder:
            self.remove_stream(stream_id)
        entry = [priority, self.counter, stream_id]
        self.counter += 1
        self.entry_finder[stream_id] = entry
        heapq.heappush(self.queue, entry)
        logging.info(f"Stream {stream_id} added with priority {priority}")
    
    def remove_stream(self, stream_id):
        """Removes a stream from the priority queue."""
        entry = self.entry_finder.pop(stream_id, None)
        if entry:
            entry[-1] = None  # Mark as removed
        logging.info(f"Stream {stream_id} removed from priority queue")
    
    def pop_stream(self):
        """Retrieves the highest-priority stream."""
        while self.queue:
            priority, _, stream_id = heapq.heappop(self.queue)
            if stream_id is not None:
                del self.entry_finder[stream_id]
                logging.info(f"Stream {stream_id} popped from queue with priority {priority}")
                return stream_id
        logging.warning("Priority queue empty")
        return None
