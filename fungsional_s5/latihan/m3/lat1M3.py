def time_conversion(data):
    total_minutes = 0

    for time_string in data:
        value, unit = time_string.split()
        value = int(value)

        if unit == "minggu":
            total_minutes += value * 7 * 24 * 60
        elif unit == "hari":
            total_minutes += value * 24 * 60
        elif unit == "jam":
            total_minutes += value * 60
        elif unit == "menit":
            total_minutes += value

    return total_minutes

def main():
    data1 = ["3 minggu", "3 hari", "7 jam", "21 menit"]
    data2 = ["5 minggu", "5 hari", "8 jam", "11 menit"]
    data3 = ["7 minggu", "1 hari", "5 jam", "33 menit"]  # Data tambahan

    result1 = time_conversion(data1)
    result2 = time_conversion(data2)
    result3 = time_conversion(data3)

    # Output data pertama ["2 minggu", "3 hari", "5 jam", "30 menit"] dan total waktu dalam menit
    print("data:")
    print(data1)
    print(data2)
    print(data3)
    print([result1, result2, result3])
  
if __name__ == "__main__":
    main()


