#!/usr/bin/env python
"""
Quick setup script for Honey Chain Django project
Run: python setup.py
"""
import os
import sys
import subprocess
from pathlib import Path


def setup_project():
    """Setup the Django project"""
    
    print("🍯 Honey Chain - Django Setup Script")
    print("=" * 50)
    
    # Get project root
    PROJECT_ROOT = Path(__file__).parent
    
    # Step 1: Check Python version
    print("\n1. Checking Python version...")
    if sys.version_info < (3, 9):
        print("❌ Python 3.9+ is required")
        sys.exit(1)
    print(f"✅ Python {sys.version.split()[0]}")
    
    # Step 2: Install dependencies
    print("\n2. Installing dependencies...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", str(PROJECT_ROOT / "requirements.txt")])
        print("✅ Dependencies installed")
    except subprocess.CalledProcessError:
        print("❌ Failed to install dependencies")
        sys.exit(1)
    
    # Step 3: Create .env file
    print("\n3. Setting up environment...")
    env_file = PROJECT_ROOT / ".env"
    env_example = PROJECT_ROOT / ".env.example"
    
    if not env_file.exists() and env_example.exists():
        with open(env_example) as f:
            content = f.read()
        with open(env_file, 'w') as f:
            f.write(content)
        print("✅ .env file created from .env.example")
    
    # Step 4: Database migrations
    print("\n4. Setting up database...")
    try:
        os.chdir(PROJECT_ROOT)
        subprocess.check_call([sys.executable, "manage.py", "makemigrations"])
        subprocess.check_call([sys.executable, "manage.py", "migrate"])
        print("✅ Database migrations completed")
    except subprocess.CalledProcessError:
        print("⚠️  Database setup encountered issues")
    
    # Step 5: Create superuser
    print("\n5. Creating admin account...")
    response = input("Do you want to create a superuser? (y/n): ").lower()
    if response == 'y':
        try:
            subprocess.call([sys.executable, "manage.py", "createsuperuser"])
            print("✅ Superuser created")
        except KeyboardInterrupt:
            print("⚠️  Skipped superuser creation")
    
    # Step 6: Collect static files
    print("\n6. Collecting static files...")
    try:
        subprocess.check_call([sys.executable, "manage.py", "collectstatic", "--noinput"])
        print("✅ Static files collected")
    except subprocess.CalledProcessError:
        print("⚠️  Static files collection encountered issues")
    
    print("\n" + "=" * 50)
    print("✅ Setup completed successfully!")
    print("\nNext steps:")
    print("1. Update .env with your settings (especially BLOCKCHAIN_NETWORK)")
    print("2. Start the development server: python manage.py runserver")
    print("3. Access admin panel at: http://127.0.0.1:8000/admin/")
    print("4. API documentation: http://127.0.0.1:8000/api/")
    print("\n🍯 Happy Beekeeping!")


if __name__ == "__main__":
    setup_project()
