from Repositorios.InterfazRepositorio import InterfazRepositorio
from Modelos.Resultado import Resultado
from bson import ObjectId

class ResultadoRepositorio(InterfazRepositorio[Resultado]):
    #Obterner los canditatos inscritos en una mesa
    def getListadoCandidatosInscritosMesa(self, id_mesa):
        theQuery = {"mesa.$id": ObjectId(id_mesa)}
        return self.query(theQuery)

    #Listado de mesas en las que un candidato está inscrito
    def getListadoMesasCandidatoInscrito(self, id_candidato):
        theQuery = {"candidato.$id": ObjectId(id_candidato)}
        return self.query(theQuery)
    
    #Devuelve el numero de cédula mayor
    def getNumeroCedulaMayorCandidato(self):
        query1 = {
            "$group":{
                "_id": "$candidato",
                "max": {
                    "$max": "$cedula"
                },
                "doc": {"$first": "$$ROOT"
                }
                
            }
        }
        pipeline = [query1]
        return self.queryAggregation(pipeline)