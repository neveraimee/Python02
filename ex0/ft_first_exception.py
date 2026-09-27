def input_temperature(temp_str: str) -> int:
    return int(temp_str)

def test_temperature() -> None:
    print("=== Garden Temperature ===")
    print()
    print("Input data is '25'")
    result = input_temperature("25")
    print(f"Temperature is now {result}°C")
    print()
    print("Input data is 'abc'")
    try:
        result = input_temperature("abc")
    except ValueError as e:
        print(f"Caught input_temperature error: {e}")
    print()
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()
