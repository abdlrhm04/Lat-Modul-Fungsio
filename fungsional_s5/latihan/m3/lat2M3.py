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
    data3 = ["7 minggu", "1 hari", "5 jam", "33 menit"]

    # Menggunakan filter untuk mengambil hanya nilai integer
    data1_integers = list(filter(lambda x: x.isdigit(), [item.split()[0] for item in data1]))
    data2_integers = list(filter(lambda x: x.isdigit(), [item.split()[0] for item in data2]))
    data3_integers = list(filter(lambda x: x.isdigit(), [item.split()[0] for item in data3]))

    # Menampilkan hanya output yang berisi nilai integer
    print(data1_integers)
    print(data2_integers)
    print(data3_integers)

if __name__ == "__main__":
    main()
