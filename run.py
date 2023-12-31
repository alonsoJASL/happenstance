import os
import argparse
from datetime import datetime
import happenstance.common.happenstance as hppns

def main(args) : 
    # Example lambdas (adjust these based on your preferences)
    lambdas = [args.small, args.medium, args.large]
    H = hppns.Happenstance(lambdas=lambdas, num_days=args.num_days, start_date=args.start_date) 

    formats = []
    if args.ics:
        formats.append("ics")
    
    if args.csv:
        formats.append("csv")

    if len(formats) == 0:
        formats.append("ics")

    for format in formats:
        output_path = os.path.join(args.base_dir, f'{args.output}.{format}')
        H.save_calendar(output_path, format=format)
    

if __name__ == '__main__' :
    
    input_parser = argparse.ArgumentParser(description='Generate a calendar of random dates for happenstance gestures.')
    input_parser.add_argument("-dir", "--base-dir", type=str, default=".", help="Base directory to save the calendar.")
    input_parser.add_argument("-output", "--output", type=str, default="happenstance", help="Output file name.")
    input_parser.add_argument('--start-date', type=lambda s: datetime.strptime(s, '%Y-%m-%d'), help='Custom start date in the format YYYY-MM-DD')
    input_parser.add_argument("--num-days", type=int, default=90, help="Number of days to generate events for.")
    input_parser.add_argument("--small", type=float, default=0.15, help="Lambda for small gestures.")
    input_parser.add_argument("--medium", type=float, default=0.075, help="Lambda for medium gestures.")
    input_parser.add_argument("--large", type=float, default=0.025, help="Lambda for large gestures.")
    input_parser.add_argument("--ics", action="store_true", help="Save the calendar ics file.")
    input_parser.add_argument("--csv", action="store_true", help="Save the calendar as a csv file instead of an ics file.")

    args = input_parser.parse_args()
    main(args)
