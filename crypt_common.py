import argparse

def add_parser_args(parser):
    parser.add_argument('text', metavar='Text', nargs='*',
                        help='The text to parse')
    parser.add_argument('--file', dest='file', nargs=1,
                        help='Read text from file')
    return parser


def sort_dict(to_sort):
    return sorted(to_sort.keys(), key=lambda k: to_sort[k], reverse=True)



def get_text(args):
    text = ""
    if args.text and args.file:
        raise Exception("Use either text or file, not both at once")
    if args.text:
        text = ' '.join(args.text)
    elif args.file:
        with open(args.file[0], 'r') as myfile:
            text=myfile.read().replace('\n', '')
    else:
        raise Exception('No text given')
    return text
