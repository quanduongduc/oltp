import os

OLTP_DB_HOST = os.getenv("OLTP_DB_HOST", "localhost")
OLTP_DB_PORT = int(os.getenv("OLTP_DB_PORT", 3306))
OLTP_DB_USER = os.getenv("OLTP_DB_USER", "root")
OLTP_DB_PASS = os.getenv("OLTP_DB_PASS", "root")

OLAP_DB_HOST = os.getenv("OLAP_DB_HOST", "localhost")
OLAP_DB_PORT = int(os.getenv("OLAP_DB_PORT", 3306))
OLAP_DB_USER = os.getenv("OLAP_DB_USER", "root")
OLAP_DB_PASS = os.getenv("OLAP_DB_PASS", "root")
