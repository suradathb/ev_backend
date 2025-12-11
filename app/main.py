from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.database import Base, engine
from app.routers import auth, branches, customers, vehicles, appointments, work_orders

# Create all tables (for demo; use Alembic in real projects)
Base.metadata.create_all(bind=engine)

app = FastAPI(title="EV Service Center Management API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router)
app.include_router(branches.router)
app.include_router(customers.router)
app.include_router(vehicles.router)
app.include_router(appointments.router)
app.include_router(work_orders.router)


@app.get("/")
def root():
    return {"message": "EV Service Center Management API is running"}
