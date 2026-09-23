import yaml




class Config(object):

    def __init__(self, config_path):
        self._config = self.load_config(config_path)
        self._flatten_config()

    @staticmethod
    def load_config(config_path):
        """加载 YAML 配置文件"""
        with open(config_path, 'r', encoding='utf-8') as file:
            config = yaml.safe_load(file)
        return config

    def __str__(self):
        return str(self._config)

    def _flatten_config(self):
        for key, value in self._config.items():
            if isinstance(value, dict):
                for sub_key, sub_value in value.items():
                    setattr(self, f"{sub_key}", sub_value)
            else:
                setattr(self, key, value)

    def __getattr__(self, name):
        if name in self._config:
            return self._config[name]
        raise AttributeError(f"'{self.__class__.__name__}' object has no attribute '{name}'")

    def get(self, key, default=None):
        keys = key.split('.')
        value = self._config
        for k in keys:
            if isinstance(value, dict) and k in value:
                value = value[k]
            else:
                return default
        return value