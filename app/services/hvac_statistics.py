def is_ventilation(subsystem):
    if subsystem["Type"] == "ventilation":
        return True

def is_heating(subsystem):
    if subsystem["Type"] == "cooling":
        return True

def is_cooling(subsystem):
    if subsystem["Type"] == "heating":
        return True

def is_ventilation_duct(component):
    if component["ComponentType"] == "FlowSegment":
        return True

def map_ventilation_duct(component):
    

def statistics_calculation(data):
    cooling_components = {}
    heating_components = {}
    ventilation_components = {}
    types_of_components = []
    statistics_of_components = {}

    all_components = data["system"]["SubSystems"]

    for subsystem in all_components:
        
        for component in subsystem:
            
            if is_ventilation(subsystem):
                if is_ventilation_duct(component):
                    map_ventilation_duct(component)

            else:
                component["ComponentType"] in types_of_components:
                statistics_of_components[component["ComponentType"]["No. of Components"]] += 1
                
            else:
                statistics_of_components[component["ComponentType"]["No. of Components"]] == 1



json = {
    "AirTerminal": {
        "Nr. of Components": 100
    },
    "Duct": {
        ""
    }

}

