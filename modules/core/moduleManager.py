def register_module(name=None):
    def decorator(cls):
        module_name = name or cls.__name__
        ModuleManager.register(module_name, cls)
        return cls

    return decorator


class ModuleManager:
    registry = {}

    @classmethod
    def register(cls, name, module_cls):
        print(f"Registering {name}")
        try:
            cls.registry[name] = module_cls
        except Exception as e:
            print(e)
        print(f"Registered {module_cls}")

    @classmethod
    def create(cls, name, *args, **kwargs):
        module_cls = cls.registry.get(name, None)
        if module_cls is None:
            raise KeyError(f"No module named {name}")
        return module_cls(*args, **kwargs)

    @classmethod
    def list_modules(cls) -> list[str]:
        return list(cls.registry.keys())

    @classmethod
    def get_module(cls, name):
        if name in cls.list_modules():
            return cls.registry[name]
        else:
            raise KeyError(f"No module named {name}")
