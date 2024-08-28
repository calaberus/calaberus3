class dispositivos_electronicos:
    def __init__(self, marca, modelo, atributo):
        self.atributo=atributo
        self.marca=marca
        self.modelo=modelo
redmi=dispositivos_electronicos("redmi","12c","gama alta")
iphone=dispositivos_electronicos("iphone","14 pro max","camara")

print(type(redmi))
print(type(iphone))

print(F"la marca es={redmi.marca},el modelo es={redmi.modelo},el atributo es={redmi.atributo}")
print(F"la marca es={iphone.marca},el modelo es={iphone.modelo},su atributo es={iphone.atributo}")