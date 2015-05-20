# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at http://mozilla.org/MPL/2.0/.
#
# Copyright (c) 2014-2015, Lars Asplund lars.anders.asplund@gmail.com

# Make vunit python module importable
from os.path import join, dirname
import sys
path_to_vunit = join(dirname(__file__), '..', '..')
sys.path.append(path_to_vunit)
#  -------

from vunit import VUnit

root = dirname(__file__)

ui = VUnit.from_argv()
ui.add_com()
tb_com_lib = ui.add_library("tb_com_lib")
tb_com_lib.add_source_files(join(root, 'test', '*.vhd'))
pkg = tb_com_lib.package('custom_types_pkg')
pkg.generate_codecs(codec_package_name='custom_codec_pkg', used_packages=['ieee.std_logic_1164'])
ui.main()
