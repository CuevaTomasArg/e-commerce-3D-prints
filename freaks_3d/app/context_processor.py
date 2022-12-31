#Lo que hace este procesador de contexto es guardar los cambios globalmente en la aplicacion
def full_bill(request):    
    total = 0
    if request.user.is_authenticated:
        if "cart" in request.session.keys():
            for key,value in request.session["cart"].items():
                total += int(value["accumulated"])
    
    return {"full_bill":total}
    