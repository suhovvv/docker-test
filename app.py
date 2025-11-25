import requests
import os

def main():
    print("🚀 Dockerized Python App работает!")
    print(f"Контейнер: {os.environ.get('HOSTNAME', 'Неизвестно')}")
    
if __name__ == "__main__":
    main()
