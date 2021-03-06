from django.conf.urls import url

from .views import (
    AddItem,
    AddItemCantidad,
    CotizacionView,
    CotizacionesListView,
    CambiarDiaEntregaView,
    TareaListView,
    RemisionListView, CotizacionEmailView)

urlpatterns = [
    url(r'^add/(?P<item_id>[0-9]+)/(?P<precio>[0-9]+)/(?P<forma_pago>[0-9]+)/(?P<cot_id>[0-9]+)/(?P<tipo>[0-9]+)$',
        AddItem.as_view(), name='add_item_cotizacion'),
    url(r'^add_qty/$', AddItemCantidad.as_view(), name='add_qty_item_cotizacion'),
    url(r'^cambiar_dias/$', CambiarDiaEntregaView.as_view(), name='cambiar_dias_item_cotizacion'),
    url(r'^detalle/(?P<pk>[0-9]+)$', CotizacionView.as_view(), name='detalle_cotizacion'),
    url(r'^enviar/(?P<pk>[0-9]+)$', CotizacionEmailView.as_view(), name='enviar'),
    url(r'^list/$', CotizacionesListView.as_view(), name='listar_cotizaciones'),
    url(r'^tareas/list/$', TareaListView.as_view(), name='listar_tareas'),
    url(r'^remisiones/list/$', RemisionListView.as_view(), name='listar_remisiones'),
    url(r'^buscar/$', CotizacionesListView.as_view(), name='buscar_cotizacion'),

]
