"""
Contains unit tests for mod:`reference_frames.py`
"""
import unittest
import numpy as np
import reference_frames as frames
__author__ = 'Michal Kononenko'


class TestReferenceFrame(unittest.TestCase):

    def setUp(self):
        self.frame = frames.ReferenceFrame()
        self.start_time = 0
        self.end_time = 1e-7
        self.number_of_points = 1000

        self.time_list = np.linspace(
            self.start_time, self.end_time, self.number_of_points
        )

        self.frame.time_list = self.time_list


class TestReferenceFrameDefaultArgs(unittest.TestCase):

    def setUp(self):
        self.frame = frames.ReferenceFrame()

    def test_default_args(self):
        expected_time_list = np.array([0, 0])
        np.testing.assert_array_equal(
            expected_time_list, self.frame.time_list)


class TestStartTime(TestReferenceFrame):

    def setUp(self):
        super().setUp()
        self.new_time = 1

    def test_start_time_getter(self):
        self.assertEqual(self.frame.start_time, self.start_time)

    def test_start_time_setter(self):
        self.frame.start_time = self.new_time
        self.assertEqual(self.frame.start_time, self.new_time)

        expected_time_list = np.linspace(self.new_time, self.end_time,
                                         self.number_of_points)
        np.testing.assert_array_equal(expected_time_list, self.frame.time_list)


class TestEndTime(TestReferenceFrame):

    def setUp(self):
        super().setUp()
        self.new_time = 1

    def test_end_time_getter(self):
        self.assertEqual(self.frame.end_time, self.end_time)

    def test_end_time_setter(self):
        self.frame.end_time = self.new_time
        self.assertEqual(self.frame.end_time, self.new_time)

        expected_time_list = np.linspace(
            self.start_time, self.new_time, self.number_of_points
        )

        np.testing.assert_array_equal(expected_time_list, self.frame.time_list)


class TestNumberOfPoints(TestReferenceFrame):
    def setUp(self):
        super().setUp()
        self.new_number_of_points = 10000

    def test_number_of_points_getter(self):
        self.assertEqual(self.frame.number_of_points, self.number_of_points)

    def test_number_of_points_setter(self):
        self.frame.number_of_points = self.new_number_of_points
        self.assertEqual(self.frame.number_of_points, self.new_number_of_points
                         )

        expected_time_list = np.linspace(
            self.start_time, self.end_time, self.new_number_of_points
        )
        np.testing.assert_array_equal(expected_time_list, self.frame.time_list)


class TestRotatingFrame(unittest.TestCase):
    def setUp(self):
        self.frequency = 1e6
        self.frame = frames.RotatingFrame(self.frequency)
        self.start_time = 0
        self.end_time = 1e-7
        self.number_of_points = 1000

        self.time_list = np.linspace(
            self.start_time, self.end_time, self.number_of_points
        )

        self.frame.time_list = self.time_list

class TestGetRotationOperator(TestRotatingFrame):
    def setUp(self):
        super().setUp()
        self.times_to_calc = np.array([0, np.pi/2])
