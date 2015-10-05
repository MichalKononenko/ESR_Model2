"""
Contains definitions for reference frames
"""
import numpy as np
import qutip as q

__author__ = 'Michal Kononenko'


class ReferenceFrame(object):
    """
    Contains an abstract model for a reference frame. The time axis
    is given
    """
    def __init__(self, time_list=np.array([0, 0])):
        self.time_list = time_list

    @property
    def start_time(self):
        r"""
        Returns the start time of the simulation
        """
        return self.time_list[0]

    @start_time.setter
    def start_time(self, new_start_time):
        """
        Sets the start time of the simulation by updating the time list
        """
        time_array = np.linspace(
            new_start_time, self.end_time, self.number_of_points
        )
        self.time_list = time_array

    @property
    def end_time(self):
        return self.time_list[len(self.time_list) - 1]

    @end_time.setter
    def end_time(self, new_end_time):
        time_array = np.linspace(
            self.start_time, new_end_time, self.number_of_points
        )
        self.time_list = time_array

    @property
    def number_of_points(self):
        return len(self.time_list)

    @number_of_points.setter
    def number_of_points(self, new_number_of_points):
        time_array = np.linspace(
            self.start_time, self.end_time, new_number_of_points
        )
        self.time_list = time_array


class RotatingFrame(ReferenceFrame):
    """
    Models a rotating frame
    """

    def __init__(self, frequency):
        self.frequency = frequency
        ReferenceFrame.__init__(self)

    def get_rotation_operator(self, time):
        r"""
        Return the rotation matrix to move from the Lab frame to this
        rotating frame. In :math:`SU(2)`, this matrix is given as

        .. math::
            \left(\begin{array}{c c}
                \cos(\Omega t) & \sin(\Omega t) \\
                -\sin(\Omega t) & \cos(\Omega t)
            \end{array}\right)

        Or

        .. math::
            \cos(\Omega t) \mathbb{I} + i \sin(\Omega t)\sigma_y

        :param array-like time: The times for which the rotation operator is
            to be calculated
        :return:
        """

        return np.cos(self.frequency * time) * q.qeye(2) + \
            1j * np.sin(self.frequency * time) * q.sigmay()
