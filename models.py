import pandas as pd
import numpy as np

def get_kpi_data():
    return {
        "perf": {"val": "92%", "delta": "+3.1%"},
        "gdiz": {"val": "1,240 t", "delta": "Flux GDIZ"},
        "stocks": {"val": "88%", "delta": "Occupation"},
        "service": {"val": "95.5%", "delta": "+0.8%"}
    }

def get_truck_flow_data():
    # Simulation d'un flux de camions sur 24h
    heures = list(range(0, 24))
    flux = [5, 3, 2, 2, 10, 30, 85, 120, 150, 140, 110, 100, 90, 110, 130, 160, 145, 100, 70, 50, 40, 30, 20, 10]
    return pd.DataFrame({"Heure": heures, "Nombre de Camions": flux})

def get_shipment_data():
    data = [
        {"ID": "BJ-101", "Transporteur": "COBEMAG", "Origine": "Port Cotonou", "Dest.": "GDIZ", "Statut": "Livré"},
        {"ID": "BJ-102", "Transporteur": "Bénin Log", "Origine": "GDIZ", "Dest.": "Parakou", "Statut": "En cours"},
        {"ID": "BJ-103", "Transporteur": "Africa Trans", "Origine": "Port Cotonou", "Dest.": "Malanville", "Statut": "Retard"},
    ]
    return pd.DataFrame(data)
        
