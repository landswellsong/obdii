import elm
import obdii
import sys
import time

def main():
    port = sys.argv[1]
    interval = len(sys.argv) > 2 and float(sys.argv[2]) or 1.0

    adapter = elm.Elm(port)
    obd = obdii.Obdii(adapter)
    
    pids = obd.get_supported_pids(0x01)
    
    print >>sys.stderr, "Supported PIDs:"
    print >>sys.stderr, pids
    
    
    print 'UNIX time, Intake Temperature, Intake Pressure, Engine load, Engine RPM, Vehicle Speed, Coolant Temperature'

    while True:
        tmp = obd.get_current_intake_air_temp()
        prs = obd.get_current_intake_air_pressure()
        eld = obd.get_current_engine_load()
        rpm = obd.get_current_engine_rpm()
        spd = obd.get_vehicle_speed()
        ect = obd.get_current_ect()

        print "%d, %d, %d, %d, %d, %d, %d" % (time.clock(), tmp, prs, eld, rpm, spd, ect)
        time.sleep(interval)


if __name__ == '__main__':
    main()
