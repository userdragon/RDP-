from src.core.common.config import config_manager

def test_config_initialization():
    """测试配置管理器初始化是否正常"""
    assert config_manager is not None

def test_default_config_values():
    """测试默认配置值是否正确"""
    # 测试master部分默认配置
    assert config_manager.get("master", "port") == 5000
    assert config_manager.get("master", "log_level") == "INFO"
    
    # 测试slave部分默认配置
    assert config_manager.get("slave", "reconnect_interval") == 5
    
    # 测试gui部分默认配置
    assert config_manager.get("gui", "theme") == "light"

def test_config_set_get():
    """测试配置的设置和获取功能"""
    # 保存原始值以便恢复
    original_value = config_manager.get("master", "sync_delay")
    
    # 测试设置新值
    config_manager.set("master", "sync_delay", 0.1)
    assert config_manager.get("master", "sync_delay") == 0.1
    
    # 恢复原始值
    config_manager.set("master", "sync_delay", original_value)
