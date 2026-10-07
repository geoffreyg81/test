from functools import wraps


def log_method(func):
    @wraps(func)
    def inner(*args, **kwargs):
        print(f"[LOG] {func.__name__}")
        result = func(*args, **kwargs)
        return result

    return inner


def valider(func):
    @wraps(func)
    def inner(*args, **kwargs):
        # On vérifie les arguments classiques
        for arg in args:
            if isinstance(arg, (int, float)) and arg < 0:
                raise ValueError(f"Erreur de validation : la valeur {arg} ne peut pas être négative.")

        # On vérifie les arguments nommés (correction du {value})
        for key, value in kwargs.items():
            if isinstance(value, (int, float)) and value < 0:
                raise ValueError(f"Erreur de validation : la valeur {value} ne peut pas être négative.")

        return func(*args, **kwargs)

    return inner