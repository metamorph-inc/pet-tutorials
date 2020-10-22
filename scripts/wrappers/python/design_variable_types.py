from __future__ import print_function
from openmdao.api import Component
from pprint import pprint



class DesignVariableTypes(Component):

    def __init__(self):
        super(DesignVariableTypes, self).__init__()

        self.add_param('foo1', val=u'', pass_by_obj=True)
        self.add_param('bar1', val=u'', pass_by_obj=True)
        self.add_param('foo2', val=u'', pass_by_obj=True)
        self.add_param('bar2', val=u'', pass_by_obj=True)
        self.add_param('foo3', val=u'', pass_by_obj=True)
        self.add_param('bar3', val=u'', pass_by_obj=True)
        self.add_param('foo4', val=u'', pass_by_obj=True)
        self.add_param('bar4', val=u'', pass_by_obj=True)
        self.add_param('foo5', val=u'', pass_by_obj=True)
        self.add_param('bar5', val=u'', pass_by_obj=True)
        self.add_param('x', val=0.0)
        self.add_param('y', val=0.0)
        self.add_param('z', val=0.0)
        self.add_param('foo', val=u'', pass_by_obj=True)
        self.add_param('bar', val=u'', pass_by_obj=True)
        self.add_param('z01', val=0.0)
        self.add_param('z02', val=0.0)
        self.add_param('z03', val=0.0)
        self.add_param('z04', val=0.0)
        self.add_param('z05', val=0.0)
        self.add_param('z06', val=0.0)
        self.add_param('z07', val=0.0)
        self.add_param('z08', val=0.0)
        self.add_param('z09', val=0.0)
        self.add_param('z10', val=0.0)
        self.add_param('z11', val=0.0)
        self.add_param('z12', val=0.0)
        self.add_param('z13', val=0.0)
        self.add_param('z14', val=0.0)
        self.add_param('z15', val=0.0)
        self.add_param('z16', val=0.0)
        self.add_param('z17', val=0.0)
        self.add_param('z18', val=0.0)
        self.add_param('z19', val=0.0)
        self.add_param('z20', val=0.0)
        self.add_param('z21', val=0.0)
        self.add_param('z22', val=0.0)
        self.add_param('z23', val=0.0)
        self.add_param('z24', val=0.0)
        self.add_param('z25', val=0.0)
        self.add_param('z26', val=0.0)
        self.add_param('z27', val=0.0)
        self.add_param('z28', val=0.0)
        self.add_param('z29', val=0.0)
        self.add_param('z30', val=0.0)
        self.add_param('z31', val=0.0)
        self.add_param('z32', val=0.0)
        self.add_param('z33', val=0.0)
        self.add_param('z34', val=0.0)
        self.add_param('z35', val=0.0)
        self.add_param('z36', val=0.0)
        self.add_param('z37', val=0.0)
        self.add_param('z38', val=0.0)
        self.add_param('z39', val=0.0)
        self.add_param('z40', val=0.0)
        self.add_param('z41', val=0.0)
        self.add_param('z42', val=0.0)
        self.add_param('z43', val=0.0)
        self.add_param('z44', val=0.0)
        self.add_param('z45', val=0.0)
        self.add_param('z46', val=0.0)
        self.add_param('z47', val=0.0)
        self.add_param('z48', val=0.0)
        self.add_param('z49', val=0.0)
        self.add_param('z50', val=0.0)
        self.add_param('z51', val=0.0)
        self.add_param('z52', val=0.0)
        self.add_param('z53', val=0.0)
        self.add_param('z54', val=0.0)
        self.add_param('z55', val=0.0)
        self.add_param('z56', val=0.0)
        self.add_param('z57', val=0.0)
        self.add_param('z58', val=0.0)
        self.add_param('z59', val=0.0)
        self.add_param('z60', val=0.0)
        self.add_param('z61', val=0.0)
        self.add_param('z62', val=0.0)
        self.add_param('z63', val=0.0)
        self.add_param('z64', val=0.0)
        self.add_param('z65', val=0.0)
        self.add_param('z66', val=0.0)
        self.add_param('z67', val=0.0)
        self.add_param('z68', val=0.0)
        self.add_param('z69', val=0.0)

        self.add_output('f_xy', shape=1)
        self.add_output('f_xz', shape=1)
        self.add_output('f_yz', shape=1)
        self.add_output('f_0', val=0.0)
        self.add_output('f_1', val=0.0)
        self.add_output('f_2', val=0.0)
        self.add_output('f_3', val=0.0)
        self.add_output('f_4', val=0.0)
        self.add_output('f_5', val=0.0)
        self.add_output('f_6', val=0.0)
        self.add_output('f_7', val=0.0)
        self.add_output('f_8', val=0.0)
        self.add_output('f_9', val=0.0)
        self.add_output('f_10', val=0.0)
        self.add_output('f_11', val=0.0)
        self.add_output('f_12', val=0.0)
        self.add_output('f_13', val=0.0)
        self.add_output('f_14', val=0.0)
        self.add_output('f_15', val=0.0)
        self.add_output('f_16', val=0.0)
        self.add_output('f_17', val=0.0)
        self.add_output('f_18', val=0.0)
        self.add_output('f_19', val=0.0)
        self.add_output('f_20', val=0.0)
        self.add_output('f_21', val=0.0)
        self.add_output('f_22', val=0.0)
        self.add_output('f_23', val=0.0)
        self.add_output('f_24', val=0.0)
        self.add_output('f_25', val=0.0)
        self.add_output('f_26', val=0.0)
        self.add_output('f_27', val=0.0)
        self.add_output('f_28', val=0.0)
        self.add_output('f_29', val=0.0)
        self.add_output('f_30', val=0.0)
        self.add_output('f_31', val=0.0)
        self.add_output('f_32', val=0.0)
        self.add_output('f_33', val=0.0)
        self.add_output('f_34', val=0.0)
        self.add_output('f_35', val=0.0)
        self.add_output('f_36', val=0.0)
        self.add_output('f_37', val=0.0)
        self.add_output('f_38', val=0.0)
        self.add_output('f_39', val=0.0)
        self.add_output('f_40', val=0.0)
        self.add_output('f_41', val=0.0)
        self.add_output('f_42', val=0.0)
        self.add_output('f_43', val=0.0)
        self.add_output('f_44', val=0.0)
        self.add_output('f_45', val=0.0)
        self.add_output('f_46', val=0.0)
        self.add_output('f_47', val=0.0)
        self.add_output('f_48', val=0.0)
        self.add_output('f_49', val=0.0)
        self.add_output('f_50', val=0.0)
        self.add_output('f_51', val=0.0)
        self.add_output('f_52', val=0.0)
        self.add_output('f_53', val=0.0)
        self.add_output('f_54', val=0.0)
        self.add_output('f_55', val=0.0)
        self.add_output('f_56', val=0.0)
        self.add_output('f_57', val=0.0)
        self.add_output('f_58', val=0.0)
        self.add_output('f_59', val=0.0)
        self.add_output('f_60', val=0.0)
        self.add_output('f_61', val=0.0)
        self.add_output('f_62', val=0.0)
        self.add_output('f_63', val=0.0)
        self.add_output('f_64', val=0.0)
        self.add_output('f_65', val=0.0)
        self.add_output('f_66', val=0.0)
        self.add_output('f_67', val=0.0)
        self.add_output('f_68', val=0.0)
        self.add_output('f_69', val=0.0)
        self.add_output('f_70', val=0.0)
        self.add_output('f_71', val=0.0)
        self.add_output('f_72', val=0.0)
        self.add_output('f_73', val=0.0)
        self.add_output('f_74', val=0.0)
        self.add_output('f_75', val=0.0)
        self.add_output('f_76', val=0.0)
        self.add_output('f_77', val=0.0)
        self.add_output('f_78', val=0.0)
        self.add_output('f_79', val=0.0)
        self.add_output('f_80', val=0.0)
        self.add_output('f_81', val=0.0)
        self.add_output('f_82', val=0.0)
        self.add_output('f_83', val=0.0)
        self.add_output('f_84', val=0.0)
        self.add_output('f_85', val=0.0)
        self.add_output('f_86', val=0.0)
        self.add_output('f_87', val=0.0)
        self.add_output('f_88', val=0.0)
        self.add_output('f_89', val=0.0)
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

        unknowns['f_0'] = x
        unknowns['f_1'] = x
        unknowns['f_2'] = x
        unknowns['f_3'] = x
        unknowns['f_4'] = x
        unknowns['f_5'] = x
        unknowns['f_6'] = x
        unknowns['f_7'] = x
        unknowns['f_8'] = x
        unknowns['f_9'] = x
        unknowns['f_10'] = x
        unknowns['f_11'] = x
        unknowns['f_12'] = x
        unknowns['f_13'] = x
        unknowns['f_14'] = x
        unknowns['f_15'] = x
        unknowns['f_16'] = x
        unknowns['f_17'] = x
        unknowns['f_18'] = x
        unknowns['f_19'] = x
        unknowns['f_20'] = x
        unknowns['f_21'] = x
        unknowns['f_22'] = x
        unknowns['f_23'] = x
        unknowns['f_24'] = x
        unknowns['f_25'] = x
        unknowns['f_26'] = x
        unknowns['f_27'] = x
        unknowns['f_28'] = x
        unknowns['f_29'] = x
        unknowns['f_30'] = x
        unknowns['f_31'] = x
        unknowns['f_32'] = x
        unknowns['f_33'] = x
        unknowns['f_34'] = x
        unknowns['f_35'] = x
        unknowns['f_36'] = x
        unknowns['f_37'] = x
        unknowns['f_38'] = x
        unknowns['f_39'] = x
        unknowns['f_40'] = x
        unknowns['f_41'] = x
        unknowns['f_42'] = x
        unknowns['f_43'] = x
        unknowns['f_44'] = x
        unknowns['f_45'] = x
        unknowns['f_46'] = x
        unknowns['f_47'] = x
        unknowns['f_48'] = x
        unknowns['f_49'] = x
        unknowns['f_50'] = x
        unknowns['f_51'] = x
        unknowns['f_52'] = x
        unknowns['f_53'] = x
        unknowns['f_54'] = x
        unknowns['f_55'] = x
        unknowns['f_56'] = x
        unknowns['f_57'] = x
        unknowns['f_58'] = x
        unknowns['f_59'] = x
        unknowns['f_60'] = x
        unknowns['f_61'] = x
        unknowns['f_62'] = x
        unknowns['f_63'] = x
        unknowns['f_64'] = x
        unknowns['f_65'] = x
        unknowns['f_66'] = x
        unknowns['f_67'] = x
        unknowns['f_68'] = x
        unknowns['f_69'] = x
        unknowns['f_70'] = x
        unknowns['f_71'] = x
        unknowns['f_72'] = x
        unknowns['f_73'] = x
        unknowns['f_74'] = x
        unknowns['f_75'] = x
        unknowns['f_76'] = x
        unknowns['f_77'] = x
        unknowns['f_78'] = x
        unknowns['f_79'] = x
        unknowns['f_80'] = x
        unknowns['f_81'] = x
        unknowns['f_82'] = x
        unknowns['f_83'] = x
        unknowns['f_84'] = x
        unknowns['f_85'] = x
        unknowns['f_86'] = x
        unknowns['f_87'] = x
        unknowns['f_88'] = x
        unknowns['f_89'] = x
