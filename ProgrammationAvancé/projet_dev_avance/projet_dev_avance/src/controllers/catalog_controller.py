from services.vehicule_service import VehiculeService
from services.motor_service import MotorService

class CatalogController:
    def __init__(self, vehicule_service: VehiculeService, motor_service: MotorService):
        self.vehicule_service = vehicule_service
        self.motor_service = motor_service

    def api_post_vehicule(self, vehicule):
        try:
            self.vehicule_service.create_vehicule(vehicule)
            return {"status": 201, "message": "Véhicule créé avec succès via l'API !"}
        except Exception as e:
            return {"status": 400, "error": str(e)}

    def api_get_vehicules(self):
        try:
            data = self.vehicule_service.get_vehicules()
            return {"status": 200, "data": data}
        except Exception as e:
            return {"status": 500, "error": str(e)}

    def api_put_vehicule(self, id_vehicule, vehicule_modifie):
        try:
            self.vehicule_service.update_vehicule(id_vehicule, vehicule_modifie)
            return {"status": 200, "message": f"Véhicule {id_vehicule} mis à jour !"}
        except Exception as e:
            return {"status": 400, "error": str(e)}

    def api_delete_vehicule(self, id_vehicule):
        try:
            self.vehicule_service.delete_vehicule(id_vehicule)
            return {"status": 200, "message": f"Véhicule {id_vehicule} supprimé !"}
        except Exception as e:
            return {"status": 400, "error": str(e)}