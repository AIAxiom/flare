import logging

class Stream:
    def __init__(self, stream_id, connection):
        self.stream_id = stream_id
        self.connection = connection
        self.buffer = b""
        self.closed = False
        logging.info(f"Stream {stream_id} initialized")
    
    def write(self, data):
        if self.closed:
            logging.warning(f"Attempt to write to closed stream {self.stream_id}")
            return
        self.buffer += data
        logging.info(f"Data written to stream {self.stream_id}: {len(data)} bytes")
    
    def read(self, size=-1):
        if size == -1:
            data, self.buffer = self.buffer, b""
        else:
            data, self.buffer = self.buffer[:size], self.buffer[size:]
        logging.info(f"Read {len(data)} bytes from stream {self.stream_id}")
        return data
    
    def close(self):
        self.closed = True
        logging.info(f"Stream {self.stream_id} closed")

class StreamManager:
    def __init__(self):
        self.streams = {}
        logging.info("Stream Manager initialized")
    
    def create_stream(self, stream_id, connection):
        if stream_id in self.streams:
            logging.warning(f"Stream {stream_id} already exists")
            return self.streams[stream_id]
        stream = Stream(stream_id, connection)
        self.streams[stream_id] = stream
        logging.info(f"Stream {stream_id} created")
        return stream
    
    def get_stream(self, stream_id):
        return self.streams.get(stream_id, None)
    
    def close_stream(self, stream_id):
        if stream_id in self.streams:
            self.streams[stream_id].close()
            del self.streams[stream_id]
            logging.info(f"Stream {stream_id} removed from manager")
