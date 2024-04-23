
#include "rclcpp/rclcpp.hpp"

class MyNode: public rclcpp::Node
{
public:
    MyNode(): Node("log_minimal_oops")
    {
        RCLCPP_INFO(this->get_logger(),"Hello world from log minimal OOPS!");
    }

private:
    
};




int main(int argc, char * argv[])
{
    rclcpp::init(argc,argv);
    auto node = std::make_shared<MyNode>();
    rclcpp::spin(node);
    rclcpp::shutdown();

    return 0;
}
