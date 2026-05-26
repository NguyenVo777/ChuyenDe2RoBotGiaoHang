import rclpy
from rclpy.node import Node
from rclpy.action import ActionClient

from nav2_msgs.action import NavigateToPose
from geometry_msgs.msg import PoseStamped

class DeliveryRobot(Node):

    def __init__(self):
        super().__init__('delivery_robot_node')

        self.nav_client = ActionClient(
            self,
            NavigateToPose,
            'navigate_to_pose'
        )

    def send_goal(self, x, y):

        self.get_logger().info(
            f'Dang di chuyen den x={x}, y={y}'
        )

        self.nav_client.wait_for_server()

        goal_msg = NavigateToPose.Goal()

        goal_msg.pose.header.frame_id = 'map'

        goal_msg.pose.pose.position.x = float(x)
        goal_msg.pose.pose.position.y = float(y)

        goal_msg.pose.pose.orientation.w = 1.0

        send_goal_future = self.nav_client.send_goal_async(goal_msg)

        rclpy.spin_until_future_complete(
            self,
            send_goal_future
        )

        goal_handle = send_goal_future.result()

        if not goal_handle.accepted:

            self.get_logger().info('Goal bi tu choi')

            return False

        result_future = goal_handle.get_result_async()

        rclpy.spin_until_future_complete(
            self,
            result_future
        )

        return True


def main(args=None):

    rclpy.init(args=args)

    robot = DeliveryRobot()

    KHO_X = 0.0
    KHO_Y = 0.0

    KHACH_X = 2.5
    KHACH_Y = 1.5

    MA_PIN = "1234"

    print("\nBAT DAU GIAO HANG")

    robot.send_goal(KHACH_X, KHACH_Y)

    print("\nDA DEN NOI")

    while True:

        pin = input("Nhap ma PIN: ")

        if pin == MA_PIN:

            print("PIN dung")

            break

        else:

            print("PIN sai")

    print("\nQUAY VE KHO")

    robot.send_goal(KHO_X, KHO_Y)

    print("\nHOAN TAT")

    robot.destroy_node()

    rclpy.shutdown()


if __name__ == '__main__':
    main()
