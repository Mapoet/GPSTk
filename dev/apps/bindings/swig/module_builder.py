"""GPSTk module __init__.py generator. This file should NOT be run
manually, but scriped into the build system.
"""

import os


# Any object that is exactly a string in this list will be ignored
ignore_exact = [

]

# Any object that contains a string in this list will be ignored
ignore_patterns = [
'swigregister',
'gpstk_pylib',
'Stream',
'Position_',
'RinexObsHeader_',
]


def should_be_added(name):
    for pattern in ignore_patterns:
        if pattern in name:
            return False
    for pattern in ignore_exact:
        if pattern == name:
            return False
    if name[:1] == '_':
        return False
    else:
        return True


def main():
    # Create __init__.py file
    import gpstk_pylib
    namespace = dir(gpstk_pylib)
    out_file = open('__init__.py', 'w')
    out_file.write('"""The GPS Toolkit - an open source library to the satellite navigation community.\n"""\n')
    out_file.write('### This file is AUTO-GENERATED by module_builder.py. ###\n\n')
    for x in namespace:
        if should_be_added(x):
            out_file.write('from gpstk_pylib import ')
            out_file.write(x)
            out_file.write('\n')

    # Create gpstk folder, move things into it
    out_dir = 'gpstk/'
    files_to_move = ['gpstk_pylib.py', '__init__.py']

    # we don't know extension of library file, so search the directory:
    files = [f for f in os.listdir('.') if os.path.isfile(f)]
    for f in files:
        if '_gpstk_pylib' in f:
            files_to_move.append(f)

    if not os.path.exists(out_dir):
        os.makedirs(out_dir)
    for f in files_to_move:
        os.rename(f, out_dir + f)


if __name__ == '__main__':
    main()