#!/usr/bin/env python3

import time
import sys

from pymodbus.constants import Endian
from pymodbus.payload import BinaryPayloadDecoder
from pymodbus import exceptions
from pymodbus.client.sync import ModbusTcpClient


def start_dryer(client: ModbusTcpClient) -> None:
    write_value(client, 6018, 1)


def stop_dryer(client: ModbusTcpClient) -> None:
    write_value(client, 6018, 0)


def reboot_dryer(client: ModbusTcpClient) -> None:
    write_value(client, 6020, 1)


def write_value(client, register, value) -> None:
    while True:
        try:
            start = time.time()
            client.write_register(register, value)

            if register != 6020:
                for ctr in range(8):
                    read_once(client, register)
                    time.sleep(1.25)
                    print("Time: ", round(time.time() - start, 3))

                break
            else:
                print("Reboot command is sent to Dryer DRY 2.1")
                break
        except exceptions.ConnectionException:
            connection_troubleshooting()
            exit(1)


def read_once(client, register) -> None:
    states = {
        257: "Waiting for Power",
        259: "Stopped by User",
        262: "Standby",
        263: "Waiting for Pressure",
        265: "Idle",
        513: "Drying 0",
        514: "Cooling 0",
        769: "Drying 1",
        770: "Cooling 1",
        1281: "Error"}

    while True:
        try:
            result = client.read_holding_registers(register, 1)
            decoder = BinaryPayloadDecoder.fromRegisters(
                result.registers, byteorder=Endian.Big, wordorder=Endian.Big)

            code = decoder.decode_16bit_int()
            print("================")
            if code in states:
                print("Dryer state: " + states[code])
            else:
                print("Dryer state: " + str(code))

            break
        except exceptions.ConnectionException:
            connection_troubleshooting()
            exit(1)
        except AttributeError:
            print(
                '''Could not read Dryer DRY 2.1 Modbus registers. Please check that:
    - Dryer DRY 2.1 and Electrolyser EL 2.1 are connected to the same Dryer Control \
Network;
    - Dryer DRY 2.1 is powered on.''', file=sys.stderr)
            exit(1)


def show_help() -> None:
    print("Usage: python " +
          sys.argv[0] + "EL 2.1 <Modbus IP address> start|stop|reboot", file=sys.stderr)
    exit(1)


def connection_troubleshooting() -> None:
    print(
        '''Failed to connect to Modbus TCP client. Please check that:
    - Dryer DRY 2.1 and Electrolyser EL 2.1 are connected to the same DCN/IDCN;
    - Entered Electrolyser EL 2.1 Modbus IP address is correct;
    - Enapter Electrolyser EL 2.1 is connected to your PC or to Wi-Fi router via Ethernet;
    - Your PC is connected to Local Area Network.''', file=sys.stderr)


if __name__ == '__main__':
    if len(sys.argv) != 3:
        show_help()
    else:
        ip_address = sys.argv[1]
        client = ModbusTcpClient(ip_address, timeout=50)

        command = sys.argv[2]
        if command == "start":
            start_dryer(client)
        elif command == "stop":
            stop_dryer(client)
        elif command == "reboot":
            reboot_dryer(client)
        else:
            show_help()
