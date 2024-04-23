#include "rclcpp/rclcpp.hpp"
#include "example_interfaces/msg/string.hpp"

class StringSubscriber : public rclcpp::Node
{
public:
    StringSubscriber() : Node("string_subscriber")
    {
        subscriber = this->create_subscription<example_interfaces::msg::String>(
            "string_msg", 10,
            std::bind(&StringSubscriber::callbackRobotNews, this, std::placeholders::_1));
        RCLCPP_INFO(this->get_logger(), "String subscriber started!");
    }

private:
    void callbackRobotNews(const example_interfaces::msg::String::SharedPtr msg)
    {
        RCLCPP_INFO(this->get_logger(), "%s", msg->data.c_str());
    }

    rclcpp::Subscription<example_interfaces::msg::String>::SharedPtr subscriber;
};

int main(int argc, char **argv)
{
    rclcpp::init(argc, argv);
    auto node = std::make_shared<StringSubscriber>();
    rclcpp::spin(node);
    rclcpp::shutdown();
    return 0;
}
