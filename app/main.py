from fastapi import FastAPI
from .api.zoo_api import router as zoo_router

# Initialize the FastAPI application with metadata.
# Metadata such as title, description, and version can be useful for
# auto-generated documentation and clients consuming your API.
app = FastAPI(title="Zoo Food Cost Calculator",
              description="A FastAPI application to calculate the total food costs for animals in a zoo.",
              version="1.0.0")

# Include the router from the zoo_api module.
# This modular approach to routing helps keep the application organized and scalable.
app.include_router(
    zoo_router,
    prefix="/zoo",  # Optiona
    tags=["Zoo Management"],  # Optional
)


