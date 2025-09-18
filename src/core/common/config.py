import os
import json
from pathlib import Path
from dotenv import load_dotenv

class ConfigManager:
    def __init__(self):
        # 初始化配置目录和文件路径
        self.config_dir = self._get_config_dir()
        self.config_file = self.config_dir / "config.json"
        self.default_config = self._get_default_config()
        
        # 加载环境变量
        load_dotenv()
        
        # 确保配置目录存在
        self.config_dir.mkdir(parents=True, exist_ok=True)
        
        # 加载配置
        self.config = self.load_config()

    def _get_config_dir(self):
        """获取系统特定的配置目录"""
        if os.name == "nt":  # Windows
            return Path(os.environ.get("APPDATA")) / "sync-remote-control"
        elif os.name == "posix":  # Linux/macOS
            return Path.home() / ".config" / "sync-remote-control"
        else:
            raise OSError(f"不支持的操作系统: {os.name}")

    def _get_default_config(self):
        """返回默认配置"""
        return {
            "master": {
                "port": 5000,
                "discovery_interval": 10,  # 设备发现间隔(秒)
                "sync_delay": 0.05,        # 同步延迟(秒)
                "log_level": "INFO"
            },
            "slave": {
                "master_ip": "",           # 默认主控IP(空表示自动发现)
                "port": 5000,
                "reconnect_interval": 5,   # 重连间隔(秒)
                "log_level": "INFO"
            },
            "gui": {
                "theme": "light",
                "window_size": "800x600"
            }
        }

    def load_config(self):
        """加载配置文件，如果不存在则创建默认配置"""
        try:
            if self.config_file.exists():
                with open(self.config_file, "r", encoding="utf-8") as f:
                    return json.load(f)
            else:
                self.save_config(self.default_config)
                return self.default_config
        except Exception as e:
            print(f"加载配置失败，使用默认配置: {e}")
            return self.default_config

    def save_config(self, config=None):
        """保存配置到文件"""
        if config is None:
            config = self.config
            
        try:
            with open(self.config_file, "w", encoding="utf-8") as f:
                json.dump(config, f, indent=2, ensure_ascii=False)
            return True
        except Exception as e:
            print(f"保存配置失败: {e}")
            return False

    def get(self, section, key=None, default=None):
        """获取配置值"""
        if key is None:
            return self.config.get(section, default)
        return self.config.get(section, {}).get(key, default)

    def set(self, section, key, value):
        """设置配置值"""
        if section not in self.config:
            self.config[section] = {}
        self.config[section][key] = value
        self.save_config()

# 单例模式的配置管理器
config_manager = ConfigManager()
