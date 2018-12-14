from decimal import Decimal

class Polar:
    """
    Defines a Polar Observation


    """

    def __init__(self, *,
                 station_id=None,
                 target_id=None,
                 station_point=None,
                 target_point=None,
                 station_height=None,
                 target_height=None,
                 horizontal_angle=None,
                 vertical_angle=None,
                 zenith_angle=None,
                 horizontal_angle_2=None,
                 vertical_angle_2=None,
                 zenith_angle_2=None,
                 azimuth=None,
                 slope_distance=None,
                 slope_distance_2=None,
                 horizontal_distance=None,
                 vertical_distance=None,
                 offset_in_out=None,
                 offset_left_right=None):
        """

        :param station_id:
        :param target_id:
        :param station_point:
        :param target_point:
        :param station_height:
        :param target_height:
        :param horizontal_angle:
        :param vertical_angle:
        :param zenith_angle:
        :param horizontal_angle_2:
        :param vertical_angle_2:
        :param zenith_angle_2:
        :param azimuth:
        :param slope_distance:
        :param slope_distance_2:
        :param horizontal_distance:
        :param vertical_distance:
        :param offset_in_out:
        :param offset_left_right:
        """
        self.station_id = station_id
        self.target_id = target_id
        self.station_point = station_point
        self.target_point = target_point
        self.station_height = Decimal(station_height)
        self.target_height = Decimal(target_height)
        self.horizontal_angle = Decimal(horizontal_angle)
        self.vertical_angle = Decimal(vertical_angle)
        self.zenith_angle = Decimal(zenith_angle)
        self.horizontal_angle_2 = Decimal(horizontal_angle_2)
        self.vertical_angle_2 = Decimal(vertical_angle_2)
        self.zenith_angle_2 = Decimal(zenith_angle_2)
        self.azimuth = Decimal(azimuth)
        self.slope_distance = Decimal(slope_distance)
        self.slope_distance_2 = Decimal(slope_distance_2)
        self.horizontal_distance = Decimal(horizontal_distance)
        self.vertical_distance = Decimal(vertical_distance)
        self.offset_in_out = Decimal(offset_in_out)
        self.offset_left_right = Decimal(offset_left_right)
