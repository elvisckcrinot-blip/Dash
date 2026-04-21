import pandas as pd

def get_kpi_data():
    return {
        "perf": {"val": "92%", "delta": "+3.1%"},
        "gdiz": {"val": "1,240 t", "delta": "Flux GDIZ"},
        "stocks": {"val": "88%", "delta": "Occupation"},
        "service": {"val": "95.5%", "delta": "+0.8%"}
    }

def get_shipment_data():
    # Simulation de données réelles Bénin
    data = [
        {"ID": "BJ-101", "Transporteur": "COBEMAG", "Origine": "Port Cotonou", "Dest.": "GDIZ", "Statut": "Livré"},
        {"ID": "BJ-102", "Transporteur": "Bénin Log", "Origine": "GDIZ", "Dest.": "Parakou", "Statut": "En cours"},
        {"ID": "BJ-103", "Transporteur": "Africa Trans", "Origine": "Port Cotonou", "Dest.": "Malanville", "Statut": "Retard"},
    ]
    return pd.DataFrame(data)
         
