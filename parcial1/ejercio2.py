class edifio:
    def __init__(self, ubicacion, tamaño, diseño):
        self.ubicacion=ubicacion
        self.tamaño=tamaño
        self.diseño=diseño
apartamento=edifio("urbano","cuarto planatas","un espacio para una familia de 6")
apartamento2=edifio("rural","de una planta","uni familiar")

print(type(apartamento))
print(type(apartamento2))

print(F"la ubicacion es= {apartamento.ubicacion} ,el tamaño es= {apartamento.tamaño} ,el diseño es= {apartamento.diseño}")
print(F"la ubicacion es= {apartamento2.ubicacion} ,el tamaño es= {apartamento2.tamaño} ,su diseño es= {apartamento2.diseño}")