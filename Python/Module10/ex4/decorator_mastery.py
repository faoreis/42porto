import random
import time
from typing import Callable, Any
from functools import wraps


def spell_timer(func: Callable) -> Callable:

    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        print(f"Casting {func.__name__}...")
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        execution_time = end_time - start_time
        print(f"Spell completed in {execution_time:.3f} seconds")
        return result

    return wrapper


def power_validator(min_power: int) -> Callable:

    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            power = kwargs.get('power')

            if power is None and args:
                power = args[0]

            if power is not None and power < min_power:
                return "Insufficient power for this spell"

            return func(*args, **kwargs)

        return wrapper
    return decorator


def retry_spell(max_attempts: int) -> Callable:

    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:

            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    print(
                        f"Spell failed, retrying... "
                        f"(attempt {attempt}/{max_attempts})"
                    )

            return f"Spell casting failed after {max_attempts} attempts"

        return wrapper
    return decorator


@spell_timer
def fireball_spell() -> str:
    time.sleep(0.5)
    return "Fireball cast!"


@power_validator(min_power=70)
def ultimate_spell(power: int, spell_name: str) -> str:
    return f"{spell_name}: {power} power!"


@retry_spell(max_attempts=10)
def spell_casting() -> str:
    num = random.randint(0, 10)
    if num <= 6:
        raise ValueError("Erro")
    return "Waaaaaaagh spelled !"


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        return len(name) >= 3 and name.replace(" ", "").isalpha()

    @power_validator(min_power=10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with {power} power"


def main() -> None:
    print("Testing spell timer...")
    result_timer = fireball_spell()
    print("Result:", result_timer)
    print("\nTesting spell power validator...")
    print(ultimate_spell(105, "ultimate"))
    print("\nTesting retrying spell...")
    print(spell_casting())
    print("\nTesting MageGuild...")
    mage = MageGuild()
    mage1 = MageGuild()
    print(mage.validate_mage_name("teste"))
    print(mage1.validate_mage_name("teste1"))
    print(mage.cast_spell("Lightning", power=15))
    print(mage.cast_spell("fireball", power=9))


if __name__ == "__main__":
    main()
