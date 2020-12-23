# pylint: disable=invalid-name
# pylint: disable=bad-whitespace
# pylint: disable=no-self-use
# pylint: disable=too-many-statements
# pylint: disable=protected-access

"""Tests for Boundary reflection."""

import unittest
import numpy as np
from nose.plugins.attrib import attr
import iadpython

def wip(f):
    """
    Only test functions with @wip decorator.

    Add the @wip decorator before functions that are works-in-progress.
    `nosetests -a wip test_combo.py` will test only those with @wip decorator.
    """
    return attr('wip')(f)

class boundary(unittest.TestCase):
    """Boundary layer calculations."""

    def test_01_boundary(self):
        """Matrices for light entering slab."""
        n_glass = 1.5
        n_slab= 1.3
        s = iadpython.Sample(n=n_slab, n_above=n_glass, n_below=n_glass)
        r, t = iadpython.start._boundary(s, 1.0, n_glass, n_slab, 0)
        rr = np.array([0.08628,0.32200,0.03502,0.00807])
        tt = np.array([0.00000,0.00000,0.91484,0.95530])
        np.testing.assert_allclose(r, rr, atol=1e-5)
        np.testing.assert_allclose(t, tt, atol=1e-5)

    def test_02_boundary(self):
        """Matrices for light exiting slab."""
        n_glass = 1.5
        n_slab= 1.3
        s = iadpython.Sample(n=n_slab, n_above=n_glass, n_below=n_glass)
        r, t = iadpython.start._boundary(s, n_slab, n_glass, 1.0, 0)
        rr = np.array([0.08628,0.32200,0.03502,0.00807])
        tt = np.array([0.00000,0.00000,0.91484,0.95530])
        np.testing.assert_allclose(r, rr, atol=1e-5)
        np.testing.assert_allclose(t, tt, atol=1e-5)

    def test_03_boundary(self):
        """Initialization of boundary matrix without glass slides."""
        s = iadpython.Sample(n=1.5, n_above=1.0, n_below=1.0)
        rr = np.array([0.11740,0.43815,0.02393,0.00509])
        tt = np.array([0.00000,0.00000,0.92455,0.96000])
        r01, r10, t01, t10 = iadpython.boundary_layer(s,top=True)
        np.testing.assert_allclose(t01, tt, atol=1e-5)
        np.testing.assert_allclose(r10, rr, atol=1e-5)
        np.testing.assert_allclose(t10, tt, atol=1e-5)
        np.testing.assert_allclose(r01, rr, atol=1e-5)
        r01, r10, t01, t10 = iadpython.boundary_layer(s,top=False)
        np.testing.assert_allclose(t01, tt, atol=1e-5)
        np.testing.assert_allclose(r10, rr, atol=1e-5)
        np.testing.assert_allclose(t10, tt, atol=1e-5)
        np.testing.assert_allclose(r01, rr, atol=1e-5)

    def test_04_boundary(self):
        """Initialization of boundary matrix without glass slides."""
        s = iadpython.Sample(n=1.5, n_above=1.5, n_below=1.5)
        rr = np.array([0.11740,0.43815,0.02393,0.00509])
        tt = np.array([0.00000,0.00000,0.92455,0.96000])
        r01, r10, t01, t10 = iadpython.boundary_layer(s,top=True)
        np.testing.assert_allclose(t01, tt, atol=1e-5)
        np.testing.assert_allclose(r10, rr, atol=1e-5)
        np.testing.assert_allclose(t10, tt, atol=1e-5)
        np.testing.assert_allclose(r01, rr, atol=1e-5)
        r01, r10, t01, t10 = iadpython.boundary_layer(s,top=False)
        np.testing.assert_allclose(t01, tt, atol=1e-5)
        np.testing.assert_allclose(r10, rr, atol=1e-5)
        np.testing.assert_allclose(t10, tt, atol=1e-5)
        np.testing.assert_allclose(r01, rr, atol=1e-5)

    def test_05_boundary(self):
        """Initialization of boundary matrices with glass slides."""
        s = iadpython.Sample(n=1.3, n_above=1.5, n_below=1.5)
        rr = np.array([0.08628,0.32200,0.03502,0.00807])
        tt = np.array([0.00000,0.00000,0.91484,0.95530])
        r01, r10, t01, t10 = iadpython.boundary_layer(s,top=True)
        np.testing.assert_allclose(r01, rr, atol=1e-5)
        np.testing.assert_allclose(t01, tt, atol=1e-5)
        np.testing.assert_allclose(r10, rr, atol=1e-5)
        np.testing.assert_allclose(t10, tt, atol=1e-5)
        r01, r10, t01, t10 = iadpython.boundary_layer(s,top=False)
        np.testing.assert_allclose(r01, rr, atol=1e-5)
        np.testing.assert_allclose(t01, tt, atol=1e-5)
        np.testing.assert_allclose(r10, rr, atol=1e-5)
        np.testing.assert_allclose(t10, tt, atol=1e-5)

    def test_06_boundary(self):
        """Initialization of boundary matrices with glass slides."""
        s = iadpython.Sample(n=1.3, n_above=1.5, n_below=1.6)
        rr = np.array([0.08628,0.32200,0.03502,0.00807])
        tt = np.array([0.00000,0.00000,0.91484,0.95530])
        r01, r10, t01, t10 = iadpython.boundary_layer(s,top=True)
        np.testing.assert_allclose(r01, rr, atol=1e-5)
        np.testing.assert_allclose(t01, tt, atol=1e-5)
        np.testing.assert_allclose(r10, rr, atol=1e-5)
        np.testing.assert_allclose(t10, tt, atol=1e-5)
        r01, r10, t01, t10 = iadpython.boundary_layer(s,top=False)
        rr = np.array([0.08628,0.32200,0.04371,0.01135])
        tt = np.array([0.00000,0.00000,0.89370,0.93715])
        np.testing.assert_allclose(r01, rr, atol=1e-5)
        np.testing.assert_allclose(t01, tt, atol=1e-5)
        np.testing.assert_allclose(r10, rr, atol=1e-5)
        np.testing.assert_allclose(t10, tt, atol=1e-5)

if __name__ == '__main__':
    unittest.main()
