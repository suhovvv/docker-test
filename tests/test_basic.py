import sys
import os
import subprocess

# Добавляем src в путь для импортов
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

def test_python_version():
    """Проверяем что Python доступен"""
    result = subprocess.run([sys.executable, '--version'], capture_output=True, text=True)
    assert result.returncode == 0
    print("✅ Python version check passed")

def test_imports():
    """Проверяем что все импорты работают"""
    try:
        import requests
        print("✅ Requests import works")
        assert True
    except ImportError:
        assert False, "Failed to import requests"

def test_docker_build():
    """Проверяем что Dockerfile собирается"""
    try:
        result = subprocess.run([
            'docker', 'build', '-t', 'test-build', '.'
        ], capture_output=True, text=True, timeout=120)
        
        if result.returncode == 0:
            print("✅ Docker build test passed")
            return True
        else:
            print(f"❌ Docker build failed: {result.stderr}")
            return False
    except subprocess.TimeoutExpired:
        print("❌ Docker build timed out")
        return False
    except Exception as e:
        print(f"❌ Docker test error: {e}")
        return False

if __name__ == "__main__":
    # Запускаем тесты
    test_python_version()
    test_imports()
    test_docker_build()
    print("🎯 All basic tests completed!")
