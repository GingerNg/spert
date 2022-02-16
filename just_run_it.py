import argparse
import spert_entry

arg_parser = argparse.ArgumentParser(add_help=False)
arg_parser.add_argument('mode', type=str, help="Mode: 'train' or 'eval'")
args, _ = arg_parser.parse_known_args()
print(args)
if args.mode == 'train':
    print("start")
    spert_entry.train()