import argparse
import datetime

def main():
    parser = argparse.ArgumentParser(description='Get Timestamp in UTC.')
    parser.add_argument('timestamp_low', type=int, help='The low part of the timestamp')
    parser.add_argument('timestamp_high', type=int, help='The high part of the timestamp')
    args = parser.parse_args()
    
    timestamp_low = args.timestamp_low
    timestamp_high = args.timestamp_high
    
    full_timestamp = (timestamp_high << 32) | (timestamp_low & 0xFFFFFFFF)
    timestamp_seconds = full_timestamp / 10**7
    timestamp = datetime.datetime(1601, 1, 1) + datetime.timedelta(seconds=timestamp_seconds)
    
    print(timestamp)

if __name__ == '__main__':
    main()
