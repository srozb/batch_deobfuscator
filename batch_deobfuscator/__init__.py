"""
Batch Deobfuscator Package

A tool to deobfuscate batch scripts obfuscated using string substitution
and escape character techniques commonly used by malware.
"""

from .batch_interpreter import BatchDeobfuscator, handle_bat_file

__version__ = "1.0"
__author__ = "@DissectMalware"

__all__ = ["BatchDeobfuscator", "handle_bat_file"]
