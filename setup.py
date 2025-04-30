import os
import sys
import subprocess

def run_command(command):
    print(f"Running: {command}")
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error running command: {command}")
        print(f"Error: {result.stderr}")
        sys.exit(1)
    print(result.stdout)

def main():
    # Create virtual environment if it doesn't exist
    if not os.path.exists("venv"):
        print("Creating virtual environment...")
        run_command("python -m venv venv")
    
    # Activate virtual environment
    if sys.platform == "win32":
        activate_script = "venv\\Scripts\\activate"
    else:
        activate_script = "source venv/bin/activate"
    
    # Install dependencies
    print("Installing dependencies...")
    run_command(f"{activate_script} && pip install -r app/requirements.txt")
    
    # Run migrations
    print("Running database migrations...")
    run_command(f"{activate_script} && python migrate.py")
    
    # Initialize database
    print("Initializing database...")
    run_command(f"{activate_script} && python init_db.py")
    
    print("Setup complete! You can now run the application with:")
    print("python run.py")

if __name__ == "__main__":
    main() 