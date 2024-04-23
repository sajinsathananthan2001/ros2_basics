#include "rclcpp/rclcpp.hpp"
#include "example_interfaces/msg/string.hpp"

class StringPublisher : public rclcpp::Node 
{
public:
    StringPublisher() : Node("string_publisher") 
    {
        publisher = this->create_publisher<example_interfaces::msg::String>("string_msg", 10);
        timer = this->create_wall_timer(std::chrono::milliseconds(500),
                                         std::bind(&StringPublisher::publishStringCB, this));
        RCLCPP_INFO(this->get_logger(), "String publisher started!");
    }

private:

    void publishStringCB()
    {
        auto msg = example_interfaces::msg::String();
        msg.data = std::string("Hi Im from string publisher node!");
        publisher->publish(msg);
    }

    rclcpp::Publisher<example_interfaces::msg::String>::SharedPtr publisher;
    rclcpp::TimerBase::SharedPtr timer;


};

int main(int argc, char **argv)
{
    rclcpp::init(argc, argv);
    auto node = std::make_shared<StringPublisher>();
    rclcpp::spin(node);
    rclcpp::shutdown();
    return 0;
}
