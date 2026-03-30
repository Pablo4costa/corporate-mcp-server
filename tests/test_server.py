import pytest
from app.tools.company import get_company_info
from app.tools.employees import search_employees
from app.tools.systems import get_system_status

def test_get_company_info_found():
    result = get_company_info("acme-corp")
    assert result["name"] == "Acme Corporation"
    assert result["industry"] == "Technology"

def test_get_company_info_not_found():
    result = get_company_info("unknown-corp")
    assert "error" in result
    assert "available_companies" in result

def test_search_employees_by_department():
    result = search_employees(department="Engineering")
    assert result["total"] == 4
    assert all(e["department"] == "Engineering" for e in result["employees"])

def test_search_employees_by_location():
    result = search_employees(location="Remote")
    assert result["total"] == 2

def test_search_employees_all():
    result = search_employees()
    assert result["total"] == 8

def test_get_system_status_all():
    result = get_system_status()
    assert result["total_systems"] == 6
    assert result["degraded"] == 1

def test_get_system_status_specific():
    result = get_system_status("api-gateway")
    assert "api-gateway" in result
    assert result["api-gateway"]["status"] == "operational"

def test_get_system_status_not_found():
    result = get_system_status("unknown-system")
    assert "error" in result