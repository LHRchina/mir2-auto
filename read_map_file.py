import struct
from datetime import datetime, timedelta


def read_header(file_name):
    # Define the structure format
    # 'H' for unsigned short (word), '16s' for 16-char array, 'd' for double (TDateTime), '24s' for 24-char array
    struct_format = 'HH16sd24s'

    # Calculate the size of the structure
    struct_size = struct.calcsize(struct_format)

    # Read the binary file
    with open(file_name, 'rb') as file:
        data = file.read(struct_size)

    # Unpack the data
    width, height, title, update_date, reserved = struct.unpack(struct_format, data)

    # Convert the title and reserved to strings
    title = title.decode('latin-1').strip('\x00')
    reserved = reserved.decode('latin-1').strip('\x00')

    # Convert the TDateTime to a Python datetime object
    # TDateTime is the number of days since 1899-12-30
    base_date = datetime(1899, 12, 30)
    update_date = base_date + timedelta(days=update_date)

    # Print the unpacked data
    print(f"Width: {width}")
    print(f"Height: {height}")
    print(f"Title: {title}")
    print(f"Update Date: {update_date}")
    print(f"Reserved: {reserved}")
