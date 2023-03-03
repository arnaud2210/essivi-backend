from fastapi import FastAPI
from routers import menu, roles, users, authentication, customers, products, orders, delivers, categories, reports
from settings.database import engine
from settings import models
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

water = FastAPI()


# Configurer les origines autorisées
origins = ["*"]

# Ajouter le middleware CORS
water.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

models.Base.metadata.create_all(bind=engine)

water.include_router(authentication.router)

water.include_router(reports.router)

water.include_router(menu.router)

water.include_router(roles.router)

water.include_router(users.router)

# water.include_router(accounts.router)

# water.include_router(agents.router)

water.include_router(customers.router)

water.include_router(categories.router)

water.include_router(products.router)

water.include_router(orders.router)

water.include_router(delivers.router)


if __name__ == "__main__":
    uvicorn.run("main:water", host="0.0.0.0", port=8000, reload=True)
