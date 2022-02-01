from cmath import sqrt
import math
import json
from types import NoneType


def is_ventilation(subsystem):
    return subsystem["Type"] == "ventilation"

def is_heating(subsystem):
    return subsystem["Type"] == "cooling"

def is_cooling(subsystem):
    return subsystem["Type"] == "heating"

def is_flow_segment(component):
    return component["ComponentType"] == "FlowSegment"

def length_of_segment(component):
    
    if component["ConnectedWith"][0] == "None" or component["ConnectedWith"][1] == "None":
        return None

    connector1_coordinates = component["ConnectedWith"][0]["Coordinate"]
    connector2_coordinates = component["ConnectedWith"][1]["Coordinate"]

    x1 = connector1_coordinates["X"]
    y1 = connector1_coordinates["Y"]
    z1 = connector1_coordinates["Z"]

    x2 = connector2_coordinates["X"]
    y2 = connector2_coordinates["Y"]
    z2 = connector2_coordinates["Z"]

    length_of_segment = round(math.sqrt(((x2 - x1)**2) + ((y2 - y1)**2) + ((z2 - z1)**2)),2)

    return length_of_segment

def is_rectangular(component):
    return component["ConnectedWith"][0]["Shape"] == "Rectangular"

def is_round(component):
    return component["ConnectedWith"][0]["Shape"] == "Round"

def has_null_connector(component):
    connectors = component["ConnectedWith"]
    
    for connector in connectors:
        if connector == "None":
            return True

def map_ventilation_duct(component):
    component_list = []
    
    if has_null_connector(component):
        component_size = "0"
        segment_length = 1
        component_list.append(component_size)
        component_list.append(segment_length)

    elif is_rectangular(component):
        segment_length = length_of_segment(component)
        component_size = str(component["ConnectedWith"][0]["Dimension"]).replace(" ", "")
        component_list.append(component_size)
        component_list.append(segment_length)

    elif is_round(component):
        segment_length = length_of_segment(component)
        component_size = str(component["ConnectedWith"][0]["Dimension"]).replace(" ", "")
        component_list.append(component_size)
        component_list.append(segment_length)

    return component_list

def map_hydronic_pipe(component):
    component_list = []
    segment_length = length_of_segment(component)
    component_size = str(component["ConnectedWith"][0]["Dimension"]).replace(" ", "")
    component_list.append(component_size)
    component_list.append(segment_length)

    return component_list

def map_component(component, types_of_components):
    if component["ComponentType"] not in types_of_components.keys():
        types_of_components[component["ComponentType"]] = {"No. of Components": 0}

    elif component["ComponentType"] in types_of_components.keys():
        types_of_components[component["ComponentType"]]["No. of Components"] += 1

    else:
        print("Something went wrong")

def statistics_calculation(data):
    hydronic_pipes = {}   
    ventilation_ducts = {}
    types_of_components = {}
    all_system = json.loads(data)
    all_components = all_system["system"]["SubSystems"]
    total_components = 0

    for subsystem in all_components.values():
        
        for component in subsystem["Components"]:
            total_components += 1

            if is_ventilation(subsystem):
                if is_flow_segment(component):
                    ventilation_duct = map_ventilation_duct(component)
                    ventilation_ducts[ventilation_duct[0]] = ventilation_duct[1]

                else:
                    map_component(component, types_of_components)
            
            elif is_heating(subsystem) or is_cooling(subsystem):
                if is_flow_segment(component):
                    hydronic_pipe = map_hydronic_pipe(component)
                    hydronic_pipes[hydronic_pipe[0]] = hydronic_pipe[1]

                else:
                    map_component(component, types_of_components)

            # else:
            #     raise Exception("Something went wrong in the mapping")

    statistics_of_components = {"Ventilation ducts": ventilation_ducts,
                                "Hydronic pipes": hydronic_pipes,
                                "Types of components": types_of_components,
                                "Total components": total_components}

    return json.dumps(statistics_of_components)