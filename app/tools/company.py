from app.resources.data import COMPANY_DATA

def get_company_info(company_id: str) -> dict:
    """Get detailed information about a company by its ID."""
    company = COMPANY_DATA.get(company_id.lower())
    
    if not company:
        available = list(COMPANY_DATA.keys())
        return {
            "error": f"Company '{company_id}' not found.",
            "available_companies": available
        }
    
    return company