from networktables import NetworkTables, NetworkTablesInstance
import json
import threading

teamNumber = 540
version = "1.0.0"


def main():
    connection_condition = threading.Condition()
    # define notified as a list variable b/c python cannot access
    # primitive types from methods and lists are considered objects. Python sucks balls.
    connection_notified = [False]

    def connectionListener(isConnected: bool, info):
        print(info, '; Connected=%s' % isConnected)
        with connection_condition:
            connection_notified[0] = True
            connection_condition.notify()

    NetworkTables.startClientTeam(team=teamNumber)
    NetworkTables.addConnectionListener(
        connectionListener, immediateNotify=True)

    with connection_condition:
        print("Waiting for connection to NetworkTables")
        if not connection_notified[0]:
            connection_condition.wait()

    # Get the Default Table
    talon_table = NetworkTablesInstance.getDefault().getTable(key='Talon')
    # put the current version of the system, useful for debugging
    talon_table.putString("version", version)
    # put object specific data in a specific table, useful for multi-state changes
    object_data_table = talon_table.getSubTable('detection')

    # whatever bs ayush pal code

    example_raw_data = {
        "predictions": [
            {
                "x": 191,
                "y": 285,
                "width": 204,
                "height": 212,
                "confidence": 0.878,
                "class": "cones"
            }
        ]
    }
    
    example_latency_ms = 23
    
    object_data_table.putNumber("latency", example_latency_ms)
    # I can reconvert this in client code, this allows me to have acess to all of the raw data I could need
    object_data_table.putString("rawData", json.dumps(example_raw_data))

if __name__ == "__main__":
    main()
