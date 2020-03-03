from __future__ import print_function
from openmdao.api import Component
from pprint import pprint



class DesignVariableTypes(Component):

    def __init__(self):
        super(DesignVariableTypes, self).__init__()

        self.add_param('x', val=0.0)
        self.add_param('y', val=0.0)
        self.add_param('z', val=0.0)
        self.add_param('foo', val=u'', pass_by_obj=True)
        self.add_param('bar', val=u'', pass_by_obj=True)

        self.add_output('f_xy', shape=1)
        self.add_output('f_xz', shape=1)
        self.add_output('f_yz', shape=1)
        self.add_output('foobar', val=u'', pass_by_obj=True)

    def solve_nonlinear(self, params, unknowns, resids):

        x = params['x']
        y = params['y']
        z = params['z']
        foo = params['foo']
        bar = params['bar']

        unknowns['f_xy'] = (x-3.0)**2 + x*y + (y+4.0)**2 - 3.0
        unknowns['f_xz'] = x + z
        unknowns['f_yz'] = y + z
        unknowns['foobar'] = foo + bar
