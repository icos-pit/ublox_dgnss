""" Launch ublox_dgnss_node publishing high precision Lon/Lat messages"""
import launch
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch.substitutions import TextSubstitution, EnvironmentVariable
from launch_ros.actions import ComposableNodeContainer
from launch_ros.descriptions import ComposableNode


def generate_launch_description():
  """Generate launch description for ublox_dgnss components."""

  use_https_arg = DeclareLaunchArgument(
    "use_https", default_value=TextSubstitution(text="false")
  )
  host_arg = DeclareLaunchArgument(
    "host", default_value=TextSubstitution(text="91.198.76.2")
  )
  port_arg = DeclareLaunchArgument(
    "port", default_value=TextSubstitution(text="8086")
  )
  mountpoint_arg = DeclareLaunchArgument(
    "mountpoint", default_value=TextSubstitution(text="BOR1_RTCM_3_2")
  )
  username_arg = DeclareLaunchArgument(
    "username", default_value=EnvironmentVariable(name="NTRIP_USERNAME", default_value="iman01")
  )
  password_arg = DeclareLaunchArgument(
    "password", default_value=EnvironmentVariable(name="NTRIP_PASSWORD", default_value="Iman0101")
  )
  params = [{
    'use_https': LaunchConfiguration('use_https'),
    'host': LaunchConfiguration('host'),
    'port': LaunchConfiguration('port'),
    'mountpoint': LaunchConfiguration('mountpoint'),
    'username': LaunchConfiguration('username'),
    'password': LaunchConfiguration('password')
  }]

  container1 = ComposableNodeContainer(
    name='ntrip_client_container',
    namespace='',
    package='rclcpp_components',
    executable='component_container_mt',
    composable_node_descriptions=[
      ComposableNode(
        package='ntrip_client_node',
        plugin='ublox_dgnss::NTRIPClientNode',
        name='ntrip_client',
        parameters=params
      )
    ]
  )

  return launch.LaunchDescription([
    use_https_arg,
    host_arg,
    port_arg,
    mountpoint_arg,
    username_arg,
    password_arg,
    container1
  ])
