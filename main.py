from fastapi import FastAPI

from models.database import engine
#from models.inventory import inventory_model
from models.users import users_model
#from models.sensor import sensor_model
from models.holedata import holedata_model, calibration_model, offset_model
from models.machine import status_model, calibration_alarm_model


#from routers.inventory import inventory_rounter
from routers.users import user_router
from routers.holedata import holedata_router, calibration_router, offset_router
#from routers.auth import authen_router
#from routers.sensor import sensor_rounter
from routers.machine import status_router, calibration_alarm_router


app = FastAPI()
#app.include_router(authen_router.router)
#app.include_router(inventory_rounter.router)
app.include_router(user_router.router)
#app.include_router(sensor_rounter.router)
app.include_router(holedata_router.router)
app.include_router(calibration_router.router)
app.include_router(offset_router.router)
app.include_router(status_router.router)
app.include_router(calibration_alarm_router.router)



@app.get("/")
def hello():
    return {"hellow": "Fast-API"}


#inventory_model.Base.metadata.create_all(engine)
users_model.Base.metadata.create_all(engine)
#sensor_model.Base.metadata.create_all(engine)
holedata_model.Base.metadata.create_all(engine)
calibration_model.Base.metadata.create_all(engine)
offset_model.Base.metadata.create_all(engine)
status_model.Base.metadata.create_all(engine)
calibration_alarm_model.Base.metadata.create_all(engine)