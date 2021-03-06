# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *
import inspect


class PerlIoSocketSsl(PerlPackage):
    """SSL sockets with IO::Socket interface"""

    homepage = "http://search.cpan.org/~sullr/IO-Socket-SSL-2.052/lib/IO/Socket/SSL.pod"
    url      = "http://search.cpan.org/CPAN/authors/id/S/SU/SULLR/IO-Socket-SSL-2.052.tar.gz"

    version('2.052', '26c9bcdfb4ba8763ef89264f21326a48')

    depends_on('perl-net-ssleay', type=('build', 'run'))

    def configure(self, spec, prefix):
        self.build_method = 'Makefile.PL'
        self.build_executable = inspect.getmodule(self).make
        # Should I do external tests?
        config_answers = ['n\n']
        config_answers_filename = 'spack-config.in'

        with open(config_answers_filename, 'w') as f:
            f.writelines(config_answers)

        with open(config_answers_filename, 'r') as f:
            inspect.getmodule(self).perl('Makefile.PL', 'INSTALL_BASE={0}'.
                                         format(prefix), input=f)
