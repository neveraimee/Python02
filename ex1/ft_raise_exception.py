def input_temperature(temp_str: str) -> int:
    Temperature = int(temp_str)
    if Temperature > 40:
        raise ValueError(f"{Temperature}°C is too hot for plants (max 40°C)")
    if Temperature < 0:
        raise ValueError(f"{Temperature}°C is too cold for plants (min 0°C)")
    return Temperature 


def test_temperature() -> None:
    print("=== Garden Temperature ===")
    print()
    print("Input data is '25'")
    try:
        result = input_temperature("25")
        print(f"Temperature is now {result}°C")
    except ValueError as e:
        print(f"Caught input_temperature error: {e}")
    print()
    print("Input data is 'abc'")
    try:
        result = input_temperature("abc")
    except ValueError as e:
        print(f"Caught input_temperature error: {e}")
    print()
    print("Input data is '100'")
    try:
        result = input_temperature("100")
    except ValueError as e:
        print(f"Caught input_temperature error: {e}")
    print()
    print("Input data is '-50'")
    try:
        result = input_temperature("-50")
    except ValueError as e:
        print(f"Caught input_temperature error: {e}")
    print()
    print("All tests completed - program didn't crash!")

if __name__ == "__main__":
    test_temperature()