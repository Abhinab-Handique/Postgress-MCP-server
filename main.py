from fastapi import FastAPI
from app.controller import user_controller
from app.core.database import engine, Base
from fastmcp import FastMCP

# 1. Initialize Database
Base.metadata.create_all(bind=engine)

# 2. Create ONE main FastAPI application
app = FastAPI(title="Database Talk")

# 3. Include your standard API routers
app.include_router(user_controller.router)

# 4. Initialize FastMCP
mcp = FastMCP.from_fastapi(app)


if __name__ == "__main__":
    mcp.run()



# from contextlib import asynccontextmanager
# from fastapi import FastAPI
# from fastmcp import FastMCP



# def answer_to_ml_model_everything(x: float):
#     return x * 42


# ml_models = {}

# @asynccontextmanager
# async def fastapi_lifespan(app: FastAPI):
#     # run something before the app fully starts
#     ml_models["ml_model"] = answer_to_ml_model_everything
#     yield 
#     # run something after the app ends


# api = FastAPI()
# mcp = FastMCP.from_fastapi(api)
# mcp_app = mcp.http_app(path='/mcp')


# # tool -> mcp
# @mcp.tool()
# def add(a:int, b:int) -> int:
#     """
#     Add two numbers
#     """
#     return (a + b) * 3823


# @mcp.tool()
# def multiply(a:int, b:int) -> float:
#     """
#     Multiply two numbers
#     """
#     return (a * b) * 0.3823

# @mcp.tool()
# def call_predict(x: float) -> float:
#     """predict the results of a number"""
#     result = ml_models["ml_model"](x)
#     return result


# @api.get("/")
# def read_root():
#     return {"hello": "world"}


# @api.get("/predict")
# def do_prediction(x:int):
#     result = ml_models["ml_model"](x)
#     return {"result": result}


# @asynccontextmanager
# async def global_lifespan(app:FastAPI):
#     async with fastapi_lifespan(app):
#         async with mcp_app.lifespan(app):
#             yield


# app = FastAPI(
#     title="Hungry Py MCP App",
#     routes = [
#         *mcp_app.routes,
#         *api.routes,
#     ],
#     lifespan=global_lifespan
# )