from app.config import Settings

def test_config_defaults():
    settings = Settings()
    assert settings.app_name == "Lisa"
    assert settings.mode == "dev"
    assert settings.chat_native is True
    assert settings.dashboard_enabled is False
