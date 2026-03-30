from app.resources.data import EMPLOYEES_DATA

def search_employees(department: str = None, location: str = None) -> dict:
    """Search employees by department and/or location."""
    results = EMPLOYEES_DATA

    if department:
        results = [e for e in results if e["department"].lower() == department.lower()]

    if location:
        results = [e for e in results if e["location"].lower() == location.lower()]

    return {
        "total": len(results),
        "employees": results
    }