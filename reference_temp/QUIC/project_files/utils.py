import logging

def setup_logging():
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )

def hex_dump(data):
    return ' '.join(f'{byte:02x}' for byte in data)
