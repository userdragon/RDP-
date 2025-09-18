import logging
import os
from pathlib import Path
from .config import config_manager

class Logger
    def __init__(self)
        # 获取日志级别配置
        log_level_str = config_manager.get(master, log_level, INFO).upper()
        log_level = getattr(logging, log_level_str, logging.INFO)
        
        # 初始化日志目录
        self.log_dir = self._get_log_dir()
        self.log_dir.mkdir(parents=True, exist_ok=True)
        
        # 配置日志
        self.logger = logging.getLogger(sync_remote_control)
        self.logger.setLevel(log_level)
        
        # 避免重复添加处理器
        if not self.logger.handlers
            self._setup_handlers()

    def _get_log_dir(self)
        获取日志目录
        if os.name == nt
            return Path(os.environ.get(APPDATA))  sync-remote-control  logs
        else
            return Path.home()  .config  sync-remote-control  logs

    def _setup_handlers(self)
        设置日志处理器
        # 格式化日志
        formatter = logging.Formatter(
            %(asctime)s - %(name)s - %(levelname)s - %(message)s
        )
        
        # 控制台处理器
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        self.logger.addHandler(console_handler)
        
        # 文件处理器
        log_file = self.log_dir  app.log
        file_handler = logging.FileHandler(log_file, encoding=utf-8)
        file_handler.setFormatter(formatter)
        self.logger.addHandler(file_handler)

    def get_logger(self)
        获取日志实例
        return self.logger

# 单例模式的日志实例
logger = Logger().get_logger()
