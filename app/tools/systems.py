from app.resources.data import SYSTEMS_DATA

def get_system_status(system_name: str = None) -> dict:
    """Get the operational status of corporate systems."""
    if system_name:
        system = SYSTEMS_DATA.get(system_name.lower())
        if not system:
            available = list(SYSTEMS_DATA.keys())
            return {
                "error": f"System '{system_name}' not found.",
                "available_systems": available
            }
        return {system_name: system}

    # Si no se especifica sistema, retorna todos
    summary = {
        "total_systems": len(SYSTEMS_DATA),
        "operational": len([s for s in SYSTEMS_DATA.values() if s["status"] == "operational"]),
        "degraded": len([s for s in SYSTEMS_DATA.values() if s["status"] == "degraded"]),
        "down": len([s for s in SYSTEMS_DATA.values() if s["status"] == "down"]),
        "systems": SYSTEMS_DATA
    }
    return summary