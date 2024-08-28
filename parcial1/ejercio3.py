class casa_automotris:
    def __init__(self, marca, modelo, caballos_de_fuerza):
        self.marca=marca
        self.modelo=modelo
        self.caballo_de_fuerza=caballos_de_fuerza
ferrari=casa_automotris("ferrari","296 GTB","205 mhp")
kawasaki=casa_automotris("kawasaki","H2R","400 km/h")

print(type(ferrari))
print(type(kawasaki))

print(F"la marca es={ferrari.marca},el modelo es={ferrari.modelo}, sus caballos de fuerza son={ferrari.caballo_de_fuerza}")
print(F"la marca es={kawasaki.marca},el modelo es={kawasaki.modelo},su velocidad MAX es={kawasaki.caballo_de_fuerza}")