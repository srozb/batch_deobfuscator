from setuptools import setup, find_packages

setup(
    name='batch_deobfuscator',
    version='1.0',
    description='Transforms Batchfile Nightmares Into Blue Team Dream Warriors',
    author='@DissectMalware',
    url='https://github.com/DissectMalware/batch_deobfuscator/',
    packages=find_packages(),
    
    # Console scripts entry point
    entry_points={
        'console_scripts': [
            'batch-deobfuscator=batch_deobfuscator.cli:main',
        ],
    },
    
    # Dependencies (if any)
    install_requires=[
        # Add any dependencies here if needed
        # Based on the code, it might need these:
        # 'tempfile',  # built-in
        # 'os',        # built-in
        # 'copy',      # built-in
    ],
    
    # Python version requirement
    python_requires='>=3.6',
    
    # Additional metadata
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'Topic :: Security',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
    ],
    
    keywords='batch deobfuscation malware analysis security',
    
    long_description="""
    Batch Deobfuscator
    ==================
    
    A tool to deobfuscate batch scripts obfuscated using string substitution 
    and escape character techniques commonly used by malware.
    
    Usage:
        batch-deobfuscator input.bat
        batch-deobfuscator obfuscated.bat --output deobfuscated.bat
    """,
    long_description_content_type='text/markdown',
)
