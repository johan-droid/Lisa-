from pydantic_settings import BaseSettings
from typing import Optional

class Settings(BaseSettings):
    app_name: str = "Lisa"
    mode: str = "dev"
    chat_native: bool = True
    dashboard_enabled: bool = False

    FREELLMAPI_BASE_URL: Optional[str] = None
    FREELLMAPI_API_KEY: Optional[str] = None
    FREELLMAPI_TIMEOUT_SECONDS: int = 30
    FREELLMAPI_ENABLE_TOKEN_BANK: bool = False
    FREELLMAPI_DEFAULT_MODEL: Optional[str] = None
    FREELLMAPI_ENABLE_FAST_MODEL_SWITCHING: bool = True
    FREELLMAPI_MAX_FALLBACKS_PER_REQUEST: int = 3

    AUTOPILOT_DEFAULT_TOKEN_BUDGET: int = 20000
    AUTOPILOT_MAX_TOKEN_BUDGET: int = 120000
    AUTOPILOT_SPIKE_TOKEN_BUDGET: int = 50000
    AUTOPILOT_MODEL_SWITCH_LATENCY_TARGET_MS: int = 1500
    AUTOPILOT_ENABLE_MODEL_ROUTING: bool = True
    AUTOPILOT_ENABLE_SPIKE_MODE: bool = True
    AUTOPILOT_MAX_LOOP_ITERATIONS: int = 5

    JUDICIAL_SUSPICION_PAUSE_THRESHOLD: float = 0.65
    JUDICIAL_SUSPICION_STOP_THRESHOLD: float = 0.85

    SANDBOX_PROVIDER: str = "local_simulator"
    SANDBOX_ENABLE_E2B: bool = False
    SANDBOX_ENABLE_CODESANDBOX: bool = False
    E2B_API_KEY: Optional[str] = None
    E2B_TEMPLATE_ID: Optional[str] = None
    E2B_TIMEOUT_SECONDS: int = 120
    CODESANDBOX_API_KEY: Optional[str] = None
    CODESANDBOX_TEMPLATE_ID: Optional[str] = None
    CODESANDBOX_TIMEOUT_SECONDS: int = 120
    SANDBOX_DEFAULT_MEMORY_MB: int = 512
    SANDBOX_DEFAULT_CPU_COUNT: int = 1
    SANDBOX_DEFAULT_TIMEOUT_SECONDS: int = 120
    SANDBOX_MAX_OUTPUT_BYTES: int = 200000
    SANDBOX_NETWORK_ENABLED: bool = False
    SANDBOX_SNAPSHOT_ENABLED: bool = True

    TOOL_DISCOVERY_ENABLE_ONLINE: bool = False
    TOOL_DISCOVERY_MAX_CANDIDATES: int = 5
    TOOL_QUARANTINE_REQUIRED: bool = True
    PRINCIPAL_APPROVAL_REQUIRED_FOR_TOOL_PROMOTION: bool = True

    class Config:
        env_file = ".env"

settings = Settings()
