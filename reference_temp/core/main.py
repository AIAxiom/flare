from fastapi import FastAPI
from typing import Dict, List, Optional
import uvicorn

app = FastAPI()

# In-memory plugin storage
plugins = []

@app.post("/process")
def process_request(conversation_id: str, prompt: str, metadata: Optional[Dict[str, str]] = None):
    if metadata is None:
        metadata = {}
    response = {
        "answer": f"Received: {prompt}",
        "conversation_id": conversation_id,
        "metadata": metadata
    }
    return response

@app.post("/register_plugin")
def register_plugin(plugin_name: str, description: str):
    plugin = {
        "plugin_id": str(len(plugins) + 1),
        "plugin_name": plugin_name,
        "description": description
    }
    plugins.append(plugin)
    return {"acknowledged": True}

@app.get("/list_plugins")
def list_plugins():
    return {"plugins": plugins}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000, http="h3")
