/* Software License Agreement (BSD License)
 *
 * Copyright (c) 2011, Willow Garage, Inc.
 * All rights reserved.
 *
 * Redistribution and use in source and binary forms, with or without
 * modification, are permitted provided that the following conditions
 * are met:
 *
 *  * Redistributions of source code must retain the above copyright
 *    notice, this list of conditions and the following disclaimer.
 *  * Redistributions in binary form must reproduce the above
 *    copyright notice, this list of conditions and the following
 *    disclaimer in the documentation and/or other materials provided
 *    with the distribution.
 *  * Neither the name of Willow Garage, Inc. nor the names of its
 *    contributors may be used to endorse or promote products derived
 *    from this software without specific prior written permission.
 *
 * THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
 * "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
 * LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
 * FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
 * COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
 * INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
 * BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
 * LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
 * CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
 * LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
 * ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
 * POSSIBILITY OF SUCH DAMAGE.
 *
 * Auto-generated by genmsg_cpp from file /home/wqh/catkin_ws/src/my/baxter_common/baxter_core_msgs/msg/HeadPanCommand.msg
 *
 */


#ifndef BAXTER_CORE_MSGS_MESSAGE_HEADPANCOMMAND_H
#define BAXTER_CORE_MSGS_MESSAGE_HEADPANCOMMAND_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace baxter_core_msgs
{
template <class ContainerAllocator>
struct HeadPanCommand_
{
  typedef HeadPanCommand_<ContainerAllocator> Type;

  HeadPanCommand_()
    : target(0.0)
    , speed(0)  {
    }
  HeadPanCommand_(const ContainerAllocator& _alloc)
    : target(0.0)
    , speed(0)  {
    }



   typedef float _target_type;
  _target_type target;

   typedef int32_t _speed_type;
  _speed_type speed;




  typedef boost::shared_ptr< ::baxter_core_msgs::HeadPanCommand_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::baxter_core_msgs::HeadPanCommand_<ContainerAllocator> const> ConstPtr;
  boost::shared_ptr<std::map<std::string, std::string> > __connection_header;

}; // struct HeadPanCommand_

typedef ::baxter_core_msgs::HeadPanCommand_<std::allocator<void> > HeadPanCommand;

typedef boost::shared_ptr< ::baxter_core_msgs::HeadPanCommand > HeadPanCommandPtr;
typedef boost::shared_ptr< ::baxter_core_msgs::HeadPanCommand const> HeadPanCommandConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::baxter_core_msgs::HeadPanCommand_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::baxter_core_msgs::HeadPanCommand_<ContainerAllocator> >::stream(s, "", v);
return s;
}

} // namespace baxter_core_msgs

namespace ros
{
namespace message_traits
{



// BOOLTRAITS {'IsFixedSize': True, 'IsMessage': True, 'HasHeader': False}
// {'std_msgs': ['/opt/ros/hydro/share/std_msgs/cmake/../msg'], 'sensor_msgs': ['/opt/ros/hydro/share/sensor_msgs/cmake/../msg'], 'geometry_msgs': ['/opt/ros/hydro/share/geometry_msgs/cmake/../msg'], 'baxter_core_msgs': ['/home/wqh/catkin_ws/src/my/baxter_common/baxter_core_msgs/msg']}

// !!!!!!!!!!! ['__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_parsed_fields', 'constants', 'fields', 'full_name', 'has_header', 'header_present', 'names', 'package', 'parsed_fields', 'short_name', 'text', 'types']




template <class ContainerAllocator>
struct IsFixedSize< ::baxter_core_msgs::HeadPanCommand_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::baxter_core_msgs::HeadPanCommand_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::baxter_core_msgs::HeadPanCommand_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::baxter_core_msgs::HeadPanCommand_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::baxter_core_msgs::HeadPanCommand_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::baxter_core_msgs::HeadPanCommand_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::baxter_core_msgs::HeadPanCommand_<ContainerAllocator> >
{
  static const char* value()
  {
    return "990c3757495fec1dbde36b9b559e7bae";
  }

  static const char* value(const ::baxter_core_msgs::HeadPanCommand_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x990c3757495fec1dULL;
  static const uint64_t static_value2 = 0xbde36b9b559e7baeULL;
};

template<class ContainerAllocator>
struct DataType< ::baxter_core_msgs::HeadPanCommand_<ContainerAllocator> >
{
  static const char* value()
  {
    return "baxter_core_msgs/HeadPanCommand";
  }

  static const char* value(const ::baxter_core_msgs::HeadPanCommand_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::baxter_core_msgs::HeadPanCommand_<ContainerAllocator> >
{
  static const char* value()
  {
    return "#Header header\n\
float32 target # radians for target, 0 str\n\
int32 speed # between 0 and 100, 100 = max\n\
\n\
";
  }

  static const char* value(const ::baxter_core_msgs::HeadPanCommand_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::baxter_core_msgs::HeadPanCommand_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.target);
      stream.next(m.speed);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER;
  }; // struct HeadPanCommand_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::baxter_core_msgs::HeadPanCommand_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::baxter_core_msgs::HeadPanCommand_<ContainerAllocator>& v)
  {
    s << indent << "target: ";
    Printer<float>::stream(s, indent + "  ", v.target);
    s << indent << "speed: ";
    Printer<int32_t>::stream(s, indent + "  ", v.speed);
  }
};

} // namespace message_operations
} // namespace ros

#endif // BAXTER_CORE_MSGS_MESSAGE_HEADPANCOMMAND_H
