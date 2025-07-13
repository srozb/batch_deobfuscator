#!/usr/bin/env python3
"""
Command-line interface for batch_deobfuscator
"""
import argparse
import sys
import os
from batch_deobfuscator.batch_interpreter import BatchDeobfuscator, handle_bat_file


def main():
    """Main CLI entry point"""
    parser = argparse.ArgumentParser(
        description='Deobfuscate batch scripts obfuscated using string substitution and escape character techniques',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  batch-deobfuscator input.bat
  batch-deobfuscator obfuscated.bat --output deobfuscated.bat
  batch-deobfuscator malware.bat --verbose
        """
    )
    
    parser.add_argument(
        'input_file',
        help='Path to the obfuscated batch file'
    )
    
    parser.add_argument(
        '-o', '--output',
        help='Output file path (default: stdout)',
        default=None
    )
    
    parser.add_argument(
        '-v', '--verbose',
        action='store_true',
        help='Enable verbose output'
    )
    
    parser.add_argument(
        '--version',
        action='version',
        version='batch_deobfuscator 1.0'
    )
    
    args = parser.parse_args()
    
    # Check if input file exists
    if not os.path.isfile(args.input_file):
        print(f"Error: Input file '{args.input_file}' does not exist.", file=sys.stderr)
        sys.exit(1)
    
    try:
        # Create deobfuscator instance
        if args.verbose:
            print(f"Processing file: {args.input_file}", file=sys.stderr)
        
        deobfuscator = BatchDeobfuscator()
        result = handle_bat_file(deobfuscator, args.input_file)
        
        # Format output
        if isinstance(result, list):
            output_text = '\n'.join(str(line) for line in result)
        else:
            output_text = str(result)
        
        # Write output
        if args.output:
            with open(args.output, 'w', encoding='utf-8') as f:
                f.write(output_text)
            if args.verbose:
                print(f"Deobfuscated content written to: {args.output}", file=sys.stderr)
        else:
            print(output_text)
            
        if args.verbose:
            print(f"Deobfuscation completed successfully.", file=sys.stderr)
            
    except Exception as e:
        print(f"Error during deobfuscation: {e}", file=sys.stderr)
        if args.verbose:
            import traceback
            traceback.print_exc()
        sys.exit(1)


if __name__ == '__main__':
    main()
