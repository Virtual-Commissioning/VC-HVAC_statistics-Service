prefixes = "@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .\n\
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .\n\
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .\n\
\n\
@prefix fso: <https://w3id.org/fso#> .\n\
\n\
@prefix inst: <https://example.com/inst#> .\n\
@prefix ex: <https://example.com/ex#> .\n\
\n\n"

#ifc_file = ifcopenshell.open("../../rawdata/02.00.04_test6.ifc")

ifc_types = {"IfcPipeSegment": "Pipe",
             "IfcFlowFitting": "Fitting",
             "IfcValve": "RegulationValve",
             "IfcPump": "Pump",
             "IfcFlowTerminal": "Terminal",
             "IfcSystem": "System"
            }

supply_temp = 60
return_temp = 40

fluid_type = "water"