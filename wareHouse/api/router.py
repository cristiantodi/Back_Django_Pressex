from rest_framework.routers import DefaultRouter

from wareHouse.api.views import  PickUpOrderApiViewSet, ReceptionOrderApiViewSet, ReleaseOrderApiViewSet

router_wareHouse = DefaultRouter()

router_wareHouse.register(prefix='pickUpOrder', basename='pickUpOrder', viewset=PickUpOrderApiViewSet)
router_wareHouse.register(prefix='receptionOrder', basename='receptionOrder', viewset=ReceptionOrderApiViewSet)
router_wareHouse.register(prefix='releaseOrder', basename='releaseOrder', viewset=ReleaseOrderApiViewSet)


