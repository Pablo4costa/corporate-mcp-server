# Datos simulados corporativos
# En producción estos vendrían de una base de datos real

COMPANY_DATA = {
    "acme-corp": {
        "name": "Acme Corporation",
        "industry": "Technology",
        "founded": 1995,
        "employees_count": 5200,
        "headquarters": "New York, USA",
        "revenue": "$2.3B",
        "description": "Leading provider of enterprise software solutions"
    },
    "globex": {
        "name": "Globex Corporation",
        "industry": "Manufacturing",
        "founded": 1982,
        "employees_count": 12000,
        "headquarters": "Chicago, USA",
        "revenue": "$8.7B",
        "description": "Global manufacturing and logistics company"
    }
}

EMPLOYEES_DATA = [
    {"id": 1, "name": "Alice Johnson", "department": "Engineering", "role": "Senior DevOps Engineer", "location": "New York"},
    {"id": 2, "name": "Bob Smith", "department": "Engineering", "role": "AI Engineer", "location": "Remote"},
    {"id": 3, "name": "Carol White", "department": "HR", "role": "HR Manager", "location": "Chicago"},
    {"id": 4, "name": "David Brown", "department": "Engineering", "role": "Backend Developer", "location": "New York"},
    {"id": 5, "name": "Eve Davis", "department": "Finance", "role": "Financial Analyst", "location": "Chicago"},
    {"id": 6, "name": "Frank Miller", "department": "HR", "role": "Recruiter", "location": "Remote"},
    {"id": 7, "name": "Grace Wilson", "department": "Engineering", "role": "ML Engineer", "location": "New York"},
    {"id": 8, "name": "Henry Moore", "department": "Finance", "role": "CFO", "location": "Chicago"},
]

SYSTEMS_DATA = {
    "api-gateway": {"status": "operational", "uptime": "99.98%", "latency_ms": 45},
    "database-primary": {"status": "operational", "uptime": "99.99%", "latency_ms": 12},
    "database-replica": {"status": "operational", "uptime": "99.95%", "latency_ms": 15},
    "cache-redis": {"status": "operational", "uptime": "99.97%", "latency_ms": 3},
    "ml-inference": {"status": "degraded", "uptime": "98.20%", "latency_ms": 320},
    "storage-s3": {"status": "operational", "uptime": "99.99%", "latency_ms": 85},
}