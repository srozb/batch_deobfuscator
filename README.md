# Introduction
By using this python script, you can deobfuscate a batch script that is obfuscated with string substitution and escape character techniques.

## Quick start

```bash
uv tool install git+https://github.com/srozb/batch_deobfuscator
```

## Running the script
To run the script 

```bash
python  batch_interpreter.py --file c:\test\obfuscated_file.bat
```

The code was written in a hurry and needs a major refactoring. Please stay tuned.

## Use as a lib

```python
from batch_deobfuscator.batch_interpreter import BatchDeobfuscator,handle_bat_file
deobfuscator = BatchDeobfuscator()
itsthewine=handle_bat_file(deobfuscator,'/home/petersichel/comfortable_study/newyorktownhouse.bat')
```
