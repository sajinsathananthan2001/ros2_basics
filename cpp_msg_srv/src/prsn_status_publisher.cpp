#include "rclcpp/rclcpp.hpp"
#include "custom_interfaces/msg/person_status.hpp"

class StatusPublisher : public rclcpp::Node 
{
public:
    StatusPublisher() : Node("string_publisher") 
    {
        publisher = this->create_publisher<custom_interfaces::msg::PersonStatus>("person_status", 10);
        timer = this->create_wall_timer(std::chrono::milliseconds(500),
                                         std::bind(&StatusPublisher::publishStatusCB, this));
        RCLCPP_INFO(this->get_logger(), "Status publisher started!");
    }

private:

    void publishStatusCB()
    {
        auto msg = custom_interfaces::msg::PersonStatus();
        msg.name = std::string("Sajin Sathananthan");
        msg.available = true;
        msg.salary = 12000;
        publisher->publish(msg);
    }

    rclcpp::Publisher<custom_interfaces::msg::PersonStatus>::SharedPtr publisher;
    rclcpp::TimerBase::SharedPtr timer;


};

int main(int argc, char **argv)
{
    rclcpp::init(argc, argv);
    auto node = std::make_shared<StatusPublisher>();
    rclcpp::spin(node);
    rclcpp::shutdown();
    return 0;
}
