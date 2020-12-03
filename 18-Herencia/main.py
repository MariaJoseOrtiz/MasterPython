import clases

persona = clases.Persona()
persona.setNombre("Maria")
persona.setApellido("Ortiz")
persona.setAltura("190cm")
persona.setEdad("800 anos")

print(f"La persona es:  {persona.getNombre() } { persona.getApellido()}")
print("---------------------------------------------------")
informatico= clases.Informatico()

informatico.setNombre("Carlos")
informatico.setApellido("Martinez")

print(f"El informatico es : {informatico.getApellido()} {informatico.getNombre()}")
print(informatico.getLenguajes())

print("---------------------------------------------------")

tecnico= clases.TecnicoRedes()
print(tecnico.auditoria(),tecnico.getLenguajes())
