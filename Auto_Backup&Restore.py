import subprocess
# Backup PostgreSQL Database
def Backup():
    subprocess.run(["pg_database","-U" "Username","-d","databse" "=f" "backup.sql"])
    print("Database backup completed")

Backup()